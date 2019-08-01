from django.contrib import admin
from jp001.models import indiaJob,indiaJob1,indiaJob2,indiaJob3

# Register your models here.

class indiaJobAdmin(admin.ModelAdmin):
    list_display=['empname','empexp','empskills','empphone']

class indiaJob1Admin(admin.ModelAdmin):
    list_display=['empname','empexp','empskills','empphone']

class indiaJob2Admin(admin.ModelAdmin):
    list_display=['empname','empexp','empskills','empphone']

class indiaJob3Admin(admin.ModelAdmin):
    list_display=['empname','empexp','empskills','empphone']

admin.site.register(indiaJob,indiaJobAdmin)
admin.site.register(indiaJob1,indiaJob1Admin)
admin.site.register(indiaJob2,indiaJob2Admin)
admin.site.register(indiaJob3,indiaJob3Admin)
