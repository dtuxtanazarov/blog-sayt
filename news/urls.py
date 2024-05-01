from django.urls import path
from .views import News_view, Post_detail

urlpatterns=[
    path('post/<int:pk>/',Post_detail.as_view(), name= 'detail_page'),
    path('',News_view.as_view(),name='home'),

]