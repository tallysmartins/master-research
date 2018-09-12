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


- Sharp questions

1) Defina um problema pequeno, pense em perguntas que quero responder e formule o
problema em uma frase: (data-science ou data-viz?)

- Como estava o trânsito na avenida paulista no dia x as x horas
	a) Estava congestionado? Como comparar alguma ação de melhoria que eu tenha tomado?

- Qual região recebe mais fluxo de entrada de pessoas durante o dia
- Como é a mudança do fluxo de entrada de pessoas em diferentes dias/climas?
- Onde moram a maioria das pessoas que vão para o centro
- Qual a velocidade média das ruas as 11 da manha
- Qual a melhor rota para se chegar de um ponto A até um ponto B levando
em consideração o tráfego?

---------------- Para deixar o problema mais claro/interessante ---------------
How can we translate data into dollars?
What impact do I want to make with this data?
What business value does our model bring to the table?
What will save us lots of money?
What can be done to make our business run more efficiently?

2) Que dados tenho/preciso para responder as questões levantadas?

3) Vamos limpar os dados 
	- Tem missing data?
	- Tem veiculo com menos de 2 pontos? Quantas?
	- Tem viagens com menos de 4 pontos? Quantas?
	- Qual o tamanho do meu dataset? O que ele representa?
	- Quais as features eu tenho e qual formato?
	- Como seria um próximo dataset?
	- Vamos automatizar esse check para quando vier um outro dataset

4) Vamos explorar os dados, identificar possíveis padrões/anomalias... use a criatividade (pensando no problema escolhido)

5) É hora de criar um modelo para visualizar, predizer, detectar as coisas 

6) Conte a história com emoção, explique para uma criança, volte ao problema
# 5 Questions Data Science can answer

- Is this A or B? (Classification algorithms)
- Is this weird? (Anomaly detection)
- How much? How many? (Regression algorithms)
- How is this organized? (Clustering algorithms)
- What should I do now? (Reinforcement learning)

