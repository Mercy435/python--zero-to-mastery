# import tensorflow as tf
from imageai.Prediction import ImagePrediction
import os

execution_path = os.getcwd()

prediction = ImagePrediction()
# prediction.setModelTypeASMobileNetV2()
# prediction.setModelPath(os.path.join(execution_path, "mobilenet_v2.h5"))
# prediction.loadModel()
#
# predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, "18.1 giraffe.jpg"), result_count=5 )
# for eachPrediction, eachProbability in zip(predictions, probabilities):
#     print(eachPrediction , " : " , eachProbability)