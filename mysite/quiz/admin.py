from django.contrib import admin
from .models import Question, Choice, User, IncorrectChoice

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(User)
admin.site.register(IncorrectChoice)