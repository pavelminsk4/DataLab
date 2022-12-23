from django.http import FileResponse
from widgets.models import ClippingFeedContentWidget
from project.models import Project
from widgets.models import WidgetsList2
from django.shortcuts import get_object_or_404
from docx import Document
from docx.shared import Inches, Pt
from reports.chartjs.chartjs import prepare_widget_images
import aspose.words as aw

from docx.shared import Pt
from docx.oxml.ns import qn
from docx.oxml.shared import OxmlElement

from reports.serializers import RegularReportSerializer
from reports.models import RegularReport
from rest_framework import viewsets
