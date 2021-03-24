from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path("", views.index, name = 'index'),
    path('loved/', views.loved, name='loved'),
    path('bookmarks/', views.bookmarks, name='bookmarks')
]
