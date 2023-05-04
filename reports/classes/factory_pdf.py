from .online_pdf import OnlinePDF
from .social_pdf import SocialPDF


class FactoryPDF:
    def __init__(self, item, format, template_path):
        self.item = item
        self.format = format
        self.layout_file = template_path

    def define(self):
        if self.item.module_type == 'Project':
            return OnlinePDF(self.item, self.format, self.layout_file)
        else:
            return SocialPDF(self.item, self.format, self.layout_file)
