from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from api.models import DoctorInfo


class RegisterForm(UserCreationForm[User]):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class DoctorInfoProfileForm(forms.ModelForm[DoctorInfo]):
    class Meta:
        model = DoctorInfo
        fields = [
            "name",
            "phone",
            "governorate",
            "governorate_code",
            "area",
            "area_code",
            "healthcare_ins",
            "healthcare_ins_code",
        ]
        labels = {
            "name": "اسم مقدم المشورة",
            "phone": "رقم الهاتف",
            "governorate": "المحافظة",
            "governorate_code": "كودالمحافظة",
            "area": "المنطقة/الادارة",
            "area_code": "كود الادارة",
            "healthcare_ins": "المنشاة الصحية",
            "healthcare_ins_code": "كود المنشاة",
        }
