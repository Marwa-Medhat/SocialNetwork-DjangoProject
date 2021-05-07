from django.contrib import admin
from .forms import BadwordsCreateForm
from .models import BadWords



        
    
   

class AdminBadWords(admin.ModelAdmin):
       form=BadwordsCreateForm
 



admin.site.register(BadWords,AdminBadWords)

# Register your models here.
