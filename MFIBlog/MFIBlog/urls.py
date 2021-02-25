from django.contrib import admin
from django.urls import path , include 
from articles import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    
    path('AdminFurkan/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('mfi05boks10network99/', admin.site.urls),
    path('', views.index , name = "index"),
    path('articles/', include("articles.urls")),
    path('ckeditor', include('ckeditor_uploader.urls')),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)