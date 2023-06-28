from docx.shared import Pt, Inches
from project_social.models import ProjectSocial


class ReportDocument:
    def __init__(self, document, item, screenshot_list):
        self.document = document
        self.item = item
        self.screenshot_list = screenshot_list
        self.project = ProjectSocial.objects.get(id=item.module_project_id)
        self.widget_list = self.project.social_widgets_list

    def fill(self):
        self.__foreach_paragraph(self.__fill_introduction)
        self.__fill_content()
        return self.document

    def __font_one(self, run, cell):
        font = run.font
        font.bold = True
        font.size = Pt(15)
        para = cell.add_paragraph()
        para.paragraph_format.line_spacing = Inches(0.1)

    def __font_two(self, run, cell):
        font = run.font
        font.size = Pt(11)
        para = cell.add_paragraph()
        para.paragraph_format.line_spacing = Inches(0.1)

    def __export_period(self):
        start_d = str(self.project.start_search_date.ctime())
        end_d = str(self.project.end_search_date.ctime())
        period = f'{start_d} - {end_d}'
        return period

    def __foreach_paragraph(self, func):
        tbls = self.document.tables
        for t in tbls:
            for row in t.rows:
                for cell in row.cells:
                    for p in cell.paragraphs:
                        func(p, cell)

    def __fill_titular(self, p, cell):
        if '$EXPORT_TITLE$' in p.text:
            p.text = p.text.replace('$EXPORT_TITLE$', self.project.title)
        if '$EXPORT_PERIOD$' in p.text:
            p.text = p.text.replace('$EXPORT_PERIOD$', self.__export_period())

    def __fill_table_of_contents(self, p, cell):
        if '$EXPORT_TOC$' in p.text:
            p.text = p.text.replace('$EXPORT_TOC$', ' ')
            self.__fill_summary_section(p, cell)
            self.__fill_potential_reach_section(p, cell)
            self.__fill_sentiment_section(p, cell)

    def __fill_summary_section(self, p, cell):
        if self.item.soc_summary:
            self.__font_one(cell.add_paragraph('').add_run('Report Summary'), cell)
            self.__font_two(cell.add_paragraph().add_run('Summary'), cell)
            cell.add_paragraph()

    def __fill_potential_reach_section(self, p, cell):
        if (self.item.soc_content_volume or
            self.item.soc_content_volume_top_locations or
            self.item.soc_content_volume_top_authors or
                self.item.soc_content_volume_top_languages):
            self.__font_one(cell.add_paragraph(
                '').add_run('Content Volume'), cell)
            if self.item.soc_content_volume:
                self.__font_two(self.__get_widget_title(cell, self.widget_list.content_volume, True), cell)
            if self.item.soc_content_volume_top_locations:
                self.__font_two(self.__get_widget_title(cell, self.widget_list.content_volume_top_locations, True), cell)
            if self.item.soc_content_volume_top_authors:
                self.__font_two(self.__get_widget_title(cell, self.widget_list.content_volume_top_authors, True), cell)
            if self.item.soc_content_volume_top_languages:
                self.__font_two(self.__get_widget_title(cell, self.widget_list.content_volume_top_languages, True), cell)
            cell.add_paragraph()

    def __fill_sentiment_section(self, p, cell):
        if (self.item.soc_sentiment_diagram):
            self.__font_one(cell.add_paragraph(
                '').add_run('Sentiment'), cell)
            if self.item.soc_sentiment_diagram:
                self.__font_two(self.__get_widget_title(cell, self.widget_list.sentiment_diagram, True), cell)
            cell.add_paragraph()

    def __get_widget_title(self, cell, widget, have_period):
        return cell.add_paragraph().add_run(f"{widget.title}{f' (per {widget.aggregation_period})' if have_period else ''}")

    def __fill_content(self):
        if self.item.soc_top_locations:
            self.__get_widget_image(self.screenshot_list['soc_top_locations'], 'Top Locations')
        if self.item.soc_top_authors:
            self.__get_widget_image(self.screenshot_list['soc_top_authors'], 'Top Authors')
        if self.item.soc_top_languages:
            self.__get_widget_image(self.screenshot_list['soc_top_languages'], 'Top Languages')
        if self.item.soc_sentiment_diagram:
            self.__get_widget_image(self.screenshot_list['soc_sentiment_diagram'], 'Sentiment diagram')

    def __get_widget_image(self, widget_image, title_widget):
        # self.document.add_paragraph()
        # p = self.document.add_paragraph().add_run(title_widget)
        # p.font.size = Pt(13)
        # self.document.add_paragraph()
        self.document.add_picture(widget_image, width=Inches(6.6))
        self.document.add_paragraph()
        self.document.add_paragraph()
        self.document.add_paragraph()
        self.document.add_page_break()

    def __fill_introduction(self, p, cell):
        self.__fill_titular(p, cell)
        self.__fill_table_of_contents(p, cell)
