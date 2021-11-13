from django.urls import path
from .views import PostList, PostCreateList, PostDetail, PostUpdate, PostDelete

urlpatterns = [
    path('', PostList.as_view(), name='list'),
    path('create/', PostCreateList.as_view(), name='create'),
    path('detail/<int:pk>/', PostDetail.as_view(), name='detail'),
    path('update/<int:pk>/', PostUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='delete'),
]