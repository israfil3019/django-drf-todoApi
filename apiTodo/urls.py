from django.urls import path
from .views import (
    TodoDetailAPIView,
    TodoListCreateAPIView,
    home,
    # todoDetail,
    # todoCreate,
    # todoList,
    # todoListCreate
)

urlpatterns = [
    path('', home),
    # path('todoList/', todoList),
    # path('todoCreate/', todoCreate),
    # path('todoListCreate/', todoListCreate),
    path('todoListCreate/', TodoListCreateAPIView.as_view()),
    path('todoDetail/<int:pk>', TodoDetailAPIView.as_view()),
    # path('todoDetail/<int:pk>/', todoDetail),
]
