from uuid import uuid4


class ProjectPDF:
    def __init__(self, item, format, template_path):
        self.item = item
        self.format = format
        self.layout_file = template_path

    docx_path = f'tmp/temp_reg_report_{str(uuid4())}.docx'
    report_path = f'tmp/temp_reg_report_{str(uuid4())}.{format}'
