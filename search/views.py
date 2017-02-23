from django.shortcuts import render, HttpResponse, render_to_response, RequestContext
from django.template import loader
from django.db.models import Q, Count
import json
from .models import LessonTime, Faculty, Specialization, Group, Timetable, University

# Create your views here.
def index(request):
    if request.is_ajax():
        selectedField = request.GET.get("selectedField")
        value = int(request.GET.get("value"))
        if selectedField == "university":
            value_list = Faculty.objects.filter(university__exact=value)
        elif selectedField == "faculty":
            value_list = Specialization.objects.filter(id_faculty__exact=value)
        elif selectedField == "specialization":
            value_list = Group.objects.filter(id_specialization__exact=value)
        context = { 'value_list': value_list }
        return render_to_response('search/options.html', context)


    university_list = University.objects.all()
    day_list = {
                0:"Весь тиждень",
                1:"Понеділок", 
                2:"Вівторок", 
                3:"Середа", 
                4:"Четвер", 
                5:"П'ятниця", 
                6:"Субота", 
                7:"Неділя",
    }
    week_list = {0:"Обидва тижні",
                 1:"Парний тиждень", 
                 2:"Непарний тиждень", 
    }

    context = { 'day_list':day_list,
                'week_list':week_list,
                'university_list': university_list,
    }
    return render(request, 'search/index.html', context)

def result(request, group, day, week_type):
    if day == '0':
        entries = Timetable.objects.filter(id_group__exact=group)    
    elif week_type == '0':
        entries = Timetable.objects.filter(day__exact=day, id_group__exact=group)
    else:
        entries = Timetable.objects.filter(Q(week_type__exact=week_type) | Q(week_type__exact='0'),
                                           Q(day__exact=day), Q(id_group__exact=group))

    entries = entries.order_by('day', 'id_time__number')
    days = list(entries.values('day'))
    number_of_days = [int(x["day"]) for x in days]
    number_of_days = list(set(number_of_days))
    print(number_of_days)
    day_list = {
                0:"Весь тиждень",
                1:"Понеділок", 
                2:"Вівторок", 
                3:"Середа", 
                4:"Четвер", 
                5:"П'ятниця", 
                6:"Субота", 
                7:"Неділя",
    }
    days = []
    for x in number_of_days:
        days.append({"day": str(x), "name":day_list[x]})
    print(days)
    context = {
        'days':  days,
        'result': entries,
    }
    return render(request, 'search/result.html', context)

def update_select(request):
    if request.is_ajax():
        pass

 