from django.urls import path
from . import views
from .views import CustomLoginView, logout_view




# urlpatterns = [
#     path('', views.post_list, name='post_list'),
#     path('post/<slug:slug>/', views.post_detail, name='post_detail'),
# ]



urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('subscribe/', views.subscribe, name='subscribe'),

    path('dashboard/author-applications/',views.author_applications,name='author_applications'),


    path('admin-register/', views.admin_register_user, name='admin_register_user'),


    # CMS Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/add/', views.add_post, name='add_post'),
    path('dashboard/edit/<int:pk>/', views.edit_post, name='edit_post'),


    path('categories/', views.category_list, name='category_list'),
    path('categories/<slug:slug>/', views.category_posts, name='category_posts'),
]

