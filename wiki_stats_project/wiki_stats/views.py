from django.http import JsonResponse
from django.shortcuts import render

# create a function based view in wiki_stats/views (use api_view from django rest framework : https://www.django-rest-framework.org/api-guide/views/#api_view)
# input request.GET.get('title') and return results of service in previous steps

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import fetch_summary, interpret_summary


@api_view(['GET'])
def get(request):
    title = request.GET.get('title')
    summary = fetch_summary(title)
    interpret_summary(summary)
    return Response({'summary': interpret_summary(summary)})