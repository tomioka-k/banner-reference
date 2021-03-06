from django.urls import path
from .views import CategoryListAPIView, TagListAPIView, ColorListAPIView, ImageListAPIView, ImageCountAPIView

urlpatterns = [
    path('category/', CategoryListAPIView.as_view(), name='category'),
    path('tag/', TagListAPIView.as_view(), name='tag'),
    path('color/', ColorListAPIView.as_view(), name='color'),
    path('image/', ImageListAPIView.as_view(), name='image'),
    path('image/count/', ImageCountAPIView.as_view(), name="image-count")
]
