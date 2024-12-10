from rest_framework import serializers

from .models import Master, Subsidiary, Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = '__all__'


class SubsidiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subsidiary
        fields = '__all__'
