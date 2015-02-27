from django.contrib import admin

from photogallery.models import Photo, Category


class PhotoInline(admin.StackedInline):
    model = Photo
    

class CategoryAdmin(admin.ModelAdmin):
    inline = [PhotoInline]
    

admin.site.register(Category,CategoryAdmin )
admin.site.register(Photo)
    
