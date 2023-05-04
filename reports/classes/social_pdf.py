from reports.classes.project_pdf import ProjectPDF
from reports.social_views_filling.filling_for_social_report import filling_templates_for_social_reports
from docx import Document
from reports.services.pdf_handler import convert_docx_to_pdf
from reports.classes.screen_driver import ScreenDriver

class SocialPDF(ProjectPDF):
    def generate(self):
        screenshots_list = ScreenDriver(self.item).get_screenshots()
        document = Document(self.template_path)
        document = filling_templates_for_social_reports(
            document, self.item, screenshots_list)
        document.save(self.docx_path)
        convert_docx_to_pdf(self.docx_path, self.report_path)
        return self.report_path
