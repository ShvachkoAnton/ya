from django.contrib import admin
from .models import Contact, Post,Profile,Comment




class PostAdmin(admin.ModelAdmin):
    list_display=('text','pub_date','author')
    search_fields=('text',)
    list_filter=('pub_date',)
admin.site.register(Post,PostAdmin)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Contact)
# Register your models here.

