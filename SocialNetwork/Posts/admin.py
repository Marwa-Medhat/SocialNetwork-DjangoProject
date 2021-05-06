from django.contrib import admin
from .forms import PostsCreateForm,CommentsAdminEditForm,CommentsAdminCreateForm
from .models import Post,Comment


class PostAdmin(admin.ModelAdmin):
    form=PostsCreateForm
    def save_model(self, request, instance, form, change):
        form.instance.user_id = self.request.user.id
        super(Post, self).save_model(request, instance, form, change)
    
class AdminComment(admin.ModelAdmin):
   

    # data = {'user_id': request.user.id}
    form=CommentsAdminCreateForm
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(AdminComment, self).save_model(request, obj, form, change)
    
    # def user_id(self, request):
    #     return request.user.id
    # def get_form(self, request, *args, **kwargs):
    #     form = super(AdminComment, self).get_form(request, *args, **kwargs)
    #     form.user = request.user.id
    #     return form  
 
        
    
   





admin.site.register(Post,PostAdmin)
admin.site.register(Comment,AdminComment)

# Register your models here.
