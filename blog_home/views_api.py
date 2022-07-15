from tabnanny import check
from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

#API for user login using Django rest Framework
class Login_user(APIView):
    
    def post(self, request):
        response =  {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data 
            if data.get('username') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')
            
            if data.get('password') is None:
                response['message'] = 'key password not found'
                raise Exception('key password not found')
            #check if username exists or not
            check_user  = User.objects.filter(username=data.get('username')).first()
            if check_user is None:
                response['message'] = 'Invalid user, User not found'
                raise Exception('Invalid user, User not found')
            #authenticate password and return response
            user_obj = authenticate(username = data.get('username'), password = data.get('password'))
            if user_obj:
                login(request, user_obj)
                response['status'] = 200
                response['message'] = 'WELCOME!'
            else:
                response['message'] = 'Invalid password, Try again'
                raise Exception('Invalid password')
        except Exception as e:
            print(e)
        return Response(response)

loginUser = Login_user.as_view()

#For SignUp , New user
class Register_user(APIView):
    
    def post(self, request):
        response =  {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data 
            if data.get('username') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')
            
            if data.get('password') is None:
                response['message'] = 'key password not found'
                raise Exception('key password not found')
            #check if username already exists 
            check_user  = User.objects.filter(username=data.get('username')).first()
            if check_user:
                response['message'] = 'Username already taken, Try another'
                raise Exception('Username already taken, Try another')
            #Create password and return response
            user_obj = User.objects.create(username = data.get('username'))
            user_obj.set_password(data.get('password'))
            user_obj.save()
            response['status'] = 200
            response['message'] = 'User Created Successfully!'
        except Exception as e:
            print(e)
        return Response(response)
registerUser = Register_user.as_view()
