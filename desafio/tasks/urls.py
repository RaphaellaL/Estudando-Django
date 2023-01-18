from django.urls import path
from . import views


urlpatterns = [
    path('helloword/', views.helloword),
    path('', views.taskList, name='index'),
    path('newtask/', views.newTask, name='new-task'),
    path('delete/<int:id>', views.deleteTask, name='delete-task')
    
    

]