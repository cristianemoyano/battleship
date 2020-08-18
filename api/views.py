from rest_framework import viewsets
from rest_framework.response import Response

class HelloView(viewsets.ViewSet):
    '''Test API Viewset'''

    def list(self, request):
        '''Return Hello Message'''
        return Response({'message': 'Hello'})

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass