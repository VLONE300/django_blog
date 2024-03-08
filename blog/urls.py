from django.urls import path
from blog import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create_post/', views.create_post, name='create_post'),
    path('post/<int:pk>/edit/', views.EditPostView.as_view(), name='edit-post'),
    path('tags/<tag_slug>/', views.posts_by_tag, name='post_by_tag'),
    path('author/<int:author_id>/', views.AuthorView.as_view(), name='author')

]
