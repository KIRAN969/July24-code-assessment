from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def addstudent(request):
        if(request.method=='POST'):
            name=request.POST.get("name")
            admno=request.POST.get("admno")
            rollno=request.POST.get("rollno")
            college=request.POST.get("college")
            parentname=request.POST.get("parentname")
            dict={"name":name,"admno":admno,"rollno":rollno,"college":college,"parentname":parentname}
            result=json.dumps(dict)
            return HttpResponse(result)
        else:
            return HttpResponse("GET method")
