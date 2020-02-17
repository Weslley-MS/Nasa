# Teste Spark

### 1 - Qual o objetivo do comando cache em Spark?
R: O comando armazena os dados da execução de ações em memória para que quando outra ação for chamada, não seja necessário realizar todo o processamento novamente.

### 2 - O mesmo código implementado em Spark é normalmente mais rápido que a implementação equivalente em
MapReduce. Por quê?
R: O Spark faz o processamento na memória, diferente do MapReduce que processa em disco.

### 3 - Qual é a função do SparkContext?
R: Carregar as funções e bibliotecas do Spark.

### 4 - Explique com suas palavras o que é Resilient Distributed Datasets (RDD).
R: É uma coleção de objetos imutaveis particionados em um conjunto de nodos do cluster.

### 5 - GroupByKey é menos eficiente que reduceByKey em grandes dataset. Por quê?
R: O  groupByKey faz o embaralhamento entre pares antes do particionamento do RDD enquanto o  reduceByKey mescla os pares antes do embaralhamento.

### 6 - 
1 - val textFile = sc.textFile("hdfs://...") <br />
2 - val counts = textFile.flatMap(line => line.split(" ")) <br />
3 - .map(word => (word, 1)) <br />
4 - .reduceByKey(_ + _) <br />
5 - counts.saveAsTextFile("hdfs://...") <br />

1 - seleciona um arquivo texto do hdfs e salva na variavel textFile <br />
2 - quebra cada linha em palavras, depois coloca cada palavra por linha<br />
3 - transforma cada palavra em uma tupla com a palavra como chave e o número 1 como valor <br />
4 - soma os valores das chaves iguais para contar as ocorrencias dela <br />
5 - salva o resultado no hdfs <br />

### 7 -
1. Número de hosts únicos. <br />
2. O total de erros 404. <br />
3. Os 5 URLs que mais causaram erro 404. <br />
4. Quantidade de erros 404 por dia. <br />
5. O total de bytes retornados <br />

1 -  127108 hosts unicos <br />
2 - 18682 erros 404 <br />
3 - <br />
|hoohoo.ncsa.uiuc.edu|     251| <br />
|piweba3y.prodigy.com|     134| <br />
|piweba1y.prodigy.com|      99| <br />
|www-d4.proxy.aol.com|      88| <br />
|piweba4y.prodigy.com|      71| <br />
4 - 
|06/Jul/1995|     640|<br />
|19/Jul/1995|     638|<br />
|30/Aug/1995|     571|<br />
|07/Jul/1995|     569|<br />
|07/Aug/1995|     537|<br />
|13/Jul/1995|     531|<br />
|31/Aug/1995|     526|<br />
|05/Jul/1995|     497|<br />
|11/Jul/1995|     471|<br />
|12/Jul/1995|     470|<br />
|03/Jul/1995|     470|<br />
|18/Jul/1995|     465|<br />
|20/Jul/1995|     428|<br />
|29/Aug/1995|     420|<br />
|24/Aug/1995|     420|<br />
|25/Aug/1995|     415|<br />
|14/Jul/1995|     411|<br />
|28/Aug/1995|     410|<br />
|17/Jul/1995|     406|<br />
|10/Jul/1995|     398|<br />
|08/Aug/1995|     390|<br />
|06/Aug/1995|     373|<br />
|27/Aug/1995|     367|<br />
|26/Aug/1995|     366|<br />
|04/Jul/1995|     359|<br />
|09/Jul/1995|     348|<br />
|04/Aug/1995|     346|<br />
|23/Aug/1995|     345|<br />
|15/Aug/1995|     327|<br />
|01/Jul/1995|     316|<br />
|20/Aug/1995|     312|<br />
|10/Aug/1995|     306|<br />
|21/Aug/1995|     305|<br />
|03/Aug/1995|     303|<br />
|08/Jul/1995|     302|<br />
|02/Jul/1995|     291|<br />
|14/Aug/1995|     287|<br />
|22/Aug/1995|     285|<br />
|09/Aug/1995|     279|<br />
|17/Aug/1995|     271|<br />
|11/Aug/1995|     263|<br />
|16/Aug/1995|     259|<br />
|16/Jul/1995|     257|<br />
|18/Aug/1995|     256|<br />
|15/Jul/1995|     254|<br />
|01/Aug/1995|     243|<br />
|05/Aug/1995|     236|<br />
|13/Aug/1995|     216|<br />
|19/Aug/1995|     209|<br />
|12/Aug/1995|     196|<br />
|21/Jul/1995|     122|<br />

5 - 58.299161189 gigas recebidos

# Observações:
 O código foi feito no google colab, para executar basta apenas dar "! pip install pyspark" para carregar o pyspark e subir as tabelas com os seguintes comandos:<br />
 
from google.colab import files<br />
uploaded = files.upload()<br />
