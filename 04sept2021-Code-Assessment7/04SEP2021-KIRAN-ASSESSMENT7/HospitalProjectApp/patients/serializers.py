from rest_framework import serializers
from patients.models import Patient
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields=('id','p_code','name','address','mail','phone_no','pincode','username','password')