from django.contrib.auth import authenticate
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render
from rest_framework import viewsets,status,generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import UserModel,HouseModel,SessionToken,ImageModel,AddBookmark
from .serializers import UserSerializer,LoginSerializer,HouseSerializer,ImageSerializer,AddToBookmarkSerializer
from datetime import timedelta
from django.utils import timezone

# Create your views here.
#Signup method

@api_view(['POST','OPTIONS'])

def signup_view(request):
    if request.method=="POST":
        user=UserModel.objects.create()
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user.save()
            token=SessionToken(user=user)
            token.create_token()
            token.save()
            res=token.session_token
            response = Response(res,status=status.HTTP_201_CREATED)
            return response
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#Login Api
@api_view(['POST'])
def login_view(request):
    if request.method=="POST":
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            email=request.data.get('email')
            password=request.data.get('password')
            user=UserModel.objects.filter(email=email).first()
            print(user.email)
            print(user.password)
            if str(password)==str(user.password):
                serializer.save()
                token=SessionToken(user=user)
                token.create_token()
                token.save()
                res={
                    'session_token':token.session_token    
                }
                response=Response(res,status=status.HTTP_201_CREATED)
                return response
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
  
#Post house details
@api_view(['POST']) 
def house_view(request):
        if request.method=="POST":
            houseobj=HouseModel.objects.create()
            serializer=HouseSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                houseobj.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
                         
#Get house objects
@api_view(['GET'])
def house_details_view(request):
           if request.method=="GET": 
                    house=HouseModel.objects.all()
                    print(house)
                    serializer=HouseSerializer(house,many=True)
                    response=Response(serializer.data,status=status.HTTP_201_CREATED)
                    return response
                    
@api_view(['GET','POST'])
def image_view(request):
    image=ImageModel.objects.create()
    if request.method=='POST':
        serializer=ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    if request.method=='GET':
        img=ImageModel.objects.all()
        serializer=ImageSerializer(img,many=True)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET'])
def your_post_view(request):
    email=request.GET.get('email', '')
    print(email)
    if request.method=='GET':
        houseobj=HouseModel.objects.all().filter(posted_by=email)
        serializer=HouseSerializer(houseobj,many=True)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
@api_view(['DELETE'])
def post_delete_view(request):
    id=request.data.get('id')
    houseobj=HouseModel.objects.get(id=id)
    if request.method=='DELETE':
        serializer=HouseSerializer
        houseobj.delete()
        return Response(status=status.HTTP_200_OK)
    

@api_view(['POST'])
def post_bookmark(request):    
    if request.method=='POST': 
        user_email=request.data.get('user_email')
        house_id=request.data.get('house_id')
        add_to_bookmark=request.data.get('add_to_bookmark') 
        bookmark=AddBookmark(user_email=user_email,house_id=house_id,add_to_bookmark=add_to_bookmark)
        serializer=AddToBookmarkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            bookmark.save()
            print(bookmark.user_email)
            print(bookmark.house_id)
            print(serializer)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE'])
def get_bookmarks(request):
    user_email=request.GET.get('user_email', '')
    house_id=request.GET.get('house_id', '')
    #print(request.GET.get('user_email', ''))
    if request.method=='GET':
       bookmarkobj=AddBookmark.objects.all().filter(user_email=user_email,house_id=house_id)
       serializer=AddToBookmarkSerializer(bookmarkobj,many=True)
       return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method=='DELETE':
        id=request.data.get('id')
        bookmarkobj=AddBookmark.objects.get(id=id)
        bookmarkobj.delete()
        return Response(status=status.HTTP_200_OK)






        



        



