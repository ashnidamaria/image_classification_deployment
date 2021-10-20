"""
Python script to implement prediction pipeline
"""

from base.pipeline_ import PredictBase
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from io import BytesIO
from PIL import Image
import requests

map_dict = {1: "Dog", 0: "Cat"}


class PredictPipe(PredictBase):
    def validate_image(self, json_dict):
        if json_dict["image_url"].split(".")[-1] not in ['jpg', 'png', 'jpeg']:
            error = "The image should be in jpg, png or jpeg format"
            return error

    def download_image(self, json_dict):
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
        prediction = f'Predicted label for this image is  {prediction}'
        return prediction

        pass

    def run(self, json_dict, model):
        error = self.validate_image(json_dict=json_dict)
        if error is None:
            image = self.download_image(json_dict)
            image = self.preprocess(image=image)
            prediction = self.predict(image,model)
            return_dict = {"return_string": prediction}
        else:
            return_dict = {"errors": error}
        return return_dict
