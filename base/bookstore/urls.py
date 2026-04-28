from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>', views.single_book, name='single_book'),
    path('author/<int:author_id>', views.bulgakov, name='bulgakov'),
]