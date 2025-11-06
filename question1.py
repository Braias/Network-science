"""Gere uma rede aleatória (ER) com 10000 vértices e grau médio < 𝑘 >= 20.  Comece 
com 5 vértices infectados escolhidos aleatoriamente. Execute múltiplas simulações da 
propagação da infecção pelo modelo SIS com os parâmetros abaixo e compare com os 
resultados esperados. (sugestão: faça em torno de 100 simulações e descreva o 
comportamento da epidemia “na média”) 
a. 𝛽 =0.02 e 𝜇 = 0.1 
b. 𝛽 =0.02 e 𝜇 = 0.4 
c. 𝛽 =0.02 e 𝜇 = 0.5 
Mostre que se 𝑅_0 = 𝛽<𝑘>/(𝜇) >1 então a doença se fixa na rede no modelo SIS de campo médio."""
import networkx as nx
