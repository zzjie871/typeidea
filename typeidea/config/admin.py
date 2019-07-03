from django.contrib import admin

from .models import Link, SideBar

from typeidea.base_admin import BaseOwnerAdmin

@admin.register(Link)
class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title', 'href', 'status', 'weight', 'created_time')
    fields = ('title', 'href', 'status', 'weight')



@admin.register(SideBar)
class SideBarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'display', 'content', 'created_time')
    fields = ('title', 'display_type', 'content')


