from django.urls import path
from . import views

urlpatterns=[
    path('reload',views.loadComments,name='loadComments'),
    path('',views.default,name='home'),
    path('loadArticles',views.loadArticles,name='load articles'),
    path('submissions',views.submissions,name='submissions'),
    path('new',views.new,name='submissions'),
    path('submit_article',views.submit_article,name='submit_article'),
    path('home',views.home,name='feeds'),
    path('account',views.account,name='account'),
    path('logout',views.default,name='logout')
   
]