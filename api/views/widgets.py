from api.services.widgets_dict import widgets, social_widgets, account_analysis_widgets
from account_analysis.models import AccountAnalysisWidgetDescription
from project_social.models import SocialWidgetDescription 
from widgets.models import WidgetDescription
from django.http import HttpResponse
import csv


def get_csv_online(request, project_pk, widget_pk):
    return CSV(request, project_pk, widget_pk, widgets, WidgetDescription).get()

def get_csv_social(request, project_pk, widget_pk):
    return CSV(request, project_pk, widget_pk, social_widgets, SocialWidgetDescription).get()

def get_csv_acc_analysis(request, project_pk, widget_pk):
    return CSV(request, project_pk, widget_pk, account_analysis_widgets, AccountAnalysisWidgetDescription).get()
    
class CSV:
    def __init__(self, request, project_pk, widget_pk, widgets, widget_description):
        self.request = request
        self.project_pk = project_pk
        self.widget_pk = widget_pk
        self.widgets = widgets
        self.widget_description = widget_description

    def get(self):
        w = self.widget_description.objects.get(id=self.widget_pk)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{w.default_title}.csv"'
        writer = csv.writer(response)
        fields, rows = self.widgets[w.default_title].to_csv(self.request, self.project_pk, self.widget_pk)
        writer.writerow(fields)
        for elem in rows:
            writer.writerow(elem)
        return response
