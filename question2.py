import networkx as nx
"""Gere uma rede “livre de escala” com 10000 vértices, grau médio < 𝑘 >= 20 e 
expoente 𝛾 = 2.5.  Comece com 5 vértices infectados escolhidos aleatoriamente. Execute 
múltiplas simulações da propagação da infecção pelo modelo SIS com os parâmetros abaixo e 
compare com os resultados esperados. (sugestão: faça em torno de 100 simulações e descreva 
o comportamento da epidemia “na média”) 
a. 𝛽 =0.01 e 𝜇 = 0.1 
b. 𝛽 =0.01 e 𝜇 = 0.2 
c. 𝛽 =0.01 e 𝜇 = 0.3 
Descreva o comportamento da epidemia e compare com o item (1) """