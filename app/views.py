from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import datetime

# Create your views here.

@api_view(['GET'])
def get_date(request):
    date = datetime.datetime.now()
    return Response({'status': 200 , 'date' : date})

