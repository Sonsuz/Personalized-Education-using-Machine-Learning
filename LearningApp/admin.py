from django.contrib import admin
from .models import (UserProfile,
                    LectureNotes,
                    Discussion, DCategory,
                    Blogpost, Blog, Author,
                    Course, Subject, Instructor, Provider, University, Language,
                    WishList,
                    FavList)


# Register your models here.
admin.site.register(UserProfile)

admin.site.register(LectureNotes)

admin.site.register(Discussion)
admin.site.register(DCategory)

admin.site.register(Blogpost)
admin.site.register(Blog)
admin.site.register(Author)

admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Instructor)
admin.site.register(Provider)
admin.site.register(University)
admin.site.register(Language)

admin.site.register(WishList)
admin.site.register(FavList)
