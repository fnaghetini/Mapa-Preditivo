### A Pluto.jl notebook ###
# v0.16.1

using Markdown
using InteractiveUtils

# This Pluto notebook uses @bind for interactivity. When running this notebook outside of Pluto, the following 'mock version' of @bind gives bound variables a default value (instead of an error).
macro bind(def, element)
    quote
        local el = $(esc(element))
        global $(esc(def)) = Core.applicable(Base.get, el) ? Base.get(el) : missing
        el
    end
end

# ╔═╡ ede1ab03-87e3-4c42-8e4d-51b3e8829aea
begin
	# configuração do ambiente
	import Pkg; Pkg.activate(mktempdir())
	
	# download de pacotes
	Pkg.add("CSV"); Pkg.add("DataFrames"); Pkg.add("Query")
	Pkg.add("GeoStats"); Pkg.add("Distributions")
	Pkg.add("PlutoUI"); Pkg.add("Plots")
	
	# importação dos pacotes
	using CSV, DataFrames, Query
	using GeoStats, Distributions, Random
	using PlutoUI
	using Plots; gr(format="png")
end;

# ╔═╡ b390f148-a4fa-4ad6-8d0c-655f5d1fb091
md"""

![geostats-logo](https://logodownload.org/wp-content/uploads/2015/02/ufmg-logo-2.png)

"""

# ╔═╡ cb520500-14bc-11ec-3ceb-d50b22b326dc
md"""

# Fenômenos Associados a Dados Geoespaciais

###### Trabalho de Conclusão de Curso - Geologia / IGC / UFMG

Autores: [Franco Naghetini](https://github.com/fnaghetini) e [Guilherme Silveira](https://github.com/guiasilveira)

"""

# ╔═╡ 504fb623-6b10-4905-8ded-5bc7a89b693e
PlutoUI.TableOfContents(aside=true, title="Sumário",
						indent=true, depth=3)

# ╔═╡ 04893b21-d20c-4084-ad58-f060c129af5f
md"""

### Introdução

Sabe-se que a aplicação de técnicas de Aprendizado de Máquina para a solução de problemas geocientíficos não pode ser conduzida de maneira direta, uma vez que algumas peculiaridades dos dados geoespaciais violam premissas fundamentais da teoria clássica. Nesse sentido, dois fenômenos comumente ocorrem em problemas geoespaciais:

1. Autocorrelação espacial entre amostras de uma mesma variável

2. Distorção da distribuição bivariada entre os conjuntos de treino e teste

**Nota:** Algumas células deste notebook foram ocultadas. Caso deseje visualizar alguma delas, clique no ícone do olho, localizado à esquerda da célula em questão.

"""

# ╔═╡ 5810feee-79a6-400b-9d56-4eafad2f8d3a
md"""### Importação dos dados

Abaixo, os dados de treino e teste gerados no [segundo notebook](https://github.com/fnaghetini/Mapa-Preditivo/blob/main/2-predictive_litho_map.ipynb) são importados.

"""

# ╔═╡ a88ea1b6-9291-4485-a573-68be7f34529e
begin
	# link dos dados
	url_train = "https://raw.githubusercontent.com/fnaghetini/Mapa-Preditivo/main/data/train.csv"
	url_test = "https://raw.githubusercontent.com/fnaghetini/Mapa-Preditivo/main/data/test.csv"
	
	# download dos dados
	file_train = download(url_train)
	file_test = download(url_test)
	
	# conversão em dataframe
	train = CSV.File(file_train) |> DataFrame
	test = CSV.File(file_test) |> DataFrame
end;

# ╔═╡ 77be9d2b-8ba2-4b29-86e9-ad013b83202f
# dados de treino
first(train, 5)

# ╔═╡ bc5c15d5-a6df-4051-a068-343c22efff8a
# dados de teste
first(test, 5)

# ╔═╡ fa317980-08e7-42d1-bfa2-3c33b4d483b1
md""" ### Pré-processamento

Nesta seção, os dados de treino e teste são submetidos a duas etapas simples de pré-processamento:

1. Seleção das variáveis de interesse

2. Estandardização das variáveis

Ressalta-se que todas as variáveis, exceto as bandas Landsat 8 e a variável dependente são selecionadas na primeira etapa. Em seguida as features selecionadas são estandardizadas e passam a seguir uma distribuição normal padrão, com μ = 0 e σ = 1.

"""

# ╔═╡ c71cc549-2710-4aba-a10e-204056b937c9
begin
	
	# variáveis de interesse
	COORD = [:X,:Y]
	FEAT = [:GT,:K,:TH,:U,:CT,:U_K,:TH_K,:U_TH,:MDT]
	
	# seleção das variáveis
	f1(table) = select(table, [COORD;FEAT])

	# estandardização das variáveis
	function f2(table)
		table_out = copy(table)
		for f ∈ FEAT
			x = table[!,f]
			
			μ = mean(x)
			σ = std(x, mean=μ)
			
			table_out[!,f] = (x .- μ) ./ σ
		end
		table_out
	end
	
	# execução do pré-processamento
	Tₐ = train |> f1 |> f2
	Tᵦ = test |> f1 |> f2
end;

# ╔═╡ 72f6bdec-2236-4008-8f0e-da1fe4d39c2e
md""" ### Verificação de shift na distribuição bivariada

Na *Figura 01*, são apresentados dois diagramas de dispersão, sendo o da esquerda relacionado ao conjunto de treino e o da direita ao conjunto de teste.

O objetivo é verificar se existe algum tipo de distorção (shift) da distribuição bivariada entre os conjuntos de treino e teste.
"""

# ╔═╡ e488e530-7945-420f-92f6-eee3997ff82d
md"""
Distribuição bivariada entre as variáveis $(@bind X₁ Select(string.(FEAT), default="U")) e $(@bind X₂ Select(string.(FEAT), default="TH"))
"""

# ╔═╡ baee023f-3532-4294-a7c3-5fd5e0cc6ada
begin
	# georreferenciamento dos dados
	train_georef = georef(Tₐ, (:X,:Y))
	test_georef = georef(Tᵦ, (:X,:Y))
	
	# distribuição bivariada (treino)
	p1 = distplot2d(train_georef, X₁, X₂, quantiles=[0.10,0.25,0.50,0.75,0.90],
					color=:red, title="Treino")
	
	# distribuição bivariada (teste)
	p2 = distplot2d(test_georef, X₁, X₂, quantiles=[0.10,0.25,0.50,0.75,0.90],
					color=:blue, title="Teste")
	
	# plotagem das distribuições bivariadas
	plot(p1, p2, link = :both, aspect_ratio = :equal, size = (700, 400))
	
end

# ╔═╡ 5dfa7583-7716-4009-9aa2-48d1133ca4d0
md" **Figura 01:** Distribuição bivariada entre $X₁ e $X₂ nos conjuntos de treino (vermelho) e teste (azul). "

# ╔═╡ 341990c2-8adf-4f6e-b488-f0723942ad9e
md"""

* Nota-se que, para quaisquer variáveis selecionadas, as distribuições bivariadas resultantes são semelhantes nos conjuntos de treino e teste. Essa observação é mais clara no caso dos canais radiométricos (i.e. `U`, `TH` e `K`).

* Portanto, pode-se dizer que o shift da distribuição bivariada entre os conjuntos de treino e teste é pouco expressivo ou inexistente. Isso era de fato esperado, uma vez que ambos os conjuntos foram reamostrados de uma mesma área.

"""

# ╔═╡ 1b23c0a0-73af-418a-a425-e7d94d3602e9
begin
	# Converte coordenadas geológicas em cartesianas
	function sph2cart(azi)
		θ = deg2rad(azi)
		sin(θ), cos(θ)
	end
end;

# ╔═╡ a8a02cd5-b512-434b-92dc-84e990e520ce
md"""
Variograma da variável $(@bind Z Select(string.(FEAT), default="K"))
"""

# ╔═╡ ae10ce94-bfab-4ee2-9049-234bf3d244b8
md""" ### Verificação de autocorrelação espacial

A *Figura 02* apresenta o variograma experimental N-S da variável $Z. O objetivo é verificar a existência de correlação espacial nas variáveis independentes.

"""

# ╔═╡ eb9705da-ddcc-4af9-a7d6-08843e5a8769
begin
	# concatenação dos conjuntos de treino e teste
	data = [train[!,[COORD;FEAT]]
		    test[!,[COORD;FEAT]]]
	
	# georrefrenciamento dos dados
	data_georef = georef(data, (:X,:Y))
	
	# semente aleatória
	Random.seed!(42)
	
	# variograma experimental N-S
	γ = DirectionalVariogram(sph2cart(0), data_georef, Symbol(Z),
		                      maxlag = 4000, nlags = 20)
	
	
	# configurações de plotagem do variograma
	plot(γ, color = :red, ms = 5, legend=false, xlims=(0,4200))
	
end

# ╔═╡ d4155a15-203d-451c-9156-783407f1e5fe
md" **Figura 02:** Variograma experimental N-S da variável $Z. "

# ╔═╡ 5497720d-5333-4368-9625-ae8a2b9da7c4
md"""

* Nota-se que, para qualquer variável selecionada, o variograma direcional resultante apresenta uma clara estrutura espacial.

* Portanto, pode-se afirmar que as variáveis utilizadas no projeto apresentam uma correlação espacial significativa. Isso já era esperado, uma vez que os próprios mapas de localizaçao dessas variáveis apresentam estrutura espacial.

"""

# ╔═╡ Cell order:
# ╟─ede1ab03-87e3-4c42-8e4d-51b3e8829aea
# ╟─b390f148-a4fa-4ad6-8d0c-655f5d1fb091
# ╟─cb520500-14bc-11ec-3ceb-d50b22b326dc
# ╟─504fb623-6b10-4905-8ded-5bc7a89b693e
# ╟─04893b21-d20c-4084-ad58-f060c129af5f
# ╟─5810feee-79a6-400b-9d56-4eafad2f8d3a
# ╠═a88ea1b6-9291-4485-a573-68be7f34529e
# ╠═77be9d2b-8ba2-4b29-86e9-ad013b83202f
# ╠═bc5c15d5-a6df-4051-a068-343c22efff8a
# ╟─fa317980-08e7-42d1-bfa2-3c33b4d483b1
# ╠═c71cc549-2710-4aba-a10e-204056b937c9
# ╟─72f6bdec-2236-4008-8f0e-da1fe4d39c2e
# ╟─e488e530-7945-420f-92f6-eee3997ff82d
# ╟─baee023f-3532-4294-a7c3-5fd5e0cc6ada
# ╟─5dfa7583-7716-4009-9aa2-48d1133ca4d0
# ╟─341990c2-8adf-4f6e-b488-f0723942ad9e
# ╟─1b23c0a0-73af-418a-a425-e7d94d3602e9
# ╟─ae10ce94-bfab-4ee2-9049-234bf3d244b8
# ╟─a8a02cd5-b512-434b-92dc-84e990e520ce
# ╟─eb9705da-ddcc-4af9-a7d6-08843e5a8769
# ╟─d4155a15-203d-451c-9156-783407f1e5fe
# ╟─5497720d-5333-4368-9625-ae8a2b9da7c4
