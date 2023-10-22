from fastapi import FastAPI, Form
from congruent_lehmer import congruentLehmer, lehmerParams, NonPrimeRelativesNumbers
from congruent_mult import congruentMult, multParams, NonOddSeedError
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from cuadrados_medios import cuadMedios, cuadParams, nonDigitos
from productos_medios import prodMedios, prodMParams, nonDDigitNumber
from mult_constantes import multConstante, algoritmoMultConstante, nonDigitos
from congruent_adit import secuenciaX, congruentAditivo, nonDigitos
from congru_no_lineal_cuad import noLinealCuad, algorit_no_lineal_cuad, NonConditionError

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




@app.post("/cuadM")
async def procesar_datos(
    d: int = Form(...),
    x0: int = Form(...),
    output_len: int = Form(...),
):
    params = {
        "d": d,
        "x0": x0,
        "output_len": output_len,
    }

    try:
        y_list, r_list = cuadMedios(cuadParams(**params))
        
        result = {
            "y_list": y_list,
            "r_list": r_list
        }

    except nonDigitos as e:
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
            "y_list": y_list,
            "r_list": r_list
        }

    except nonDDigitNumber as e:
        result = {"error": str(e)}

    return result

@app.post("/multCons")
async def procesar_datos(
    d: int = Form(...),
    x0: int = Form(...),
    a: int = Form(...),
    output_len: int = Form(...),
):
    params = {
        "d": d,
        "x0": x0,
        "a": a,
        "output_len": output_len,
    }

    try:
        y_list, r_list = multConstante(cuadParams(**params))
        
        result = {
            "y_list": y_list,
            "r_list": r_list
        }

    except nonDigitos as e:
        result = {"error": str(e)}

    return result

@app.post("/congAdit")
async def procesar_datos(
    n: int = Form(...),
    x_values: int = Form(...),
    m: int = Form(...),
    output_len: int = Form(...)
):
    params = {
        "n": n,
        "x_values": x_values,
        "m": m,
        "output_len": output_len
    }

    try:
        x_list, r_list = secuenciaX(multParams(**params))
        result = {
            "x_list": x_list.tolist(),
            "r_list": r_list.tolist()
        }
    except NonOddSeedError as e:
        result = {"error": str(e)}

    return result


@app.post("/noLineal")
async def procesar_datos(
    x0: int = Form(...),
    a: int = Form(...),
    b: int = Form(...),
    c: int = Form(...),
    g: int = Form(...)
):
    params = {
        "x0": x0,
        "a": a,
        "b": b,
        "c": c,
        "g": g
    }

    try:
        x_list, r_list = noLinealCuad(multParams(**params))
        result = {
            "x_list": x_list.tolist(),
            "r_list": r_list.tolist()
        }
    except NonConditionError as e:
        result = {"error": str(e)}

    return result