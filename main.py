from fastapi import FastAPI, __version__
from congruential_lehmer import congruential, congruentialParam, NonPrimeRelativesNumbers
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

html = f"""
<!DOCTYPE html>
<html>
    <head>
        <title>FastAPI on Vercel</title>
        <link rel="icon" href="/static/favicon.ico" type="image/x-icon" />
    </head>
    <body>
        <div class="bg-gray-200 p-4 rounded-lg shadow-lg">
            <h1>Hello from FastAPI@{__version__}</h1>
            <ul>
                <li><a href="/docs">/docs</a></li>
                <li><a href="/redoc">/redoc</a></li>
            </ul>
            <p>Powered by <a href="https://vercel.com" target="_blank">Vercel</a></p>
        </div>
    </body>
</html>
"""

@app.get("/")
async def root():
    return HTMLResponse(html)
  
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