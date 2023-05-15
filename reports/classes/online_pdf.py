from .project_pdf import ProjectPDF
from docx import Document
from reports.chartjs.chartjs import prepare_widget_images_for_regular
from reports.views_filling.filling_for_report import filling_templates_for_instant_and_regular_reports
from reports.services.pdf_handler import convert_docx_to_pdf

class OnlinePDF(ProjectPDF):
    def generate(self):
        prepare_widget_images_for_regular(self.item)
        document = Document(self.template_path)
        document = filling_templates_for_instant_and_regular_reports(
            document, self.item.module_project_id)
        document.save(self.docx_path)
        convert_docx_to_pdf(self.docx_path, self.report_path)
        return self.report_path
