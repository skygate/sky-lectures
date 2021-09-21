import six
import json

from rest_framework import viewsets, parsers

from resources.serializers import CreateResourceSerializer
from resources.models import Resource
from resources.permissions import IsAdminOrOwner, IsAdminOrReadOnly


class MultiPartJSONParser(parsers.MultiPartParser):

    def parse(self, stream, media_type=None, parser_context=None):

        dataAndFiles = super(MultiPartJSONParser, self).parse(stream, media_type, parser_context)

        try:
            jsonData = json.loads(dataAndFiles.data.get('data'))
        except ValueError as exc:
            raise parsers.ParseError('JSON parse error - %s' % six.text_type(exc))

        # make data mutable, insert json data, and remove raw data
        dataAndFiles.data = data = dataAndFiles.data.copy()
        data.update(jsonData)
        del data['data']

        return dataAndFiles


class ResourceViewSet(viewsets.ModelViewSet):

    queryset = Resource.objects.all()
    serializer_class = CreateResourceSerializer
    permission_classes = (IsAdminOrOwner, IsAdminOrReadOnly)
    http_method_names = ("post", "get", "patch")

    def get_parsers(self):
        if self.request.method == 'POST':
            self.parser_classes = (parsers.MultiPartParser, )
        else:
            self.parser_classes = (parsers.JSONParser, )
        return [parser() for parser in self.parser_classes]

    def create(self, request, *args, **kwargs):
        from rest_framework.response import Response
        try:
            super(ResourceViewSet, self).create(request, *args, **kwargs)
        except Exception as e:
            print(e)
            return Response()
