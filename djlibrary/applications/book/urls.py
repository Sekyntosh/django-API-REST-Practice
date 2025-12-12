from django.urls import path

from .views import hello

app_name = "book_apps"

urlpatterns = [
	path('hello', hello)
]