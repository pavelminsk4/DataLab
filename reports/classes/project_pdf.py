from .online_pdf import Online_PDF
from .social_pdf import Social_PDF
from uuid import uuid4


class Project_PDF:
    def __init__(self, item, format, template_path):
        self.item = item
        self.format = format
        self.layout_file = template_path

    docx_path = 'tmp/temp_reg_report_' + str(uuid4()) + '.docx'
    report_path = 'tmp/temp_reg_report_' + str(uuid4()) + '.' + format


class Factory_PDF:
    def __init__(self, item, format, template_path):
        self.item = item
        self.format = format
        self.layout_file = template_path

    def define(self):
        if self.item.module_type == 'Project':
            return Online_PDF(self.item, self.format, self.layout_file)
        else:
            return Social_PDF(self.item, self.format, self.layout_file)
