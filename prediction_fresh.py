import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from io import BytesIO
from PIL import Image
import requests

map_dict = {1: "Dog",
            0: "Cat"}


class PredictPipe():
    def validate_image(self, json_dict):
        if json_dict["image_url"].split(".")[-1] not in ['jpg', 'png', 'jpeg']:
            error = "The image should be in jpg, png or jpeg format"
            return error

    def downloadimage(self, json_dict):
        image_url = json_dict["image_url"]
        response = requests.get(image_url)
        img_bytes = BytesIO(response.content)
        return img_bytes

    def preprocess(self, image):
        img = Image.open(image)
        img = img.convert('RGB')
        img = img.resize((128, 128))
        img = img_to_array(img)
        img = img.reshape(-1, 128, 128, 3)
        return img

    def predict(self, image, model):
        prediction = model.predict(image)
        prediction = map_dict[int(prediction[0][0])]
        return prediction
