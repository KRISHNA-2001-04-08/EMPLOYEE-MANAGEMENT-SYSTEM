from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    department = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)

    city = models.TextField(null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)

    gender = models.CharField(
        max_length=10,
        choices=[
            ("Male", "Male"),
            ("Female", "Female"),
            ("Other", "Other"),
        ],
        null=True,
        blank=True
    )

    salary = models.IntegerField(null=True, blank=True)
    experience = models.IntegerField(default=0)

    dob = models.DateField(null=True, blank=True)
    join_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
