from django.contrib import admin

from users.models import Profile, User

admin.site.register(User)
admin.site.register(Profile)
