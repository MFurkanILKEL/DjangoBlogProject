from django.contrib import admin
from articles import views
from django.urls import path



app_name = "articles"


urlpatterns = [

    path('network/', views.networkArticles , name = "network"),
    path('SoC/', views.SoCArticles , name = "SoC"),
    path('forensic/', views.forensicArticles , name = "forensic"),
    path('karisik/', views.karisikArticles , name = "karisik"),

    path('networkDetail/<int:id>', views.networkDetail , name = "networkDetail"),
    path('SoCDetail/<int:id>', views.SoCDetail , name = "SoCDetail"),
    path('forensicDetail/<int:id>', views.forensicDetail , name = "forensicDetail"),
    path('karisikDetail/<int:id>', views.karisikDetail , name = "karisikDetail"),  

]