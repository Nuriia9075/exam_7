from django.urls import path

from views import index, add_book, delete_book, update_book

urlpatterns = [
    path('', index, name='book'),
    path('book/', index, name='book'),
    path('book/add/', add_book, name='create'),
    path('book/<int:pk>/delete/', delete_book, name='delete'),
    path('book/<int:pk>/update/', update_book, name='update'),
]