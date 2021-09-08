from django.contrib import admin

from presentation.models import Comment, Presentation


class CommentAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False


admin.site.register(Comment, CommentAdmin)
admin.site.register(Presentation)
