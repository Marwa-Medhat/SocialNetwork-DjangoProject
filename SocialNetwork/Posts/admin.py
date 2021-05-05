from django.contrib import admin
from .forms import PostsCreateForm
from .models import Post,Comment
from .forms import CommentsAdminCreateForm

class PostAdmin(admin.ModelAdmin):
    form=PostsCreateForm


class AdminComment(admin.ModelAdmin):
    form=CommentsAdminCreateForm


admin.site.register(Post,PostAdmin)
admin.site.register(Comment,AdminComment)
# Register your models here.
