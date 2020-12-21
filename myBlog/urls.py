from django.urls import path
from . views import IndexView, PostDetailView, CreatePostView, UpdatePostView, \
    UserRegisterView, CreateCategoryView, CategoryView, AddCommentView

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    path('add_post/', CreatePostView.as_view(), name="create-post"),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('categories', CreateCategoryView.as_view(), name='add-category'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('add_comment/<int:pk>/comment', AddCommentView.as_view(), name='add-comment')
]