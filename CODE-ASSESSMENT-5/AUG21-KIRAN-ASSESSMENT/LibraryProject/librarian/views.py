from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from librarian.serializers import LibrarianSerializer
from librarian.models import Librarian
from rest_framework.parsers import JSONParser
from rest_framework import status
# Create your views here.
@csrf_exempt
def addLibrarian(request):
    if(request.method=="POST"):
        mydict=JSONParser().parse(request)
        lib_serialize=LibrarianSerializer(data=mydict)
        if(lib_serialize.is_valid()):
            lib_serialize.save()
            return JsonResponse(lib_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET method allowed",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def viewLibrarian(request):
    if(request.method=="GET"):
        lib=Librarian.objects.all()
        lib_serialize=LibrarianSerializer(lib,many=True)
        return JsonResponse(lib_serialize.data,safe=False)

@csrf_exempt
def librarianDetails(request,id):
    try:
        lib=Librarian.objects.get(id=id)
    except Librarian.DoesNotExist:
        return HttpResponse("Invalid Librarian Id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        lib_serialize=LibrarianSerializer(lib)
        return JsonResponse(lib_serialize.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        lib.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        lib_serialize=LibrarianSerializer(lib,data=mydict)
        if(lib_serialize.is_valid()):
            lib_serialize.save()
        return JsonResponse(lib_serialize.data,status=status.HTTP_200_OK)

@csrf_exempt
def singleLibrarian(request,ecode):
    try:
        lib=Librarian.objects.get(enroll_code=ecode)
    except Librarian.DoesNotExist:
        return HttpResponse("Invalid Librarian enroll_code",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        lib_serialize=LibrarianSerializer(lib)
        return JsonResponse(lib_serialize.data,safe=False,status=status.HTTP_200_OK)

def LibrarianPage(request):
    return render(request,'register.html')

def Librarianlogin(request):
    return render(request,'login.html')