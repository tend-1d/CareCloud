from django.contrib import admin
from careapp.models import Patient
from careapp.models import Doctor
from careapp.models import MyAppointments
from careapp.models import ContactMessage
from careapp.models import Transaction

# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(MyAppointments)
admin.site.register(ContactMessage)
admin.site.register(Transaction)



