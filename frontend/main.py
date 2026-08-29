from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='register.html'
    )

from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="static"), name="static")

# 2. Add an explicit route to deliver the register layout file
@app.get("/register", response_class=FileResponse)
def get_register_page():
    return FileResponse("templates/register.html")

# 3. Add an explicit route to deliver the login layout file
@app.get("/login", response_class=FileResponse)
def get_login_page():
    return FileResponse("templates/login.html")

# 4. Add an explicit route to deliver the dashboard matrix file
@app.get("/dashboard", response_class=FileResponse)
def get_dashboard_page():
    return FileResponse("templates/dashboard.html")

@app.get("/seller-dashboard", response_class=FileResponse)
def get_seller_page():
    return FileResponse("templates/seller_dashboard.html")

@app.get("/buyer-dashboard", response_class=FileResponse)
def get_buyer_page():
    return FileResponse("templates/buyer_dashboard.html")
# 