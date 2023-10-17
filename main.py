from fastapi import FastAPI, Form
from congruent_lehmer import congruentLehmer, lehmerParams, NonPrimeRelativesNumbers
from congruent_mult import congruentMult, multParams, NonOddSeedError
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from productos_medios import prodMedios, prodMParams, nonDDigitNumber

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return FileResponse("static/index.html")

@app.post("/mult")
async def procesar_datos(
    x0: int = Form(...),
    k: int = Form(...),
    g: int = Form(...)
):
    params = {
        "x0": x0,
        "k": k,
        "g": g
    }

    try:
        x_list, r_list = congruentMult(multParams(**params))
        result = {
            "x_list": x_list.tolist(),
            "r_list": r_list.tolist()
        }
    except NonOddSeedError as e:
        result = {"error": str(e)}

    return result


@app.post("/lehmer")
async def procesar_datos(
    x0: int = Form(...),
    k: int = Form(...),
    g: int = Form(...),
    c: int = Form(...),
):
    params = {
        "x0": x0,
        "k": k,
        "g": g,
        "c": c
    }

    try:
        x_list, r_list = congruentLehmer(lehmerParams(**params))
        result = {
            "x_list": x_list.tolist(),
            "r_list": r_list.tolist()
        }
    except NonPrimeRelativesNumbers as e:
        result = {"error": str(e)}

    return result

@app.post("/prodM")
async def procesar_datos(
    D: int = Form(...),
    x0: int = Form(...),
    x1: int = Form(...),
    output_len: int = Form(...),
):
    params = {
        "D": D,
        "x0": x0,
        "x1": x1,
        "output_len": output_len
    }

    try:
        y_list, r_list = prodMedios(prodMParams(**params))
        result = {
            "y_list": y_list.tolist(),
            "r_list": r_list.tolist()
        }
    except nonDDigitNumber as e:
        result = {"error": str(e)}

    return result

