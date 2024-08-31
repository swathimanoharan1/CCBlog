# from django.contrib import admin
# from .models import posts  # Replace with your model names
# from .models import Image
# from django.utils.html import format_html

# admin.site.register(posts)
from django.contrib import admin
from .models import Post, Contact

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on')
    search_fields = ['title', 'content']


admin.site.register(Post, PostAdmin)

admin.site.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')