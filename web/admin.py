from django.contrib import admin
from .models import *


class Result_post_admin_list(admin.ModelAdmin):
    list_display = (
        'address',
        'business_name',
    )
    list_display_links = (
        'address',
        'business_name',
    )

class Notice_post_admin_list(admin.ModelAdmin):
    list_display = (
        'title',
        'create_at',
    )
    list_display_links = (
        'title',
    )

class Information_post_admin_list(admin.ModelAdmin):
    list_display = (
        'author',
        'title',
        'phone_number',
        'create_at'
    )
    list_display_links = (
        'author',
        'title',
        'phone_number',
    )

admin.site.register(Result_post, Result_post_admin_list)
admin.site.register(Notice_post, Notice_post_admin_list)
admin.site.register(Information_post, Information_post_admin_list)
