from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Cloud Laboratory - Exercise no.1")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/", response_class=HTMLResponse)
async def root_post(request: Request, num: str = Form()):
    num = int(num)
    if num < 1 or num > 20:
        return templates.TemplateResponse("index.html", {"request": request, "error":
                                                                             "Value less than 1 or more than 20"})

    result: int = fibonacci(num)

    return templates.TemplateResponse("index.html", {"request": request, "num": num, "result": result})


def fibonacci(n: int) -> int:
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


