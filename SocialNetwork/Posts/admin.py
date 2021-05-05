from django.contrib import admin
from .forms import PostsCreateForm,CommentsAdminEditForm,CommentsAdminCreateForm
from .models import Post,Comment

class PostAdmin(admin.ModelAdmin):
    form=PostsCreateForm

    def form_valid(self, form):
        form.instance.post = self.object
        form.instance.user_id_id = self.request.user.id
        return super().form_valid(form)



    
class AdminComment(admin.ModelAdmin):
    form=CommentsAdminCreateForm





admin.site.register(Post,PostAdmin)
admin.site.register(Comment,AdminComment)

# Register your models here.
