from rest_framework import serializers

from lesson2.models import CarBrand, Car


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class CarBrandListSerializer(serializers.ModelSerializer):
    cars = CarListSerializer(many=True)

    class Meta:
        model = CarBrand
        fields = 'id name country cars'.split()

class CarBrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarBrand
        fields = 'id name country'.split()

class CarWithBrandSerializer(serializers.ModelSerializer):
    # brand = CarBrandSerializer()
    brand = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = 'id model brand'.split()

    def get_brand(self, obj):
        return obj.brand.name