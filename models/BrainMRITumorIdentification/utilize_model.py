import numpy as np
import cv2
import tensorflow as tf
import argparse

parser = argparse.ArgumentParser()  
parser.add_argument("image_path", help = "Path of the image for Tumor Identification")
args = parser.parse_args()  

with open('classifier-resnet-model.json', 'r') as json_file:
    json_savedModel = json_file.read()

# load the model architecture
model = tf.keras.models.model_from_json(json_savedModel)
model.load_weights('classifier-resnet-weights.hdf5')
model.compile(optimizer="Adam",loss="categorical_crossentropy", metrics=["accuracy"])

def identify_tumor(file_path):
    img = cv2.imread(file_path, cv2.IMREAD_COLOR)
    img = cv2.resize(img,(256,256))
    img = np.array(img)
    img = img/255
    img = img.reshape((1, 256, 256, 3))
    prediction = model.predict(img)

    labels = {0: 'No Tumor', 1: 'Tumor'}
    result = labels[np.argmax(prediction[0])]

    return result

if __name__=="__main__":
    print(identify_tumor(args.image_path))