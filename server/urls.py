from starlette.routing import Route
from .views import page_not_found
from users.urls import user_urlpatterns


urlpatterns=[
    Route('/', page_not_found, methods=["GET","POST"]),
]

urlpatterns.extend(user_urlpatterns)
