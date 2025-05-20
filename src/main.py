from fastapi import FastAPI
from data_model import Water
import pandas as pd
import pickle

app = FastAPI(title="water portability",description="water portability project api using dvc")

with open("/media/brainwired/D/BW_ML/01_AUG_FARM_TEST/study/MLOPS_MACHINE_LEARNING_PIPLELINES/models/model.pkl",'rb') as m:
    prediction_model = pickle.load(m)

@app.get("/")
def home():
    return "welcome to water portability"

@app.post("/Prediction")
def prediction(details:Water):

    data = {'ph':[details.ph],'Hardness':[details.Hardness],'Solids':[details.Solids],'Chloramines':[details.Chloramines],
            'Sulfate' : [details.Sulfate],
            'Conductivity' : [details.Conductivity],
            'Organic_carbon': [details.Organic_carbon],
            'Trihalomethanes': [details.Trihalomethanes],
            'Turbidity' : [details.Turbidity]
    }

    df = pd.DataFrame(data)
    print(df)
    result = prediction_model.predict(df)
    print(result[0])
    if result[0]==1:
        return "water is consuamble"
    else:
        return "Not good"
