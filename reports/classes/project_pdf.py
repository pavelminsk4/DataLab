from uuid import uuid4


class ProjectPDF:
    def __init__(self, item, format, template_path):
        self.item = item
        self.report_path = f'tmp/temp_reg_report_{uuid4()}.{format}'
        self.template_path = template_path

    docx_path = f'tmp/temp_reg_report_{uuid4()}.docx'
