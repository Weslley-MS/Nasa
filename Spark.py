#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyspark import SparkContext
sc = SparkContext.getOrCreate()
sc1 = SQLContext(sc)

df = sc1.read.csv('access_log_Aug95', sep = ' ')
df2 = sc1.read.csv('access_log_Jul95', sep = ' ')
df = df.union(df2)
df = df.withColumn("data", df._c3.substr(2,11))
df = df.selectExpr("_c0 as host","data as data","_c6 as codigo","_c7 as bytes")
df.write.saveAsTable('nasa')

q1 = sc1.sql("select count(distinct(host)) as HostUnicos from  nasa")
q1.show()

q2 = sc1.sql("select count(*) as Erros404 from  nasa where codigo = 404")
q2.show()

q3 = sc1.sql("select host,count(*) as Erros404 from  nasa where codigo = 404 group by host order by Erros404 desc")
q3.show(5)

q4 = sc1.sql("select data,count(*) as Erros404 from  nasa where codigo = 404 group by data order by Erros404 desc")
q4.show()

q5 = sc1.sql("select (sum(bytes)/ 1000000000) Bytes from  nasa")
q5.show()

