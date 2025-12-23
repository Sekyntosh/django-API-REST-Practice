from django.urls import path

from .views import ListAutors

app_name = "book_apps"

urlpatterns = [
	path('autor',ListAutors.as_view(), name='list-autor')
]