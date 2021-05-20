from django.db import models

class Schedule(models.Model):
    SCHEDULE_TYPES = (
        ("A1", '교양선택'),
        ("B1", '인성필수'),
        ("C1`", '전공선택'),
        ("C2", '전공필수'),
    )
    title = models.CharField(max_length=50)
    date = models.DateField(null=True)
    professor = models.CharField(max_length=30, blank=True)
    grade = models.DecimalField(max_digits=5, decimal_places=2)
    meo = models.CharField(max_length=500, blank=True)
    schedule_type = models.CharField(choices=SCHEDULE_TYPES,max_length=20)

    class Meta:
        db_table = "django"

