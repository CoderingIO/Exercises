from django.urls import include,path
from django.contrib import admin

urlpatterns = [
    path('exercises/', include('exercises.urls')),
    path('admin/', admin.site.urls),
]