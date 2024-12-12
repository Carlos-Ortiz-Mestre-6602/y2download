from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.utils.yt_dlp import download

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="app/templates")

@app.get('/', response_class=HTMLResponse)
def home_view(request: Request):
    return templates.TemplateResponse(
        request=request, name="home.html"
    )

@app.get('/download/', response_class=RedirectResponse)
def download_video(request: Request, url: str):
    file_path = download(url)

    return RedirectResponse(f'{request.base_url}{file_path}')


@app.get('/error_invalid_url')
def error_invalid_url(request: Request):
    return templates.TemplateResponse(
        request=request, name="error_invalid_url.html"
    )