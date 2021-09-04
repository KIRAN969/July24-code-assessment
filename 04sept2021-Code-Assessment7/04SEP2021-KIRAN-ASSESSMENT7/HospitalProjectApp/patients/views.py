from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from patients.serializers import PatientSerializer
from patients.models import Patient
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests,json
from django.shortcuts import redirect
# Create your views here.
@csrf_exempt
def addPatient(request):
    if(request.method=="POST"):
        #mydict=JSONParser().parse(request)
        p_serialize=PatientSerializer(data=request.POST)
        if(p_serialize.is_valid()):
            p_serialize.save()
            return redirect(viewingPatients)
            #return JsonResponse(p_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET method allowed",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def viewPatients(request):
    if(request.method=="GET"):
        patients=Patient.objects.all()
        p_serialize=PatientSerializer(patients,many=True)
        return JsonResponse(p_serialize.data,safe=False)

@csrf_exempt
def patientDetails(request,id):
    try:
        patients=Patient.objects.get(id=id)
    except Patient.DoesNotExist:
        return HttpResponse("Invalid Patient Id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        p_serialize=PatientSerializer(patients)
        return JsonResponse(p_serialize.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        patients.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        p_serialize=PatientSerializer(patients,data=mydict)
        if(p_serialize.is_valid()):
            p_serialize.save()
            return JsonResponse(p_serialize.data,status=status.HTTP_200_OK)


def patientAdd(request):
    return render(request,'register.html')

def viewingPatients(request):
    fetchdata=requests.get("http://127.0.0.1:8000/patients/viewall/").json()
    return render(request,'view.html',{"data":fetchdata})

def patientSearch(request):
    return render(request,'search.html')

def patientUpdate(request):
    return render(request,'update.html')

def patientDelete(request):
    return render(request,'delete.html')


@csrf_exempt
def searchapi(request):
    try:
        getPatientCode=request.POST.get("p_code")
        getPatient=Patient.objects.get(p_code=getPatientCode)
        p_serialize=PatientSerializer(getPatient)
        return render(request,"search.html",{"data":p_serialize.data})
        #return JsonResponse(p_serialize.data,safe=False)
    except:
        return HttpResponse("Invalid Patient Code")



@csrf_exempt
def update_searchapi(request):
    try:
        getPatientCode=request.POST.get("p_code")
        getPatient=Patient.objects.get(p_code=getPatientCode)
        p_serialize=PatientSerializer(getPatient)
        return render(request,"update.html",{"data":p_serialize.data})
        #return JsonResponse(p_serialize.data,safe=False)
    except:
        return HttpResponse("Invalid Patient Code")
  

@csrf_exempt
def update_data_read(request):
    getNewId=request.POST.get("newId")
    getPCode=request.POST.get("newp_code")
    getName=request.POST.get("newname")
    getAddress=request.POST.get("newaddress")
    getEmailId=request.POST.get("newmail")
    getPhone=request.POST.get("newphone_no")
    getPincode=request.POST.get("newpincode")
    mydata={"p_code":getPCode,"name":getName,"address":getAddress,"mail":getEmailId,"phone_no":getPhone,"pincode":getPincode}
    jsondata=json.dumps(mydata)
    print(jsondata)
    ApiLink="http://127.0.0.1:8000/patients/view/"+getNewId
    requests.put(ApiLink,data=jsondata)
    return HttpResponse("Updated successfully")


@csrf_exempt
def delete_searchapi(request):
    try:
        getPatientCode=request.POST.get("p_code")
        getPatient=Patient.objects.get(p_code=getPatientCode)
        p_serialize=PatientSerializer(getPatient)
        return render(request,"delete.html",{"data":p_serialize.data})
        #return JsonResponse(p_serialize.data,safe=False)
    except:
        return HttpResponse("Invalid Patient Code")

@csrf_exempt
def delete_data_read(request):
    getNewId=request.POST.get("newId")
    ApiLink="http://127.0.0.1:8000/patients/view/"+getNewId
    requests.delete(ApiLink)
    return HttpResponse("Deleted successfully")


@csrf_exempt
def login_check(request):
    try:
        username=request.POST.get("username")
        password=request.POST.get("password")
        getUsers=Patient.objects.filter(username=username,password=password)
        patient_serialize=PatientSerializer(getUsers,many=True)
        if(patient_serialize.data):
            for i in patient_serialize.data:
                x=i["name"]
                y=i["id"]
            request.session['uname']=x
            request.session['uid']=y
            return render(request,"Welcome.html")
        else:
            return HttpResponse("Invalid credentails")
    except Patient.DoesNotExist:
        return HttpResponse("Invalid Details")


def loginData(request):
    return render(request,'log.html')
   