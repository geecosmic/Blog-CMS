from django.shortcuts import render, get_object_or_404
# from .models import Post, Category


from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden

from django.contrib.auth import authenticate, logout
from django.contrib.auth.views import LoginView


from .models import Post, Category,AuthorApplication
from .forms import PostForm, AdminUserCreationForm, AuthorApplicationForm
# from django.contrib.auth import login
from django.shortcuts import redirect

from django.contrib.auth.views import LoginView

from django.utils.text import slugify
import uuid
from django.contrib import messages

from .utils.permissions import is_editor, is_author

from django.contrib.auth.decorators import login_required, user_passes_test



from django.contrib.auth.decorators import user_passes_test

def admin_required(view_func):
    return user_passes_test(lambda u: u.is_superuser, login_url='login')(view_func)



from .utils.email_helpers import send_password_setup_email
@admin_required
def admin_register_user(request):
    if request.method == 'POST':
        form = AdminUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Send password setup email
            send_password_setup_email(user, request)
            messages.success(
                request, 
                "User created successfully. An email has been sent for password setup."
            )
            return redirect('dashboard')
    else:
        form = AdminUserCreationForm()

    return render(request, 'blog/admin_register.html', {'form': form})




class CustomLoginView(LoginView):
    template_name = 'blog/login.html'  # your login template
    redirect_authenticated_user = True

    def get_success_url(self):
        return '/dashboard/'  # force all users to site dashboard
    




def subscribe(request):
    if request.method == 'POST':
        form = AuthorApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your application has been submitted. Admin will review it.")
            return redirect('subscribe')
    else:
        form = AuthorApplicationForm()
    return render(request, 'blog/subscribe.html', {'form': form})



def role_based_redirect(user):
    if user.is_superuser:
        return '/admin/'
    if user.groups.filter(name__in=['Authors', 'Editors']).exists():
        return '/dashboard/'
    return '/'



# class CustomLoginView(LoginView):
#     def get_success_url(self):
#         return role_based_redirect(self.request.user)



def post_list(request):
    posts = Post.objects.filter(status='published')
    categories = Category.objects.all()
    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'categories': categories
    })

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    return render(request, 'blog/post_detail.html', {'post': post})





def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = f"{slugify(self.title)}-{uuid.uuid4().hex[:6]}"
    super().save(*args, **kwargs)


from .forms import CommentForm

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    comments = post.comments.filter(approved=True)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            form = CommentForm()
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })




# @login_required
# def dashboard(request):
#     user = request.user

#     if user.groups.filter(name='Editor').exists():
#         # Editors see ALL posts
#         posts = Post.objects.all()
#     else:
#         # Authors see only their own posts
#         posts = Post.objects.filter(author=user)

#     return render(request, 'blog/dashboard.html', {'posts': posts})


@login_required
def dashboard(request):
    user = request.user

    if is_editor(user):
        # Editors (and superusers) see ALL posts
        posts = Post.objects.all()
    elif is_author(user):
        # Authors see only their own posts
        posts = Post.objects.filter(author=user)
    else:
        messages.error(request, "You are not allowed to access the dashboard.")
        return redirect('login')

    return render(request, 'blog/dashboard.html', {
        'posts': posts,
        'user': user
    })



@login_required
def add_post(request):
    user = request.user

    # 🔐 Permission gate
    if not (is_editor(user) or is_author(user)):
        return HttpResponseForbidden("You are not allowed")

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = user

            # 🔒 Publishing rule
            if is_editor(user):
                post.status = 'published'
            else:
                post.status = 'draft'

            post.save()
            return redirect('dashboard')
    else:
        form = PostForm()

    return render(request, 'blog/post_form.html', {'form': form})



@login_required
def edit_post(request, pk):
    user = request.user
    post = get_object_or_404(Post, pk=pk)

    # Only the author OR an editor can edit
    if post.author != request.user and not request.user.groups.filter(name='Editor').exists():
        return HttpResponseForbidden("You are not allowed")

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)

            # 🔒 ENFORCE PUBLISHING RULES
            # if post.can_publish(request.user):
            #     post.status = 'published'
            # else:
            #     post.status = 'draft'

            if is_editor(user):
                post.status = 'published'
            else:
                post.status = 'draft'

            post.save()
            return redirect('dashboard')
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_form.html', {'form': form})



# =Forsubscribers=============================




def admin_required(view_func):
    return user_passes_test(
        lambda u: u.is_authenticated and u.is_superuser,
        login_url='login'
    )(view_func)


@admin_required
def author_applications(request):
    applications = AuthorApplication.objects.all().order_by('-created_at')
    return render(
        request,
        'blog/admin_author_applications.html',
        {'applications': applications}
    )














def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories})




def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category, status='published')
    return render(request, 'blog/category_posts.html', {
    'category': category,
    'posts': posts
    })








def logout_view(request):
    logout(request)
    return redirect('login')