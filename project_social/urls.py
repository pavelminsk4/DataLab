from rest_framework import routers
from project_social import views
from django.urls import path
from .models import *
from .views import *

app_name = 'project_social'

router = routers.SimpleRouter()

urlpatterns = [
  #========Workspaces and Progects=========  
  path("social_workspaces/",views.WorkspaceSocialList.as_view(),name="social_workspaces_list"),
  path("social_workspaces/create/", views.WorkspaceSocialCreate.as_view(),name="social_workspaces_create"),
  path("social_workspaces/update/<int:pk>/",views.WorkspaceSocialUpdate.as_view(),name="social_workspaces_update"),
  path("social_workspaces/delete/<int:pk>/",views.WorkspaceSocialDelete.as_view(),name="social_workspaces_delete"),
  path("twitter_post_search/", views.twitter_posts_search,name="twitter_posts_search"),
  #========Widgets========
  path('social_summary_widget/<int:pk>/<int:widget_pk>', views.social_summary_widget, name='social_summary_widget'),
  path('social_clipping_feed_content/<int:pk>/<int:widget_pk>', views.clipping_feed_content, name='social_clipping_feed_content'),
  path('social_top_locations/<int:pk>/<int:widget_pk>', views.social_top_locations, name='social_top_locations'),
  path('social_top_languages/<int:pk>/<int:widget_pk>', views.social_top_languages, name='social_top_languages'),
  path('social_top_authors/<int:pk>/<int:widget_pk>', views.social_top_authors, name='social_top_authors'),
  path('social_content_volume/<int:pk>/<int:widget_pk>', views.social_content_volume, name='social_content_volume'),
  path('social_content_volume_by_top_locations/<int:pk>/<int:widget_pk>', views.social_content_volume_by_top_locations, name='social_content_volume_by_top_locations'),
  path('social_content_volume_by_top_authors/<int:pk>/<int:widget_pk>', views.social_content_volume_by_top_authors, name='social_content_volume_by_top_authors'),
  path('social_content_volume_by_top_languages/<int:pk>/<int:widget_pk>', views.social_content_volume_by_top_languages, name='social_content_volume_by_top_languages'),
  path('social_sentiment/<int:pk>/<int:widget_pk>', views.social_sentiment, name='social_sentiment'),
  path('social_sentiment_authors/<int:pk>/<int:widget_pk>', views.social_sentiment_authors, name='social_sentiment_authors'),
  path('social_sentiment_languages/<int:pk>/<int:widget_pk>', views.social_sentiment_languages, name='social_sentiment_languages'),
  path('social_sentiment_locations/<int:pk>/<int:widget_pk>', views.social_sentiment_locations, name='social_sentiment_locations'),
  path('social_sentiment_by_gender/<int:pk>/<int:widget_pk>', views.social_sentiment_by_gender, name='social_sentiment_by_gender'),
  path('social_gender_volume/<int:pk>/<int:widget_pk>', views.social_gender_volume, name='social_gender_volume'),
  path('social_top_keywords/<int:pk>/<int:widget_pk>', views.social_top_keywords, name='social_top_keywords'),
  path('social_top_sharing_sources/<int:pk>/<int:widget_pk>', views.social_top_sharing_sources, name='social_top_sharing_sources'),
  path('social_sentiment_top_keywords/<int:pk>/<int:widget_pk>', views.social_sentiment_top_keywords, name='social_sentiment_top_keywords'), 
  path('social_sentiment_number_of_results/<int:pk>/<int:widget_pk>', views.social_sentiment_number_of_results, name='social_sentiment_number_of_results'), 
  path('social_sentiment_diagram/<int:pk>/<int:widget_pk>', views.social_sentiment_diagram, name='social_sentiment_diagram'),  
  path('dimensions_for_each_widgets/<int:project_pk>/<int:widget_pk>', views.dimensions_for_each_widgets, name='dimensions_for_each_widgets'),
  #========Widgets List========
  path('projects/<int:pk>/widgets_list', views.ProjectSocialWidgetsAPIView.as_view(), name='social_widgets_list'),
  path('projects/<int:pk>/widgets_list/update', views.UpdateSocialProjectsWidgetsAPIView.as_view(), name='update_social_widgets_list'),
  #========Filter=========
  path('social_authors_list', views.SocialAuthorList.as_view(), name='social_authors_list'),
  path('social_locations_list', views.SocialLocationList.as_view(), name='social_locations_list'),
  path('social_languages_list', views.SocialLanguageList.as_view(), name='social_languages_list'),
]

router.register('projects', ProjectsSotialViewSet)
router.register('social_clipping_feed_content', SocialClippingWidget)

urlpatterns += router.urls
