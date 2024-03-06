from django.urls import path
from . import views
from django.conf.urls.static import static
from .views import maquina, form, create, view,edit, update, delete
from django.contrib import admin
from .views import consumo, form2, cre, view2, edit2, update2,delete2,pdf,pdf1,cvs,cvs1


urlpatterns = [
    
    path('oWorld/', views.helloWorld),
    path('', views.taskList, name='tasks-list'),
    path('task/<int:id>', views.taskView, name="task-view"),
    path('newtask/', views.newTask, name="new-task"),
    path('edit/<int:id>', views.editTask, name="edit-task"),
    path('delete/<int:id>', views.deleteTask, name="delete-task"),
    path('yourname/<str:name>', views.yourName, name='your-name'),
    path('maquina/', views.maquina, name='maquina'),
    path('form/', views.form, name='form'),
    path('create/',views.create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name= 'delete'),
    path('consumo/',views.consumo, name='consumo'),
    path('form2/',views.form2, name='form2'),
    path('cre/', views.cre, name='cre'),
    path('view2/<int:pk>/', view2, name='view2'),
    path('edit2/<int:pk>/', edit2, name='edit2'),
    path('update2/<int:pk>/', update2, name='update2'),
    path('delete2/<int:pk>/', delete2, name= 'delete2'),
    path('pdf/',pdf , name= 'pdf'),
    path('cvs/',cvs , name= 'cvs'),
    path('pdf1/',pdf1 , name= 'pdf1'),
    path('cvs1/',cvs1 , name= 'cvs1'),
    
]

