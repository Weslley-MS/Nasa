# Nasa

## 1 - Qual o objetivo do comando cache em Spark?
R: O comando armazena os dados da execução de ações em memória para que quando outra ação for chamada, não seja necessário realizar todo o processamento novamente.

## 2 - O mesmo código implementado em Spark é normalmente mais rápido que a implementação equivalente em
MapReduce. Por quê?
R: O Spark faz o processamento na memória, diferente do MapReduce que processa em disco.

## 3 - Qual é a função do SparkContext?
R: Carregar as funções e bibliotecas do Spark.

## 4 - Explique com suas palavras o que é Resilient Distributed Datasets (RDD).
R: É uma coleção de objetos imutaveis particionados em um conjunto de nodos do cluster.

## 5 - GroupByKey é menos eficiente que reduceByKey em grandes dataset. Por quê?
R: O  groupByKey faz o embaralhamento entre pares antes do particionamento do RDD enquanto o  reduceByKey mescla os pares antes do embaralhamento.

## 6 - 
1 - val textFile = sc.textFile("hdfs://...")
2 - val counts = textFile.flatMap(line => line.split(" "))
3 - .map(word => (word, 1))
4 - .reduceByKey(_ + _)
5 - counts.saveAsTextFile("hdfs://...")

1 - seleciona um arquivo texto do hdfs e salva na variavel textFile
2 - quebra cada linha em palavras, depois coloca cada palavra por linha
3 - transforma cada palavra em uma tupla com a palavra como chave e o número 1 como valor
4 - soma os valores das chaves iguais para contar as ocorrencias dela
5 - salva o resultado no hdfs
