from django.urls import path
from .views import home, todoCreate, todoList, todoListCreate

urlpatterns = [
    path('', home, name= 'home'),
    path('todoList/', todoList),
    path('todoCreate/', todoCreate),
    path('todoListCreate/', todoListCreate),
]