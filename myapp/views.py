from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import jwt



# Create your views here.
@csrf_exempt
def home(request):
    if request.method == 'GET':
        print("got request in backend ==>")
        context = {
            'id' : 145789
        }

        encoded_data =  {  'token' :  jwt.encode(context , "this is very complexksncjabjkvbfsk" , algorithm="HS256")  } 
        return JsonResponse(encoded_data)
    else:
        return JsonResponse({ 'error' : "something went wrong" })



@csrf_exempt
def decodedata(request):
    if request.method == "POST":
        print("In decodedata")
        print("==========> Header" , request.META['HTTP_AUTHORIZATION'].split()[1])
        decodedata = jwt.decode(request.META['HTTP_AUTHORIZATION'].split()[1] , "this is very complexksncjabjkvbfsk" , algorithms="HS256")
        return JsonResponse(decodedata)
    else:
        return JsonResponse({ 'error' : "something went wrong" })



