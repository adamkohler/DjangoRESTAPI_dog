from rest_framework import serializers
from dogs.models import Dog
from dogs.models import Breed


class DogSerializer(serializers.HyperlinkedModelSerializer):
    breed = serializers.SlugRelatedField(queryset=Breed.objects.all(), slug_field='name')
    #dog = serializers.SlugRelatedField(queryset=Dog.objects.all(), slug_field='name')
    class Meta:
        model = Dog
        fields = (
            #'url',
            'id',
            'name',
            'age',
            'breed',
            'gender',
            'color',
            'favoritefood',
            'favoritetoy',)

class BreedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Breed
        fields = (
            #'url',
            'id',
            'name',
            'size',
            'friendliness',
            'trainability',
            'sheddingamount',
            'exerciseneeds',)