from widgets.common_widget.filters_for_widgets import post_agregator_with_dimensions
from widgets.common_widget.filters_for_widgets import post_agregetor_for_each_widget
from widgets.models import WidgetDescription
from project.models import Project

def project_posts_filter(pk, widget_pk):
    project = Project.objects.get(id=pk)
    posts = post_agregator_with_dimensions(project)
    widget = WidgetDescription.objects.get(id=widget_pk)
    posts = post_agregetor_for_each_widget(widget, posts)
    return posts, widget
