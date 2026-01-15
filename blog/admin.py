from django.contrib import admin
from .models import Post, Category, Comment, AuthorApplication



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_at')
    list_filter = ('status', 'category')
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name='Authors').exists():
            return qs.filter(author=request.user)
        return qs

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user

        if request.user.groups.filter(name='Authors').exists():
            obj.status = 'draft'

        super().save_model(request, obj, form, change)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'approved', 'created_at')
    list_filter = ('approved', 'created_at')
    search_fields = ('name', 'email', 'content')
    list_editable = ('approved',)







@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_at')
    list_filter = ('status', 'category', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')
    ordering = ('-created_at',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}



@admin.register(AuthorApplication)
class AuthorApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'approved', 'created_at')
    list_filter = ('approved', 'created_at')
    search_fields = ('name', 'email')
    list_editable = ('approved',)



# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('name',)}


    