from rest_framework import serializers
from doctors.models import Doctor
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields=('id','d_code','name','address','specilization','phone_no','mail','username','password')