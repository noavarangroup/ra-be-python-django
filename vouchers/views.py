from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

import pandas as pd

from .models import Master, Subsidiary, Person
from .serializers import MasterSerializer, SubsidiarySerializer, PersonSerializer


# Create your views here.

class SoftDeleteMixin:
    """This is for soft delete """

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = [DjangoFilterBackend]


class MasterViewSet(SoftDeleteMixin, ModelViewSet):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['code', 'title']

    @action(detail=False, methods=['get'])
    def export(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        data = MasterSerializer(queryset, many=True).data
        df = pd.DataFrame(data)
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=masters.xlsx'
        df.to_excel(response, index=False)
        return response


class SubsidiaryViewSet(SoftDeleteMixin, ModelViewSet):
    queryset = Subsidiary.objects.all()
    serializer_class = SubsidiarySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['code', 'title']

    @action(detail=False, methods=['get'])
    def export(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        data = MasterSerializer(queryset, many=True).data
        df = pd.DataFrame(data)
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=masters.xlsx'
        df.to_excel(response, index=False)
        return response