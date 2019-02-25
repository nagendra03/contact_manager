from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    mobile = models.CharField(max_length=14)
    alternate_mobile = models.CharField(max_length=14, null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self): #converted object to string
        return self.first_name

    def get_full_name(self):
        full_name = self.first_name

        if self.middle_name:
            full_name = full_name + ' ' + self.middle_name

        if self.last_name:
            full_name = full_name + ' ' + self.last_name

        return full_name


