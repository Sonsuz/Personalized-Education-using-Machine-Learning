from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^LearningApp/', include('LearningApp.urls')),
    url(r'^', include('LearningApp.urls')),
]
