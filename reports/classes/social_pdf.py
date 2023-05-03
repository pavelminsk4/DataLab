from .project_pdf import Project_PDF
from reports.social_chartjs.social_chartjs import prepare_social_widget_images
from reports.social_views_filling.filling_for_social_report import filling_templates_for_social_reports
from docx import Document
from reports.services.pdf_handler import convert_docx_to_pdf

class Social_PDF(Project_PDF):
    def generate(self):
        screenshots_list = prepare_social_widget_images(self.item)
        document = Document(self.template_path)
        document = filling_templates_for_social_reports(
            document, self.item, screenshots_list)
        document.save(self.docx_path)
        convert_docx_to_pdf(self.docx_path, self.report_path)
        return self.report_path
