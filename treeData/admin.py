from django.contrib import admin

from .models import Node


class NodeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'parent',
    )

    ordering = ('name'.lower(),)


admin.site.register(Node, NodeAdmin)
