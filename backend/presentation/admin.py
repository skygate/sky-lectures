from django.contrib import admin

from presentation.models import Tag, Presentation, Notification

admin.site.register(Tag)
admin.site.register(Presentation)
admin.site.register(Notification)
