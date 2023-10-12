from widgets.common_widget.filters_for_widgets import post_agregetor_for_each_widget
from widgets.common_widget.filters_for_widgets import posts_with_filters
from widgets.models import WidgetDescription
from project.models import Project
import environ

env = environ.Env()


def project_posts_filter(pk, widget_pk):
    project = Project.objects.get(id=pk)
    posts = project.posts
    posts = posts_with_filters(project, posts)
    widget = WidgetDescription.objects.get(id=widget_pk)
    posts = post_agregetor_for_each_widget(widget, posts)
    return posts, widget
