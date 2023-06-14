from widgets.common_widget.filters_for_widgets import post_agregator_with_dimensions
from widgets.common_widget.summary import calculate_summary_widget
from project_social.models import ProjectSocial
from project.models import Project


class SummaryFactory:
    def __init__(self, item):
        self.item = item

    def define(self):
        if self.item.module_type == 'Project':
            return SummaryOnline(Project.objects.get(id=self.item.module_project_id))
        else:
            return SummarySocial(ProjectSocial.objects.get(id=self.item.module_project_id))


class SummaryOnline:
    def __init__(self, project):
        self.posts = post_agregator_with_dimensions(project)
        self.project = project

    def get_widgets(self):
        return {
            self.project.title: {'Summary': calculate_summary_widget(self.posts)}
        }


class SummarySocial:
    def get_widgets(self):
        pass
