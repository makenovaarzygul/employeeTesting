from django.contrib import admin

from OTS.models import Question
from OTS.models import User,Result

# Register your models here.
admin.site.register(Question)
admin.site.register(User)
admin.site.register(Result)

