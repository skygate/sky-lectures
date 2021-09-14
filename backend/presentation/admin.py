from django.contrib import admin

from presentation.models import Comment, Presentation, Tag


class CommentAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False


admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag)
admin.site.register(Presentation)
