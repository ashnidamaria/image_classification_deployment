"""
 Fast API implementation
"""
from base.api_io_model import PredictApiRequest, PredictApiResponse
from pipeline.prediction_pipeline import PredictPipe
from fastapi import FastAPI
import uvicorn
import tensorflow as tf

app = FastAPI()
prediction_pipeline = PredictPipe()

model = tf.keras.models.load_model("./model/ck_cnn_model.hdf5")


@app.get('/')
async def home():
    return f"Welcome to image classification API"


@app.post('/server/predict', response_model=PredictApiResponse)
async def model_predict(request_params: PredictApiRequest):
    """
    Model prediction API
    :param request_params:
    :return:
    """
    json_dict = request_params.dict()
    response = prediction_pipeline.run(json_dict, model)
    return response


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)
