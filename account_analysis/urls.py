from rest_framework import routers
from account_analysis import views
from django.urls import path
from .models import *
from .views import *

app_name = 'account_analysis'

router = routers.SimpleRouter()

urlpatterns = [
    #========Workspaces and Progects=========  
    path("workspaces/",views.WorkspaceAccountAnalysisList.as_view(),name="account_analysis_workspaces_list"),
    path("workspaces/create/", views.WorkspaceAccountAnalysisCreate.as_view(),name="account_analysis_workspaces_create"),
    path("workspaces/update/<int:pk>/",views.WorkspaceAccountAnalysisUpdate.as_view(),name="account_analysis_workspaces_update"),
    path("workspaces/delete/<int:pk>/",views.WorkspaceAccountAnalysisDelete.as_view(),name="account_analysis_workspaces_delete"),
    #=======Widgets======
    path("account_analysis_summary_widget/<int:pk>/<int:widget_pk>",views.account_analysis_summary_widget,name="account_analysis_summary_widget"),
]

router.register('projects', ProjectsAccountAnalysisViewSet)

urlpatterns += router.urls