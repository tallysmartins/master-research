# Seleção de ferramentas

1) Escolha de 3 bibliotecas de mapa interativos para python
	- geoplotlib (GUI)
	- folium (JS)
	- dash (JS)

2) Fazer um toy application com cada uma

- a) Plotar os pontos de uma linha
- b) Plotar um grafo com a trajetória de uma linha
- c) Fazer uma animação de uma linha
- d) Plotar a animação de todas as linhas
- e) Plotar o grafo de todas os carros
- f) Tentar adicionar um filtro: e.g time > 3

|   -   | geoplotlib | folium | dash |
|:-----:|:----------:|:------:|------|
| **a** |      v     |   -    |   -  |
| **b** |      v     |   -    |   -  |
| **c** |      v     |   -    |   -  |
| **d** |      v     |   -    |   -  |
| **e** |      v     |   -    |   -  |
| **f** |      -     |   -    |   -  |

Testar com 3 tamanhos de dados:

- Small = 1_000_000
- Medium = 10_000_000
- Large = 30_000_000

3) Procurar exemplos de bundling na lib ou como plotar o resultado do bundling
4) Precisa de GPU? Se sim, como a lib faria essa integração?

## Observações:

### geoplotlib:
- cor das linhas do grafo da trajetória é com base na distância entre os pontos e algumas
acabam ficando brancas. Para modificar isso devo utilizar uma layer própria com
esse comportamento modificado
([ver issue e PR aberto](https://github.com/andrea-cuttone/geoplotlib/issues/26))

## Links:

[Comparison of bokeh and dash](https://blog.sicara.com/bokeh-dash-best-dashboard-framework-python-shiny-alternative-c5b576375f7f)

[Several python plot libraries - jupytalk](http://www.xavierdupre.fr/app/jupytalk/helpsphinx/notebooks/10_plotting_libraries.html#geoplotlib-for-maps-in-a-gui)

[Tutorial folium](https://blog.prototypr.io/interactive-maps-with-python-part-1-aa1563dbe5a9)

[Folium notebooks examples](http://nbviewer.jupyter.org/github/python-visualization/folium/tree/master/examples/)
