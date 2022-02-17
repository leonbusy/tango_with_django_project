from csv import list_dialects
from django import views
from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile


# Register your models here.

class PageAdmin(admin.ModelAdmin):
    #create list_display
    list_display=('title','category','url')
class CategoryAdmin(admin.ModelAdmin):
    # can show list_display in admin manage page
    prepopulated_fields={'slug':('name',)}
    list_display=('name','views','likes')

admin.site.register(Category,CategoryAdmin)
#different show different page and function
admin.site.register(Page,PageAdmin)
# admin.site.register(Category)
# admin.site.register(CategoryAdmin)
# admin.site.register(Page)
# admin.site.register(PageAdmin)
admin.site.register(UserProfile)
