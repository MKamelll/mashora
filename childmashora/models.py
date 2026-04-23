from django.db import models
from doctors.models import DoctorInfo

# Create your models here.


class ChildInfo(models.Model):
    class Delivery(models.TextChoices):
        C_SECTION = "C_SECTION", "قيصري"
        NATURAL = "NATURAL", "طبيعي"

    class DeliveryLocation(models.TextChoices):
        HOME = "HOME", "المنزل"
        HOSPITAL = "HOSPITAL", "المستشفي"

    class HospitalizationReason(models.TextChoices):
        BELOW_AVERAGE_WEIGHT = "BELOW_AVERAGE_WEIGHT", "انخفاض وزن الطفل"
        NEED_MEDICATION = "NEED_MEDICATION", "احتياج الطفل لأدوية محددة بهذا الوقت"
        DIFFICULTY_BREATHING = (
            "DIFFICULTY_BREATHING",
            "صعوبة شديدة في التنفس لعدم اكتمال نمو الرئتين",
        )
        FEVER = "FEVER", "ارتفاع درجة حرارة جسم الرضيع"
        ABNORMAL_VITAL_SIGNS = (
            "ABNORMAL_VITAL_SIGNS",
            "تعطل العمليات الحيوية بجسم الطفل",
        )
        HYPOGLYCEMIA = "HYPOGLYCEMIA", "انخفاض معدل الجلوكوز في دم الطفل"
        ABNORMAL_GIT_FUNCTION = (
            "ABNORMAL_GIT_FUNCTION",
            "معاناة الرضيع مشكلات في الجهاز الهضمي",
        )
        SEPTICEMIA = "SEPTICEMIA", "اصابة الطفل بعدوي في الدم"
        JAUNDICE = "JAUNDICE", "اصابة الطفل بالصفراء"
        PROBLEMS_DURING_PREGNANCY = "PROBLEMS_DURING_PREGNANCY", (
            "حدوث مشكلات خلال الولادة الولادة المتعسرة أو الحمل الحرج"
        )
        BIRTH_DEFECT = (
            "BIRTH_DEFECT",
            "وجود عيب خلقي يمنع الطفل عن التنفس أو الرضاعة بشكل طبيعي",
        )

    name = models.CharField(max_length=150)
    birth_date = models.DateField()
    curr_age_in_months = models.IntegerField()
    uterine_age_in_months = models.IntegerField()
    delivery_type = models.CharField(max_length=10, choices=Delivery.choices)
    delivery_location = models.CharField(
        max_length=10, choices=DeliveryLocation.choices
    )
    birth_weight_in_gm = models.IntegerField()
    birh_height_in_cm = models.IntegerField()
    birth_head_size_in_cm = models.IntegerField()
    birth_hospitalization = models.BooleanField(default=False)
    birth_hospitalization_duration_in_days = models.IntegerField(blank=True, null=True)
    birth_hospitalization_reason = models.CharField(
        max_length=150, choices=HospitalizationReason.choices
    )
    first_hour_skin_to_skin_contact = models.BooleanField(default=False)
    first_hour_breast_feeding = models.BooleanField(default=False)


class Education(models.TextChoices):
    NONE = "NONE", "أمي"
    CAN_READ = "CAN_READ", "يجيد القراء"
    MODERATE = "MODERATE", "مؤهل متوسط"
    ABOVE_MODERATE = "ABOVE_MODERATE", "فوق المتوسط"
    EXCELLANT = "EXCELLANT", "مؤهل عالي"


class FatherInfo(models.Model):
    name = models.CharField(max_length=150)
    id_number = models.CharField(max_length=14, blank=True)
    phone_number = models.CharField(max_length=11, blank=True)
    education = models.CharField(max_length=150, choices=Education.choices)
    job = models.BooleanField(default=False)


class MotherInfo(models.Model):
    name = models.CharField(max_length=150)
    id_number = models.CharField(max_length=14, blank=True)
    phone_number = models.CharField(max_length=11, blank=True)
    birh_date = models.DateField(blank=True, null=True)
    education = models.CharField(max_length=150, choices=Education.choices)
    job = models.BooleanField(default=False)
    no_of_kids = models.IntegerField()
    duration_between_last_two_pregnancies_in_months = models.IntegerField()
    is_using_contraceptives = models.BooleanField(default=False)
    is_planning_a_pregnancy = models.BooleanField(default=False)


class DevelopmentProgress(models.Model):
    class ProgressStatus(models.TextChoices):
        NORMAL = (
            "NORMAL",
            "طبيعي",
        )
        EARLY = (
            "EARLY",
            "متقدم",
        )
        LATE = "LATE", "متأخر"

    movement = models.CharField(max_length=10, choices=ProgressStatus.choices)
    mental = models.CharField(max_length=10, choices=ProgressStatus.choices)
    linguistic = models.CharField(max_length=10, choices=ProgressStatus.choices)


class VisitTopics(models.Model):
    breast_feeding_benefits = models.BooleanField(default=False)
    normal_stool_frequency = models.BooleanField(default=False)
    vitamin_d_supplement = models.BooleanField(default=False)
    navel_care_and_hygiene = models.BooleanField(default=False)
    healthcare_id_and_followup = models.BooleanField(default=False)
    vaccination = models.BooleanField(default=False)
    nutrition_for_breast_feeding_mother = models.BooleanField(default=False)
    recognizing_abnormal_behaviour = models.BooleanField(default=False)
    develoment_progress = models.ForeignKey(
        to=DevelopmentProgress, on_delete=models.CASCADE
    )
    positive_education = models.BooleanField(default=False)
    encouraging_activities = models.BooleanField(default=False)
    positive_education = models.BooleanField(default=False)
    iron_supplement = models.BooleanField(default=False)
    contraceptives_and_abstinence = models.BooleanField(default=False)


class VisitInfo(models.Model):
    class VisitTiming(models.TextChoices):
        FIRST_WEEK = "FIRST_WEEK", "الاسبوع الاول"
        ONE_MONTH = "ONE_MONTH", "عمر شهر"
        TWO_MONTH_OLD = "TWO_MONTH_OLD", "عمر شهرين"
        THREE_MONTH_OLD = "THREE_MONTH_OLD", "عمر 3 شهور"
        FOUR_MONTH_OLD = "FOUR_MONTH_OLD", "عمر 4 شهور"
        SIX_MONTH_OLD = "SIX_MONTH_OLD", "عمر 6 شهور"
        NINE_MONTH_OLD = "NINE_MONTH_OLD", "عمر 9 شهور"
        TWELVE_MONTH_OLD = "TWELVE_MONTH_OLD", "عمر 12 شهر"
        EIGHTEEN_MONTH_OLD = "EIGHTEEN_MONTH_OLD", "عمر 18 شهر"
        TWO_YEAR_OLD = "TWO_YEAR_OLD", "عمر سنتين"
        THREE_YEAR_OLD = "THREE_YEAR_OLD", "عمر 3 سنوات"

    class ExclusiveBreastFeedingDuration(models.TextChoices):
        THREE_MONTHS = "THREE_MONTHS", "3 شهور"
        FOUR_MONTHS = "FOUR_MONTHS", "4 شهور"
        SIX_MONTHS = "SIX_MONTHS", "6 شهور"

    class BreastFeeding(models.TextChoices):
        ONLY_NATURAL = "ONLY_NATURAL", "رضاعة طبيعية مطلقة"
        LIQUIDS_AND_HERBS = "LIQUIDS_AND_HERBS", "سوائل واعشاب"
        NATURAL_PLUS_PROCESSED_MILK = (
            "NATURAL_PLUS_PROCESSED_MILK",
            "رضاعة طبيعية مع لبن صناعي",
        )
        PROCESSED_MILK = "PROCESSED_MILK", "لبن صناعي"

    timing = models.CharField(max_length=150, choices=VisitTiming.choices)
    date = models.DateField()
    breast_feeding = models.CharField(max_length=150, choices=BreastFeeding.choices)
    exclusive_breast_feeding_duration = models.CharField(
        max_length=150,
        choices=ExclusiveBreastFeedingDuration.choices,
        null=True,
        blank=True,
    )
    curr_weight_in_kg = models.FloatField()
    curr_height_in_cm = models.IntegerField()
    curr_head_size_in_cm = models.FloatField()
    visit_topics = models.ForeignKey(to=VisitTopics, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)
    unavailable_services = models.TextField(blank=True)
    notes_for_next_visit = models.TextField(blank=True)


class ChildMashora(models.Model):
    doctor = models.ForeignKey(to=DoctorInfo, on_delete=models.SET_NULL, null=True)
    mother = models.ForeignKey(
        to=MotherInfo, on_delete=models.CASCADE, related_name="child_mashora"
    )
    father = models.ForeignKey(
        to=FatherInfo, on_delete=models.CASCADE, related_name="child_mashora"
    )
    child = models.ForeignKey(
        to=ChildInfo, on_delete=models.CASCADE, related_name="child_mashora"
    )
    visit_info = models.ForeignKey(
        to=VisitInfo, on_delete=models.CASCADE, related_name="child_mashora"
    )
