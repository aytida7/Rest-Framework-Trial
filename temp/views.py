from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from .models import rmodel 

# Create your views here.
@api_view(['GET'])
def index(request):
    name={'name':'aditya','lname':"patil hey"}
    return Response(name)
