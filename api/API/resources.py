from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from api.API import serializers
from page import models


class PageView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = models.Page.objects.all()
    serializer_class = serializers.PageSerializer

    @action(methods=["get"], detail=False, url_path="(?P<label>.+)")
    def pages(self, request, *args, **kwargs):
        label = kwargs["label"]
        objects = models.Page.objects.filter(label=label)
        serializer = self.get_serializer(objects, many=True)
        return Response(status=200, data=serializer.data)