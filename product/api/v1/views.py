from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


data = {
    'id': 1,
    'title': 'Nima'
}

@api_view()
def api_list_view(request):
    return Response('ok')


@api_view()
def api_detail_view(request, id):
    return Response(data)