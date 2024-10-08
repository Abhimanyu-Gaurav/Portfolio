from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

# Create an instance of the FastAPI class
app = FastAPI()

# Set up the template directory for Jinja2
templates = Jinja2Templates(directory="templates")

# Define the route for the root URL ("/")
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Render the index.html template and pass the request object
    return templates.TemplateResponse("index.html", {"request": request})
