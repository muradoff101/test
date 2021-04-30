from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path("", MainPageView.as_view(), name="main_page_link"),
    path("api/v1/load_csv/", UploadCSVFilesView.as_view()),
    path("api/v1/customers/", CustomersView.as_view())
]
