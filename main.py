from fastapi import FastAPI
from congruential_lehmer import congruential, congruentialParam, NonPrimeRelativesNumbers

app = FastAPI()
  
@app.post("/lehmer")
def get_random_numbers(params: congruentialParam):
    try:
        x_list, r_list = congruential(params)
        result = {
            "x_list": x_list.tolist(),
            "r_list": r_list.tolist()
        }
    except NonPrimeRelativesNumbers as e:
        result = {"error": str(e)}

    return result