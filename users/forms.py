from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import MashoraDoctor

class RegisterForm(UserCreationForm[MashoraDoctor]):
    username = forms.CharField(label="اسم المستخدم", max_length=150, required=True, error_messages={
        "required": "هذا الحقل مطلوب",
        "max_length": "اقصي عدد من الحروف هو 150",
        "unique": "اسم المستخدم موجود بالفعل"
    })
    password1 = forms.CharField(label="كلمة المرور", max_length=150, required=True, error_messages={
        "required": "كلمة السر مطلوبة"
    })
    password2 = forms.CharField(label="تاكيد كلمة المرور", max_length=150, required=True, error_messages={
        "required": "اعد كتابة كلمة السر مرة اخري",
        "password_mismatch": "كلمة السر غير متطابقة"
    })
    name = forms.CharField(label="اسم مقدم المشورة", max_length=100, required=True)
    phone = forms.CharField(label="رقم الهاتف", max_length=100, required=True)
    governorate = forms.CharField(label="المحافظة", max_length=100, required=True)
    governorate_code = forms.CharField(label="كود المحافظة", max_length=100, required=False)
    area = forms.CharField(label="المنطقة/الادارة", max_length=100, required=True)
    area_code = forms.CharField(label="كود الادارة", max_length=100, required=False)
    healthcare_ins = forms.CharField(label="المنشاة الصحية", max_length=100, required=True)
    healthcare_ins_code = forms.CharField(label="كود المنشاة", max_length=100, required=False)
    class Meta:
        model = MashoraDoctor
        fields = ["username", "password1", "password2", "name", "phone",
                  "governorate", "governorate_code", "area", "area_code",
                  "healthcare_ins", "healthcare_ins_code"]



