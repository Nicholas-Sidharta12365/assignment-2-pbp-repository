from django.urls import path, include
from . import views
# TODO: Implement Routings Here

app_name= 'todolist'

urlpatterns= [
   path('', views.todolist, name="todolist"),
   path('login/', views.login_user, name="login"),
   path('register/', views.register, name="register"),
   path('logout/', views.logout_user, name="logout"),
   path('create-task/', views.create_task, name="create_task")
]