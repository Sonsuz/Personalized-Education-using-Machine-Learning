from django.contrib.auth.models import Permission, User
from django.db import models
import datetime



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=15, blank=True)
    phone = models.IntegerField(default=0)
    group_choices = (('Student','Student'),('Teacher','Teacher'),('Other','Other'))
    user_type = models.CharField(max_length=30, choices=group_choices, default='Student')
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return str(self.user.first_name)

class LectureNotes(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    courseName = models.CharField(max_length=20)
    document = models.FileField(upload_to='documents/')
    description = models.CharField(max_length=300, blank=True)
    uploaded_at = models.DateTimeField(default=datetime.datetime.now(), blank=True)

    def __str__(self):
         return str(self.courseName)+ ', ' + str(self.document)

class DCategory(models.Model):
    category_name = models.CharField(max_length=20)
    def __str__(self):
         return str(self.category_name)

class Discussion(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    category =  models.ForeignKey(DCategory, on_delete=models.CASCADE, default=1)
    topic = models.CharField(max_length=50)
    sub_topic = models.CharField(max_length=50)
    post = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.datetime.now(), blank=True)

    def __str__(self):
        return str(self.topic) + " " + str(self.category)

class Blog(models.Model):
    blog_name = models.CharField(max_length=50)
    def __str__(self):
         return str(self.blog_name)
class Author(models.Model):
    author_name = models.CharField(max_length=50)
    def __str__(self):
         return str(self.author_name)

class Blogpost(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, default=1)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=5000)
    link = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='blog_img', blank=True)

    def __str__(self):
        return str(self.blog) + " " + str(self.title)

class Subject(models.Model):
    subject_name = models.CharField(max_length=50)
    def __str__(self):
         return str(self.subject_name)
class Instructor(models.Model):
    instructor_name = models.CharField(max_length=50)
    def __str__(self):
         return str(self.instructor_name)
class Provider(models.Model):
    provider_name = models.CharField(max_length=50)
    def __str__(self):
         return str(self.provider_name)
class University(models.Model):
    university_name = models.CharField(max_length=50)
    def __str__(self):
         return str(self.university_name)
class Language(models.Model):
    lang = models.CharField(max_length=50)
    def __str__(self):
         return str(self.lang)

class Course(models.Model):
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=300, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=1)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, default=1)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, default=1)
    university = models.ForeignKey(University, on_delete=models.CASCADE, default=1, blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=1)
    duration = models.CharField(max_length=50)
    cost = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='course_img', blank=True)
    link = models.CharField(max_length=500)

    def __str__(self):
        return str(self.title) + " - " + str(self.subject)

class WishList(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, default=1, on_delete=models.CASCADE)
    wished = models.BooleanField(default=False)
    def __str__(self):
         return str(self.user)+ ', ' + str(self.course)

class FavList(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, default=1, on_delete=models.CASCADE)
    favorited = models.BooleanField(default=False)
    def __str__(self):
         return str(self.user)+ ', ' + str(self.course)
