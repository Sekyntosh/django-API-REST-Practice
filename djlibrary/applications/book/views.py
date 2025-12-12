from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def hello(request):
	print("mi primera url")
	return JsonResponse({'saludo':  'hola'})    