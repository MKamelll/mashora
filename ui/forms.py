from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from typing import Any
from api.models import MashoraDoctor


class RegisterForm(UserCreationForm[User]):

    def clean_username(self) -> str:
        username = self.cleaned_data.get("username")
        if not username:
            raise forms.ValidationError("هذا الحقل مطلوب")
        if MashoraDoctor.objects.filter(username=username).exists():
            raise forms.ValidationError("اسم المستخدم غير متاح")
        return str(username)

    def clean_password2(self) -> str:
        password2 = self.cleaned_data.get("password2")
        password1 = self.cleaned_data.get("password1")
        if not password2 or not password1:
            raise forms.ValidationError("هذا الحقل مطلوب")
        if password1 != password2:
            raise forms.ValidationError("كلمتا السر غير متطابقتين")
        return str(password2)

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class MashoraDoctorProfileForm(forms.ModelForm[MashoraDoctor]):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["required"] = False

    def clean_healthcare_ins_code(self) -> str:
        healthcare_ins_code = self.cleaned_data.get("healthcare_ins_code")
        if not healthcare_ins_code:
            return ""
        for i in healthcare_ins_code:
            if not i.isdigit():
                raise forms.ValidationError("كود المنشاة الصحية يجب ان يكون ارقام فقط")
        if len(healthcare_ins_code) > 50:
            raise forms.ValidationError("كود المنشاة الصحية يجب ألا يتجاوز 50 رقم")

        return str(healthcare_ins_code)

    def clean_healthcare_ins(self) -> str:
        healthcare_ins = self.cleaned_data.get("healthcare_ins")
        if not healthcare_ins:
            raise forms.ValidationError("هذا الحقل مطلوب")
        for i in healthcare_ins:
            if i.isdigit():
                raise forms.ValidationError(
                    "اسم المنشاة الصحية لا يمكن أن يحتوي علي أرقام"
                )
        if len(healthcare_ins) > 150:
            raise forms.ValidationError("اسم المنشاة الصحية لا يمكن ان يتجاوز 150 حرف")
        return str(healthcare_ins)

    def clean_area_code(self) -> str:
        area_code = self.cleaned_data.get("area_code")
        if not area_code:
            return ""
        for i in area_code:
            if not i.isdigit():
                raise forms.ValidationError("كود المنطقة يجب ان يكون ارقام فقط")
        if len(area_code) > 50:
            raise forms.ValidationError("كود المنطقة يجب ألا يتجاوز 50 رقم")

        return str(area_code)

    def clean_area(self) -> str:
        area = self.cleaned_data.get("area")
        if not area:
            raise forms.ValidationError("هذا الحقل مطلوب")
        for i in area:
            if i.isdigit():
                raise forms.ValidationError("اسم المنطقة لا يمكن أن يحتوي علي أرقام")
        if len(area) > 150:
            raise forms.ValidationError("اسم المنطقة لا يمكن ان يتجاوز 150 حرف")

        return str(area)

    def clean_governorate_code(self) -> str:
        governorate_code = self.cleaned_data.get("governorate_code")
        if not governorate_code:
            return ""
        for i in governorate_code:
            if not i.isdigit():
                raise forms.ValidationError("كود المحافظة يجب ان يكون ارقام فقط")
        if len(governorate_code) > 50:
            raise forms.ValidationError("كود المحافظة يجب ألا يتجاوز 50 رقم")

        return str(governorate_code)

    def clean_governorate(self) -> str:
        governorate = self.cleaned_data.get("governorate")
        if not governorate:
            raise forms.ValidationError("هذا الحقل مطلوب")
        for i in governorate:
            if i.isdigit():
                raise forms.ValidationError("اسم المحافظة لا يمكن أن يحتوي علي أرقام")
        if len(governorate) > 50:
            raise forms.ValidationError("اسم المحافظة لا يمكن ان يتجاوز 50 حرف")
        return str(governorate)

    def clean_name(self) -> str:
        name = self.cleaned_data.get("name")
        if not name:
            raise forms.ValidationError("هذا الحقل مطلوب")
        for i in name:
            if i.isdigit():
                raise forms.ValidationError("هذا الحقل لايمكن أن بحتوي علي أرقام")
        name_separated = name.split()
        if len(name_separated) < 3:
            raise forms.ValidationError(
                "الاسم يجب أن يكون ثلاثي علي الاقل والفاصل مسافة"
            )
        return str(name)

    def clean_phone(self) -> str:
        phone = self.cleaned_data.get("phone")
        if not phone:
            raise forms.ValidationError("هذا الحقل مطلوب")
        if not phone.isdigit():
            raise forms.ValidationError("رقم الهاتف يجب ان يحتوي علي ارقام فقط")
        if len(phone) != 11:
            raise forms.ValidationError("رقم الهاتف يجب ان يكون 11 رقم")
        return str(phone)

    class Meta:
        model = MashoraDoctor
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
