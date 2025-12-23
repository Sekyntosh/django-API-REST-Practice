from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

from rest_framework import generics, serializers


from .models import Autor

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = [
			'name',
			'surname',
			'nationality',
		]


class ListAutors(generics.ListAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer