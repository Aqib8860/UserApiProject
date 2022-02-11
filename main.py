from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
import uvicorn
from server.urls import urlpatterns


middleware=[
    Middleware(CORSMiddleware, allow_origins=['*'])
]

app = Starlette(routes=urlpatterns, middleware=middleware)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", debug=True)

