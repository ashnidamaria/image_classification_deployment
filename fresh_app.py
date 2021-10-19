from fastapi import FastAPI
from prediction_fresh import PredictPipe
import tensorflow as tf
import uvicorn
from api_io import PredictApiRequest, PredictApiResponse


model = tf.keras.models.load_model("ck_cnn_model.hdf5")
app = FastAPI()
pp = PredictPipe()


@app.get('/')
async def home():
    return f"Welcome to image classification API"


@app.post('/Predict', response_model=PredictApiResponse)
async def predict(image_url: PredictApiRequest):
    json_dict = image_url.dict()
    errors = pp.validate_image(json_dict=json_dict)
    if errors is None:
        image = pp.downloadimage(json_dict=json_dict)
        image = pp.preprocess(image=image)
        prediction = pp.predict(image=image, model=model)
        return_string = f'Predicted label for this image is {prediction}'
        return_dict = {"return_string": return_string}
    else:
        return_dict = {"errors": errors}
    return return_dict



if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)
