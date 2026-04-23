from django import forms
from .models import DoctorInfo


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
