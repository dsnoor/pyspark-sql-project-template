def run(spark, config):
    df = spark.read.csv(config['relative_path'] + config['babynames_file_path'], header=True)

    df.printSchema()

    df.limit(10).show()
