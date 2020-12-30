# importing the modules required
from django.contrib import admin
from django.urls import path,include

# project url patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/",include("api.urls"))
]
