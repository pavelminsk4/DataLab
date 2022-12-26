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

def widget_image(document, title_widget, widget_image):
    p4 = document.add_paragraph(title_widget, style='pTableHeaderLeft')
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), '575756')
    p4.paragraph_format.element.get_or_add_pPr()
    p4.paragraph_format.element.pPr.append(shd)
    document.add_paragraph('', style='pTableHeaderLeft')
    document.add_picture(widget_image, width=Inches(6.6))
    document.add_paragraph('', style='pTableHeaderLeft')
