from pyspark.sql import DataFrame
from pyspark import SparkContext, SQLContext
from pyspark.ml.feature import StringIndexer, VectorIndexer
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.sql import SparkSession
from pyspark.ml.feature import Imputer
from pyspark.sql.functions import when
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import StandardScaler
from pyspark.mllib.util import MLUtils
from pyspark.mllib.evaluation import MulticlassMetrics
from pyspark.ml.classification import RandomForestClassifier



spark = SparkSession.builder.master("local").appName("classification of wine").config("spark.some.config.option","some-value").getOrCreate()

set_data = spark.read.csv('TrainingDataset.csv',header='true', inferSchema='true', sep=';')

valid_data = spark.read.csv('ValidationDataset.csv',header='true', inferSchema='true', sep=';')


fColumns = [x for x in orignalData.columns if x != 'quality']
vassembler = VectorAssembler(inputCols=featureColumns, outputCol="Values")
in_trans = vassembler.transform(set_Data)
in_trans.cache()


feature = [x for x in validationData.columns if x != 'quality']
assembler = VectorAssembler(inputCols=feature, outputCol="Values")
valid_trans = assembler.transform(valid_Data)


forest = RandomForestClassifier(labelCol="quality", featuresCol="Values", numTrees=20)
RModel = forest.fit(transformation)


predict_Data = RModel.transform(valid_Trans)

print()
eval = MulticlassClassificationEvaluator(
    labelCol="quality", predictionCol="prediction", metricName="f1")
accuracy = eval.evaluate(predictionData)
print("Error Testing = %g" % (1.0 - accuracy))

print()

trans_data = RModel.transform(valid_Trans)
print(eval.getMetricName(), "Accuracy = " , eval.evaluate(trans_data))
print()
