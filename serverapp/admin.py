from django.contrib import admin
from .models import Users, Mountains, Achievements, Comments
# Register your models here.
admin.site.register(Users)

admin.site.register(Mountains)
admin.site.register(Comments)
admin.site.register(Achievements)


