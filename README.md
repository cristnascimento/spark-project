# Spark and PySpark

## Description

This project is a simple way of introducing some of the essential concepts in [Apache Spark](https://spark.apache.org/).

## Dependencies

* Java 8
* Python 3
* Spark 2.4.6

## Install Spark

1. Download from [Spark website](https://spark.apache.org/downloads.html)
1. Extract to local folder
```console
$ tar xzvf <downloaded-file>.gz
```
1. Set up path. Add these lines to ~/.bashrc
```console
export SPARK_HOME=/home/thais/cristiano/git/cristnascimento/spark/spark-2.4.6-bin-hadoop2.7
export PATH=$PATH:$SPARK_HOME/bin
```
Then activate it
```console
$ source ~/.bashrc
```

## Test Spark Install

```console
$ cd $SPARK_HOME
$ bin/<test> PiSpark 10
```

## Test PySpark

Dataset

```console
Year,State1,Team1,State2,Team2
...
```

Sample, champions.txt

```txt
1959,Bahia,Bahia
1960,São Paulo,Palmeiras
1961,São Paulo,Santos
1962,São Paulo,Santos
1963,São Paulo,Santos
1964,São Paulo,Santos
1965,São Paulo,Santos
1966,Minas Gerais,Cruzeiro
1967,São Paulo,Palmeiras
1967,São Paulo,Palmeiras
1968,Rio de Janeiro,Botafogo
...
```

Where

```console
State1, Team1 = Champion of the National league

State2, Team2 = Champion of the National cup
```
Python program

```py
from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    conf = SparkConf().setAppName("champions counter").setMaster("local")
    sc = SparkContext(conf = conf)

    rdd = sc.textFile("champions.txt")

    # Team name
    teams = rdd.map(lambda line: line.split(",")[2])

    # How many years it was the winner of the National league
    count = teams.countByValue()

    # Sort descending
    results = sorted(count.items(), key=lambda item: item[1], reverse=True)

    for team, counter in results:
        print ("{0}: {1}".format(team, counter))

```
Run

```console
$ spark-submit <your-program>.py
```

## Documentation

This is a quick reference of the **class pyspark.RDD** methods.

**count()**

**countByKey()**

**countByValue()**

**collect()**

**distinct()**

**filter()**

**first()**
  Return the first element in this RDD.
```python
>>> sc.parallelize([2, 3, 4]).first()
2
>>> sc.parallelize([]).first()
Traceback (most recent call last):
    ...
ValueError: RDD is empty
```
**flapMap()**

**groupBy()**

**intersection()**

**map()**

**max()**

**mean()**

**min()**

**reduce()**

**sample()**

**saveAsHadoopDataset()**

**saveAsHadoopFile()**

**saveAsTextFile()**

**sortBy()**

**sum()**

**take()**

**union()**

### References
* [PySpark RDD documentation](https://spark.apache.org/docs/2.4.6/api/python/pyspark.html#pyspark.RDD)
