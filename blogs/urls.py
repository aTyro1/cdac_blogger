from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('/loadArticles',views.loadArticles,name='load articles'),
    path('/submissions',views.submissions,name='submissions'),
    path('/new',views.new,name='submissions'),
    path('/submit_article',views.submit_article,name='submit_article')
]