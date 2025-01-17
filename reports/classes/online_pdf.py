from reports.services.pdf_handler import convert_docx_to_pdf
from reports.classes.report_document import ReportDocument
from reports.classes.screen_driver import ScreenDriver
from project.models import Project
from .project_pdf import ProjectPDF
from docx import Document


class OnlinePDF(ProjectPDF):
    def generate(self):
        screenshots_list = ScreenDriver(self.item).screenshots()
        document = Document(self.template_path)
        document = ReportDocument(document, self.item, screenshots_list, Project, 'widgets_list_2').fill()
        document.save(self.docx_path)
        convert_docx_to_pdf(self.docx_path, self.report_path)
        return self.report_path
