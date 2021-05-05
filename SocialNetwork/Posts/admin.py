from django.contrib import admin
from .forms import PostsCreateForm,CommentsAdminEditForm,CommentsAdminCreateForm
from .models import Post,Comment

class PostAdmin(admin.ModelAdmin):
    form=PostsCreateForm
    def save_model(self, request, instance, form, change):
        form.instance.user = self.request.user 
        super(Post, self).save_model(request, instance, form, change)
    
class AdminComment(admin.ModelAdmin):
    form=CommentsAdminCreateForm





admin.site.register(Post,PostAdmin)
admin.site.register(Comment,AdminComment)

# Register your models here.
