from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from doctors.serializers import DoctorSerializer
from doctors.models import Doctor
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests,json
from django.shortcuts import redirect
# Create your views here.
@csrf_exempt
def addDoctor(request):
    if(request.method=="POST"):
        #mydict=JSONParser().parse(request)
        d_serialize=DoctorSerializer(data=request.POST)
        if(d_serialize.is_valid()):
            d_serialize.save()
            return redirect(viewingDoctors)
            #return JsonResponse(d_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET method allowed",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def viewDoctors(request):
    if(request.method=="GET"):
        doctors=Doctor.objects.all()
        d_serialize=DoctorSerializer(doctors,many=True)
        return JsonResponse(d_serialize.data,safe=False)

@csrf_exempt
def doctorDetails(request,id):
    try:
        doctors=Doctor.objects.get(id=id)
    except Doctor.DoesNotExist:
        return HttpResponse("Invalid Doctor Id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        d_serialize=DoctorSerializer(doctors)
        return JsonResponse(d_serialize.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        doctors.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        d_serialize=DoctorSerializer(doctors,data=mydict)
        if(d_serialize.is_valid()):
            d_serialize.save()
            return JsonResponse(d_serialize.data,status=status.HTTP_200_OK)

def doctorAdd(request):
    return render(request,'init.html')

def viewingDoctors(request):
    fetchdata=requests.get("http://127.0.0.1:8000/doctors/viewall/").json()
    return render(request,'viewall.html',{"data":fetchdata})

def searchDoctor(request):
    return render(request,'searc.html')

def updateDoctor(request):
    return render(request,'updat.html')

def deleteDoctor(request):
    return render(request,'delet.html')

def loginData(request):
    return render(request,'login.html')


@csrf_exempt
def searchapi(request):
    try:
        getDoctorCode=request.POST.get("d_code")
        getDoctor=Doctor.objects.get(d_code=getDoctorCode)
        d_serialize=DoctorSerializer(getDoctor)
        return render(request,"searc.html",{"data":d_serialize.data})
        #return JsonResponse(d_serialize.data,safe=False)
    except:
        return HttpResponse("Invalid Doctor Code")

@csrf_exempt
def update_api(request):
    try:
        getDoctorCode=request.POST.get("d_code")
        getDoctor=Doctor.objects.get(d_code=getDoctorCode)
        d_serialize=DoctorSerializer(getDoctor)
        return render(request,"updat.html",{"data":d_serialize.data})
        #return JsonResponse(d_serialize.data,safe=False)
    except:
        return HttpResponse("Invalid Doctor Code")

@csrf_exempt
def update_dataread(request):
    getNewId=request.POST.get("newId")
    getDCode=request.POST.get("newd_code")
    getName=request.POST.get("newname")
    getAddress=request.POST.get("newaddress")
    getSpecialisation=request.POST.get("newspecilization")
    getPhone=request.POST.get("newphone_no")
    getMail=request.POST.get("newmail")
    mydata={"d_code":getDCode,"name":getName,"address":getAddress,"specilization":getSpecialisation,"phone_no":getPhone,"mail":getMail}
    jsondata=json.dumps(mydata)
    print(jsondata)
    ApiLink="http://127.0.0.1:8000/doctors/view/"+getNewId
    requests.put(ApiLink,data=jsondata)
    return HttpResponse("Updated successfully")


@csrf_exempt
def delete_api(request):
    try:
        getDoctorCode=request.POST.get("d_code")
        getDoctor=Doctor.objects.get(d_code=getDoctorCode)
        d_serialize=DoctorSerializer(getDoctor)
        return render(request,"delet.html",{"data":d_serialize.data})
        #return JsonResponse(d_serialize.data,safe=False)
    except:
        return HttpResponse("Invalid Doctor Code")


@csrf_exempt
def delete_dataread(request):
    getNewId=request.POST.get("newId")
    ApiLink="http://127.0.0.1:8000/doctors/view/"+getNewId
    requests.delete(ApiLink)
    return HttpResponse("Deleted successfully")




@csrf_exempt
def login_check(request):
    try:
        username=request.POST.get("username")
        password=request.POST.get("password")
        getUsers=Doctor.objects.filter(username=username,password=password)
        doctor_serialize=DoctorSerializer(getUsers,many=True)
        if(doctor_serialize.data):
            for i in doctor_serialize.data:
                x=i["name"]
                y=i["id"]
            request.session['uname']=x
            request.session['uid']=y
            return render(request,"Welcome.html")
        else:
            return HttpResponse("Invalid credentails")
    except Doctor.DoesNotExist:
        return HttpResponse("Invalid Details")
   