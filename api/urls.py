from django.urls import path
from . import views

urlpatterns = [
    path("projects/",views.ListProjectAPIView.as_view(),name="projects_list"),
    path("project/create/", views.CreateProjectAPIView.as_view(),name="project_create"),
    path("project/update/<int:pk>/",views.UpdateProjectAPIView.as_view(),name="project_update"),
    path("project/delete/<int:pk>/",views.DeleteProjectAPIView.as_view(),name="project_delete"),

    path("users/",views.UserList.as_view(),name="users_list"),
    path("user/create/", views.UserCreate.as_view(),name="user_create"),
    path("user/update/<int:pk>/",views.UserUpdate.as_view(),name="user_update"),
    path("user/delete/<int:pk>/",views.UserDelete.as_view(),name="user_delete"),

]