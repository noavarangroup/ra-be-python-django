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

    def validate(self, data):
        parent = data.get('parent')
        master = data.get('master')
        if parent:
            if parent.master!= master:
                raise serializers.ValidationError('The master of the Subsidiary and its parent must be the same.')
        return data
