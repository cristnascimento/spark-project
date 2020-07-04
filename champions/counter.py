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
