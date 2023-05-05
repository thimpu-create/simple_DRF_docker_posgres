from django.shortcuts import render
from rest_framework.views import APIView
from api.models import Book
from api.serializers import BookSerializer
from rest_framework.response import Response

class Home(APIView):
    def get(self,request):
        books = Book.objects.all()
        serializer = BookSerializer(books,many = True)
        return Response(serializer.data)
    
    def post(self,request):
        datas = request.data
        serializer = BookSerializer(data=datas)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)




