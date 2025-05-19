import requests


url = 'http://127.0.0.1:8000/Prediction'


data = {
  "ph": 1,
  "Hardness": 1,
  "Solids": 1,
  "Chloramines": 1,
  "Sulfate": 1,
  "Conductivity": 1,
  "Organic_carbon": 1,
  "Trihalomethanes": 1,
  "Turbidity": 1
}
import json
result = requests.post(url=url,data=json.dumps(data)) 
print(result.text)