from django.contrib import admin
from blog.models import *
# from media.admin import MediaAdmin
# Register your models here.
from django_markdown.admin import MarkdownModelAdmin

# admin.site.register(Blog)
admin.site.register(Cases)
admin.site.register(About_us)
admin.site.register(Contact_us)
admin.site.register(Picture)
admin.site.register(Anli)
admin.site.register(CateBlog)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_filter = ('type', 'public_date',)
    search_fields = ('id', 'title',)
    list_per_page = 20


#admin.site.register(Book)
admin.site.register(Blog, MarkdownModelAdmin)

# class MediaAdmin(admin.StackedInline):
#     model = Media
#     admin.site.register(Media)


# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'date', 'author')
#     radio_fields = {'post_status': admin.VERTICAL,
#                     'type': admin.VERTICAL,
#                     'comment_status': admin.VERTICAL}
#     inlines = [MediaAdmin,]

#     class Media:
#         # js = ( 
#         #     '/static/js/tiny_mce/tiny_mce.js',
#         #     '/static/js/textareas.js',
#         # )   
#         admin.site.register(Post, PostAdmin)