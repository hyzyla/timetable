from django.db import models

# Create your models here.


class University(models.Model):
    id = models.AutoField(primary_key=True)
    full_title = models.CharField(max_length=1024)
    short_title = models.CharField(max_length=256)

    def __str__(self):
        return "{}".format(self.short_title)


class Building(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    floor_number = models.IntegerField()
    university = models.ForeignKey(University, models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)


class Room(models.Model):

    TYPE_OF_ROOMS = [
        ('s', 'семінарський'),
        ('l', 'лекційний'),
        ('a', 'адміністративний'),
        ('o', 'інший'),
    ]

    id = models.AutoField(primary_key=True)
    id_building = models.ForeignKey(Building, models.CASCADE)
    floor = models.IntegerField()
    name = models.CharField(max_length=16)
    room_type = models.CharField( max_length=2, choices=TYPE_OF_ROOMS, default='o')

    def __str__(self):
        return "{}".format(self.name)


class Faculty(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=512)
    university = models.ForeignKey(University, models.CASCADE)

    def __str__(self):
        return "{}".format(self.title)


class Lecturer(models.Model):
    id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=256)

    faculty = models.ForeignKey(Faculty, models.CASCADE)

    def __str__(self):
        return "{}".format(self.last_name)


class Specialization(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=512)
    id_faculty = models.ForeignKey(Faculty, models.CASCADE)

    def __str__(self):
        return "{}".format(self.title)


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    id_specialization = models.ForeignKey(Specialization, models.CASCADE)
    year_of_study = models.IntegerField()
    title = models.CharField(max_length=256)

    def __str__(self):
        return "{}".format(self.title)


class Lesson(models.Model):

    TYPE_OF_LESSON = [
        ('l', 'Лекція'),
        ('c', 'Консультація'),
        ('s', 'Семінар'),
        ('o', 'Інший'),
        ('b', 'Лабораторна'),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=512)
    id_specialization = models.ForeignKey(Specialization, models.CASCADE)
    lesson_type = models.CharField(max_length=2, choices=TYPE_OF_LESSON)

    def __str__(self):
        return "{} ({})".format(self.title, self.lesson_type)


class LessonTime(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    time_begin = models.TimeField()
    time_end = models.TimeField()
    university = models.ForeignKey(University, models.CASCADE)

    def __str__(self):
        return "{}.({}-{}) {}".format(self.number, self.time_begin.strftime("%H:%M"), 
            self.time_end.strftime("%H:%M"), self.university)


class Timetable(models.Model):

    DAYS_OF_WEEK = [
        ('1', 'Понеділок'),
        ('2', 'Вівторок'),
        ('3', 'Середа'),
        ('4', 'Четвер'),
        ('5', "П'ятниця"),
        ('6', 'Субота'),
        ('7', 'Неділя'),
    ]

    TYPE_OF_WEEK = [
        ('1', 'Парний тиждень'),
        ('2', 'Непарний тиждень'),
        ('0', 'Обидва тижні'),
    ]

    id = models.AutoField(primary_key=True)
    day = models.CharField(max_length=2, choices=DAYS_OF_WEEK)
    week_type = models.CharField(max_length=2, choices=TYPE_OF_WEEK)
    id_group = models.ForeignKey(Group, models.CASCADE)
    id_lesson = models.ForeignKey(Lesson, models.CASCADE)
    id_room = models.ForeignKey(Room, models.CASCADE)
    id_lecturer = models.ForeignKey(Lecturer, models.CASCADE)
    id_time = models.ForeignKey(LessonTime, models.CASCADE)

    def __str__(self):
        return "{} - {} - {} - {} - {} - {} - {} - {}".format(  self.id,
                                                                self.day,
                                                                self.week_type,
                                                                self.id_group,
                                                                self.id_lesson,
                                                                self.id_room,
                                                                self.id_lecturer,
                                                                self.id_time)

