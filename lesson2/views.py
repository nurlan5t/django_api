from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from lesson2.models import CarBrand, Car
from lesson2.serializers import CarBrandListSerializer, CarListSerializer, CarWithBrandSerializer


@api_view(['GET'])
def car_brand_list_view(request):
    car_brands = CarBrand.objects.all()
    data = CarBrandListSerializer(car_brands, many=True).data
    return Response(data=data)

@api_view(['GET'])
def car_list_view(request):
    cars = Car.objects.all()
    return Response(data=CarWithBrandSerializer(cars, many=True).data)

