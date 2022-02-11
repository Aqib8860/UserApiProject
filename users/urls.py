from starlette.routing import Route
from users import views

user_urlpatterns=[
    Route('/api/users', views.getUsers , methods=["GET","POST"]),
    Route('/api/users/{user_id:int}', views.getUser , methods=["GET","PUT","DELETE"]),
    #Route('/api/users/', views.getUser , methods=["GET","PUT","DELETE"]),
]
