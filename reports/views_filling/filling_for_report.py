from .filling_summary_widget import summarry_widget_image
from .filling_volume_widget import volume_widget_image
from .filling_top_10_authors_by_volume_widget import top_10_authors_by_volume_widget_image
from .filling_top_10_sources_widget import top_10_sources_widget_image
from .filling_top_10_countries_widget import top_10_countries_widget_image
from .filling_top_10_languages_widget import top_10_languages_widget_image
from .filling_sentiment_top_10_sources_widget import sentiment_top_10_sources_widget_image
from .filling_sentiment_top_10_authors_widget import sentiment_top_10_authors_widget_image
from .filling_sentiment_top_10_countries_widget import sentiment_top_10_countries_widget_image
from .filling_sentiment_top_10_languages_widget import sentiment_top_10_languages_widget_image
from .filling_sentiment_for_period_widget import sentiment_for_period_widget_image
from .filling_content_volume_top_10_source_widget import content_volume_top_10_source_widget_image
from .filling_content_volume_top_10_authors_widget import content_volume_top_10_authors_widget_image
from .filling_content_volume_top_10_countries_widget import content_volume_top_10_countries_widget_image
from reports.models import Templates
from .options import *

def export_title(project_id):
  proj = get_object_or_404(Project, pk=project_id)
  title = proj.title
  return title

def export_period(project_id):
  proj = get_object_or_404(Project, pk=project_id)
  start_d = str(proj.start_search_date.ctime())
  end_d = str(proj.end_search_date.ctime())
  period = start_d + ' - ' + end_d
  return period

def filling_templates_for_instant_and_regular_reports(document, project_id):
  tbls = document.tables
  for t in tbls:
    for row in t.rows:
      for cell in row.cells:
        for p in cell.paragraphs:
          if '$EXPORT_TITLE$' in p.text:
            p.text = p.text.replace('$EXPORT_TITLE$', export_title(project_id))
          if '$EXPORT_PERIOD$' in p.text:
            p.text = p.text.replace('$EXPORT_PERIOD$', export_period(project_id))
          if '$EXPORT_TOC$' in p.text:
            proj = WidgetsList2.objects.get(project_id=project_id)
            p.text = p.text.replace('$EXPORT_TOC$',' ')
            if proj.summary_widget.is_active:
              cell.add_paragraph('Report Summary', style='pTOC1')
              cell.add_paragraph('Summary', style='pTOC2')
            if proj.volume_widget.is_active or proj.top_10_authors_by_volume_widget.is_active or proj.top_10_brands_widget.is_active or proj.top_10_countries_widget.is_active or proj.top_10_languages_widget.is_active:
              cell.add_paragraph('Potential Reach', style='pTOC1')
              if proj.volume_widget.is_active:
                cell.add_paragraph(proj.volume_widget.title + ' (per ' + proj.volume_widget.aggregation_period + ')', style='pTOC2')
              if proj.top_10_authors_by_volume_widget.is_active:
                cell.add_paragraph(proj.top_10_authors_by_volume_widget.title + ' (per ' + proj.top_10_authors_by_volume_widget.aggregation_period + ')', style='pTOC2')
              if proj.top_10_brands_widget.is_active:
                cell.add_paragraph(proj.top_10_brands_widget.title + ' (per ' + proj.top_10_brands_widget.aggregation_period + ')', style='pTOC2')
              if proj.top_10_countries_widget.is_active:
                cell.add_paragraph(proj.top_10_countries_widget.title + ' (per ' + proj.top_10_countries_widget.aggregation_period + ')', style='pTOC2')
              if proj.top_10_languages_widget.is_active:
                cell.add_paragraph(proj.top_10_languages_widget.title + ' (per ' + proj.top_10_languages_widget.aggregation_period + ')', style='pTOC2')
            if proj.sentiment_top_10_sources_widget.is_active or proj.sentiment_top_10_authors_widget.is_active or proj.sentiment_top_10_countries_widget.is_active or proj.sentiment_top_10_languages_widget.is_active or proj.sentiment_for_period_widget.is_active:
              cell.add_paragraph('Sentiment Distribution', style='pTOC1')
              if proj.sentiment_top_10_sources_widget.is_active:
                cell.add_paragraph(proj.sentiment_top_10_sources_widget.title, style='pTOC2')
              if proj.sentiment_top_10_authors_widget.is_active:
                cell.add_paragraph(proj.sentiment_top_10_authors_widget.title, style='pTOC2')
              if proj.sentiment_top_10_countries_widget.is_active:
                cell.add_paragraph(proj.sentiment_top_10_countries_widget.title, style='pTOC2')   
              if proj.sentiment_top_10_languages_widget.is_active:
                cell.add_paragraph(proj.sentiment_top_10_languages_widget.title, style='pTOC2')
              if proj.sentiment_for_period_widget.is_active:
                cell.add_paragraph(proj.sentiment_for_period_widget.title, style='pTOC2')     
            if proj.content_volume_top_10_source_widget.is_active or proj.content_volume_top_10_authors_widget.is_active:
              cell.add_paragraph('Content Volume', style='pTOC1')
              if proj.content_volume_top_10_source_widget.is_active:
                cell.add_paragraph(proj.content_volume_top_10_source_widget.title, style='pTOC2')
              if proj.content_volume_top_10_authors_widget.is_active:
                cell.add_paragraph(proj.content_volume_top_10_authors_widget.title, style='pTOC2')
              if proj.content_volume_top_10_countries_widget.is_active:
                cell.add_paragraph(proj.content_volume_top_10_countries_widget.title, style='pTOC2')                          
            if proj.clipping_feed_content_widget.is_active:
              cell.add_paragraph(proj.clipping_feed_content_widget.title, style='pTOC1')
              cell.add_paragraph('Description: ' + proj.clipping_feed_content_widget.aggregation_period, style='pTOC2')   

  summarry_widget_image(document, proj)
  def new_section(name_section):
    document.add_page_break() 
    p3 = document.add_paragraph('', style='pExportCoverPageValue')
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), '575756')
    p3.paragraph_format.element.get_or_add_pPr()
    p3.paragraph_format.element.pPr.append(shd)
    p3 = p3.add_run(name_section)
    p3.font.size = Pt(18)
    document.add_paragraph('', style='pTableHeaderLeft')

  if proj.volume_widget.is_active or proj.top_10_authors_by_volume_widget.is_active or proj.top_10_brands_widget.is_active or proj.top_10_countries_widget.is_active or proj.top_10_languages_widget.is_active:
    new_section(' Volume and Potential Reach')

  volume_widget_image(document, proj)
  top_10_authors_by_volume_widget_image(document, proj)
  top_10_sources_widget_image(document, proj)
  top_10_countries_widget_image(document, proj)
  top_10_languages_widget_image(document, proj)

  if proj.volume_widget.is_active or proj.top_10_authors_by_volume_widget.is_active or proj.top_10_brands_widget.is_active or proj.top_10_countries_widget.is_active or proj.top_10_languages_widget.is_active:
    new_section(' Sentiment Distribution')

  sentiment_top_10_sources_widget_image(document, proj)
  sentiment_top_10_authors_widget_image(document, proj)
  sentiment_top_10_countries_widget_image(document, proj)
  sentiment_top_10_languages_widget_image(document, proj)
  sentiment_for_period_widget_image(document, proj)

  if proj.content_volume_top_10_source_widget.is_active or proj.content_volume_top_10_authors_widget.is_active or proj.content_volume_top_10_countries_widget.is_active:
    new_section(' Content Volume')

  content_volume_top_10_source_widget_image(document, proj)
  content_volume_top_10_authors_widget_image(document, proj)
  content_volume_top_10_countries_widget_image(document, proj)

  if proj.clipping_feed_content_widget.is_active:
    new_section(' Clippings: Sample Articles')

    posts = ClippingFeedContentWidget.objects.filter(project_id=project_id).values(
        'post__entry_title',
        'post__entry_summary',
        'post__entry_published',
        'post__entry_author',
        'post__feedlink__country',
        'post__sentiment',
        )
    for each in posts:
        p = document.add_paragraph(each['post__entry_title'], style='pTableHeaderLeft')
        shd = OxmlElement('w:shd')
        shd.set(qn('w:val'), 'clear')
        shd.set(qn('w:color'), 'auto')
        shd.set(qn('w:fill'), '575756')
        p.paragraph_format.element.get_or_add_pPr()
        p.paragraph_format.element.pPr.append(shd)
        document.add_paragraph(each['post__entry_summary'], style='pPostContent')
        table = document.add_table(rows=2, cols=4)
        for row in table.rows:
            for cell in row.cells:
                shade_obj = OxmlElement('w:shd')
                shade_obj.set(qn('w:fill'), "#ebebeb")
                cell._tc.get_or_add_tcPr().append(shade_obj)# set silver background color
        heading_cells = table.rows[0].cells
        heading_cells[0].add_paragraph('Published:', style='pPropertyLabel')
        heading_cells[1].add_paragraph('Author:', style='pPropertyLabel')
        heading_cells[2].add_paragraph('Country:', style='pPropertyLabel')
        heading_cells[3].add_paragraph('Sentiment:', style='pPropertyLabel')
        sec_row = table.rows[1].cells
        sec_row[0].add_paragraph(each['post__entry_published'].strftime("%c"), style='pPropertyValue')
        sec_row[1].add_paragraph(each['post__entry_author'], style='pPropertyValue')
        sec_row[2].add_paragraph(each['post__feedlink__country'], style='pPropertyValue')
        sec_row[3].add_paragraph(each['post__sentiment'], style='pPropertyValue')
        document.add_paragraph('', style='pTableHeaderLeft')     
  return document
