from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from books.serializers import BookSerializer
from books.models import Book
from rest_framework.parsers import JSONParser
from rest_framework import status
# Create your views here.
@csrf_exempt
def addBook(request):
    if(request.method=="POST"):
        mydict=JSONParser().parse(request)
        book_serialize=BookSerializer(data=mydict)
        if(book_serialize.is_valid()):
            book_serialize.save()
            return JsonResponse(book_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET method allowed",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def viewBooks(request):
    if(request.method=="GET"):
        book=Book.objects.all()
        book_serialize=BookSerializer(book,many=True)
        return JsonResponse(book_serialize.data,safe=False)



@csrf_exempt
def bookDetails(request,id):
    try:
        book=Book.objects.get(id=id)
    except Book.DoesNotExist:
        return HttpResponse("Invalid Book Id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        book_serialize=BookSerializer(book)
        return JsonResponse(book_serialize.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        book.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        book_serialize=BookSerializer(book,data=mydict)
        if(book_serialize.is_valid()):
            book_serialize.save()
        return JsonResponse(book_serialize.data,status=status.HTTP_200_OK)

@csrf_exempt
def singlebook(request,book):
    try:
        book=Book.objects.get(bookname=book)
    except Book.DoesNotExist:
        return HttpResponse("Invalid Book name",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        book_serialize=BookSerializer(book)
        return JsonResponse(book_serialize.data,safe=False,status=status.HTTP_200_OK)

def BookPage(request):
    return render(request,'book.html')