from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import jwt



# Create your views here.

@csrf_exempt
def home(request):
    if request.method == 'GET':
        return JsonResponse({ 'message' : "You are on the home page" })
    else:
        return JsonResponse({ 'message' : "something went wrong" })



@csrf_exempt
def login(request):
    if request.method == 'POST':
        print("Call has reached")
        email = request.POST['email']
        password = request.POST['password']
        context = {
            'id' : 1,
            'email' : email,
            'password' : password
        }

        encoded_data =  {  'token' :  jwt.encode(context , "this is very complexksncjabjkvbfsk" , algorithm="HS256")  } 
        return JsonResponse(encoded_data)
    else:
        return JsonResponse({ 'error' : "something went wrong" })




@csrf_exempt
def verifytoken(request):
    if request.method == "GET":
        decodedata = jwt.decode(request.META['HTTP_AUTHORIZATION'].split()[1] , "this is very complexksncjabjkvbfsk" , algorithms="HS256")
        if decodedata['id'] == 1:
            return JsonResponse({ 'message' : "successfully decoded, User is Authenticated.." , 'payload' : decodedata  })
        else:
            return JsonResponse({ 'error' : "Authentication is failed" })
    else:
        return JsonResponse({ 'error' : "something went wrong" })



