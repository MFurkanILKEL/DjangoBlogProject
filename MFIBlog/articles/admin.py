from django.contrib import admin
from .models  import Network , SoC , Forensic , karisik

@admin.register(Network)
class networkAdmin(admin.ModelAdmin):
    
    list_display = ["title","author","createDate"]

    list_display_links = ["title","author","createDate"]

    search_fields = ["title"]
    
    list_filter = ["createDate"]
    
    class Meta:
        model = Network



@admin.register(SoC)
class SoCAdmin(admin.ModelAdmin):
    
    list_display = ["title","author","createDate"]

    list_display_links = ["title","author","createDate"]

    search_fields = ["title"]
    
    list_filter = ["createDate"]
    
    class Meta:
        model = SoC



@admin.register(Forensic)
class forensicAdmin(admin.ModelAdmin):
    
    list_display = ["title","author","createDate"]

    list_display_links = ["title","author","createDate"]

    search_fields = ["title"]
    
    list_filter = ["createDate"]
    
    class Meta:
        model = Forensic



    
@admin.register(karisik)
class karisikAdmin(admin.ModelAdmin):
    
    list_display = ["title","author","createDate"]

    list_display_links = ["title","author","createDate"]

    search_fields = ["title"]
    
    list_filter = ["createDate"]
    
    class Meta:
        model = karisik


