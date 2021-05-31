import tensorflow as tf
from keras.models import load_model
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go
import numpy as np

model = tf.keras.models.load_model("generator.h5", custom_objects=None, compile=True, options=None)
model.compile() 
batch_size = 5
latent_dim = 128
random_latent_vectors = tf.random.normal(shape=(batch_size, latent_dim))
generated_images = model.predict(random_latent_vectors)
#fig = go.Figure(figsize=[16,8])
#plt.axis("off")
#plt.imshow((generated_images*255).astype("int"))

def image_generator(batch_size, latent_dim):
    random_latent_vectors = tf.random.normal(shape=(batch_size,latent_dim))
    generated_images = model.predict(random_latent_vectors)
    return generated_images