from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from student.serializers import StudentSerializer
from student.models import Student
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests,json
from django.shortcuts import redirect

# Create your views here.
@csrf_exempt
def addStudent(request):
    if(request.method=="POST"):
        #mydict=JSONParser().parse(request)
        s_serialize=StudentSerializer(data=request.POST)
        if(s_serialize.is_valid()):
            s_serialize.save()
            return redirect(viewingStudent)
            #return JsonResponse(s_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET method allowed",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def viewStudents(request): 
    if(request.method=="GET"):
        students=Student.objects.all()
        s_serialize=StudentSerializer(students,many=True)
        return JsonResponse(s_serialize.data,safe=False)


@csrf_exempt
def studentDetails(request,id):
    try:
        students=Student.objects.get(id=id)
    except Student.DoesNotExist:
        return HttpResponse("Invalid Student Id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        s_serialize=StudentSerializer(students)
        return JsonResponse(s_serialize.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        students.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        s_serialize=StudentSerializer(students,data=mydict)
        if(s_serialize.is_valid()):
            s_serialize.save()
            return JsonResponse(s_serialize.data,status=status.HTTP_200_OK)

def StudentAdd(request):
    return render(request,'register.html')

def viewingStudent(request):
    fetchdata=requests.get("http://127.0.0.1:8000/student/viewall/").json()
    return render(request,'view.html',{"data":fetchdata}) 

def loginData(request):
    return render(request,'login.html')


def ProfileData(request):
    return render(request,'profile.html')
def EditProfile(request):
    return render(request,'editprofile.html')

@csrf_exempt
def login_check(request):
    try:
        username=request.POST.get("username")
        password=request.POST.get("password")
        getUsers=Student.objects.filter(username=username,password=password)
        s_serialize=StudentSerializer(getUsers,many=True)
        if(s_serialize.data):
            for i in s_serialize.data:
                a=i["name"]
                b=i["id"]
                c=i["address"]
                d=i["standard"]
                e=i["phone_no"]
                f=i["username"]
                g=i["password"]
            request.session['uname']=a
            request.session['uid']=b
            request.session['uaddress']=c
            request.session['ustandard']=d
            request.session['uphone_no']=e
            request.session['uusername']=f
            request.session['upassword']=g
            return render(request,"profile.html")
        else:
            return HttpResponse("Invalid credentails")
    except Student.DoesNotExist:
        return HttpResponse("Invalid Details")



@csrf_exempt
def update_dataread(request):
    getNewId=request.POST.get("newId")
    getName=request.POST.get("newname")
    getAddress=request.POST.get("newaddress")
    getStandard=request.POST.get("newstandard")
    getPhone=request.POST.get("newphone_no")
    getUsername=request.POST.get("newusername")
    getPassword=request.POST.get("newpassword")
    mydata={"name":getName,"address":getAddress,"standard":getStandard,"phone_no":getPhone,"username":getUsername,"password":getPassword}
    jsondata=json.dumps(mydata)
    print(jsondata)
    ApiLink="http://127.0.0.1:8000/student/view/"+getNewId
    requests.put(ApiLink,data=jsondata)
    return HttpResponse("Updated successfully")