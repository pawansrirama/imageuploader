from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home) #open path of  views
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #to open media files when clicked