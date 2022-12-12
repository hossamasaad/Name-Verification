import os
import sys
import time
import uvicorn
import joblib
from fastapi import FastAPI
from pydantic import BaseModel

# Hide tensorflow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

sys.path.append(os.path.realpath(""))
from src import Prediction



# load the model
print('loading the model.....')
model = joblib.load('models/model_v3.pkl')
print('Model loaded successfully.')


# Create predictor
print('Creating predictor....')
predictor = Prediction(model)
print('Predictor created successfully.')


class Item(BaseModel):
    name: str

class Response(BaseModel):
    result: str
    prediction: str
    excution_time: str


app = FastAPI()


@app.post('/is_real_name/')
async def is_real_name(item: Item):

    try:
        start = time.time()

        prediction = predictor.predict([item.name])
        result = predictor.convert_prediction_into_confidence(prediction)
        
        end = time.time()
        excution_time = (end - start) * 1000
        
        return Response(result        = result[0],
                        prediction    = "{}".format(prediction[0][0]),
                        excution_time = "{:.2f} ms".format(excution_time))

    except KeyError:
        return {"Result": "Please enter valid arabic chars"}