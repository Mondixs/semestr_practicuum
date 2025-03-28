from django.contrib import admin
from django.urls import include, path
from polls.nocodb import get_nocodb_data

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    path('nocodb-data/', get_nocodb_data, name='nocodb_data'),
]