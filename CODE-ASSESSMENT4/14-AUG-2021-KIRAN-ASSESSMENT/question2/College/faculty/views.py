from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def addfaculty(request):
        if(request.method=='POST'):
            name=request.POST.get("name")
            addr=request.POST.get("address")
            dept=request.POST.get("department")
            college=request.POST.get("college")
            dict={"name":name,"address":addr,"department":dept,"college":college}
            result=json.dumps(dict)
            return HttpResponse(result)
        else:
            return HttpResponse("GET method")