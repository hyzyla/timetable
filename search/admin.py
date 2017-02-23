from django.contrib import admin
from .models import Lecturer, \
					Building, \
					Room, \
					Group, \
					Lesson, \
					Specialization, \
					Faculty, \
					Timetable, \
					LessonTime, \
					University
					
# Register your models here.
admin.site.register(Lecturer)
admin.site.register(Building)
admin.site.register(Room)
admin.site.register(Group)
admin.site.register(Lesson)
admin.site.register(Specialization)
admin.site.register(Faculty)
admin.site.register(Timetable)
admin.site.register(LessonTime)
admin.site.register(University)
