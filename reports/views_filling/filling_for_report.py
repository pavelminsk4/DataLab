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
from .filling_content_volume_top_5_source_widget import content_volume_top_5_source_widget_image
from .filling_content_volume_top_5_authors_widget import content_volume_top_5_authors_widget_image
from .filling_content_volume_top_5_countries_widget import content_volume_top_5_countries_widget_image
from docx.shared import Pt, Inches
from .options import *
from django.shortcuts import get_object_or_404
from docx.oxml.shared import OxmlElement
from docx.oxml.ns import qn

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

def font_one(run, cell):
  font = run.font
  font.bold = True
  font.size = Pt(15)
  para = cell.add_paragraph()
  para.paragraph_format.line_spacing = Inches(0.1)

def font_two(run, cell):
  font = run.font
  font.size = Pt(11) 
  para = cell.add_paragraph()
  para.paragraph_format.line_spacing = Inches(0.1)

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
              run = cell.add_paragraph('').add_run('Report Summary')
              font_one(run, cell)
              run = cell.add_paragraph().add_run('Summary')
              font_two(run, cell)
              cell.add_paragraph()
            if proj.volume_widget.is_active or proj.top_10_authors_by_volume_widget.is_active or proj.top_10_brands_widget.is_active or proj.top_10_countries_widget.is_active or proj.top_10_languages_widget.is_active:
              run = cell.add_paragraph('').add_run('Potential Reach')
              font_one(run, cell)
              if proj.volume_widget.is_active:
                run = cell.add_paragraph().add_run(proj.volume_widget.title + ' (per ' + proj.volume_widget.aggregation_period + ')')
                font_two(run, cell)
              if proj.top_10_authors_by_volume_widget.is_active:
                run = cell.add_paragraph().add_run(proj.top_10_authors_by_volume_widget.title + ' (per ' + proj.top_10_authors_by_volume_widget.aggregation_period + ')')
                font_two(run, cell)
              if proj.top_10_brands_widget.is_active:
                run = cell.add_paragraph().add_run(proj.top_10_brands_widget.title + ' (per ' + proj.top_10_brands_widget.aggregation_period + ')')
                font_two(run, cell)
              if proj.top_10_countries_widget.is_active:
                run = cell.add_paragraph().add_run(proj.top_10_countries_widget.title + ' (per ' + proj.top_10_countries_widget.aggregation_period + ')')
                font_two(run, cell)
              if proj.top_10_languages_widget.is_active:
                run = cell.add_paragraph().add_run(proj.top_10_languages_widget.title + ' (per ' + proj.top_10_languages_widget.aggregation_period + ')')
                font_two(run, cell)
              cell.add_paragraph()  
            if proj.sentiment_top_10_sources_widget.is_active or proj.sentiment_top_10_authors_widget.is_active or proj.sentiment_top_10_countries_widget.is_active or proj.sentiment_top_10_languages_widget.is_active or proj.sentiment_for_period_widget.is_active:
              run = cell.add_paragraph().add_run('Sentiment Distribution')
              font_one(run, cell)
              if proj.sentiment_top_10_sources_widget.is_active:
                run = cell.add_paragraph().add_run(proj.sentiment_top_10_sources_widget.title)
                font_two(run, cell)
              if proj.sentiment_top_10_authors_widget.is_active:
                run = cell.add_paragraph().add_run(proj.sentiment_top_10_authors_widget.title)
                font_two(run, cell)
              if proj.sentiment_top_10_countries_widget.is_active:
                run = cell.add_paragraph().add_run(proj.sentiment_top_10_countries_widget.title)
                font_two(run, cell)
              if proj.sentiment_top_10_languages_widget.is_active:
                run = cell.add_paragraph().add_run(proj.sentiment_top_10_languages_widget.title)
                font_two(run, cell)
              if proj.sentiment_for_period_widget.is_active:
                run = cell.add_paragraph().add_run(proj.sentiment_for_period_widget.title)
                font_two(run, cell)
                cell.add_paragraph()
            if proj.content_volume_top_5_source_widget.is_active or proj.content_volume_top_5_authors_widget.is_active:
              run = cell.add_paragraph().add_run('Content Volume')
              font_one(run, cell)
              if proj.content_volume_top_5_source_widget.is_active:
                run = cell.add_paragraph().add_run(proj.content_volume_top_5_source_widget.title)
                font_two(run, cell)
              if proj.content_volume_top_5_authors_widget.is_active:
                run = cell.add_paragraph().add_run(proj.content_volume_top_5_authors_widget.title)
                font_two(run, cell)
              if proj.content_volume_top_5_countries_widget.is_active:
                run = cell.add_paragraph().add_run(proj.content_volume_top_5_countries_widget.title)
                font_two(run, cell)
              cell.add_paragraph()  
            if proj.clipping_feed_content_widget.is_active:
              run = cell.add_paragraph().add_run('Clippings: Sample Articles')
              font_one(run, cell)

  def new_section(name_section):
    p3 = document.add_paragraph()
    p = p3._p  # p is the <w:p> XML element
    pPr = p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    pPr.insert_element_before(pBdr,
        'w:shd', 'w:tabs', 'w:suppressAutoHyphens', 'w:kinsoku', 'w:wordWrap',
        'w:overflowPunct', 'w:topLinePunct', 'w:autoSpaceDE', 'w:autoSpaceDN',
        'w:bidi', 'w:adjustRightInd', 'w:snapToGrid', 'w:spacing', 'w:ind',
        'w:contextualSpacing', 'w:mirrorIndents', 'w:suppressOverlap', 'w:jc',
        'w:textDirection', 'w:textAlignment', 'w:textboxTightWrap',
        'w:outlineLvl', 'w:divId', 'w:cnfStyle', 'w:rPr', 'w:sectPr',
        'w:pPrChange'
    )
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '10')
    bottom.set(qn('w:space'), '1')
    bottom.set(qn('w:color'), '055FFC')
    pBdr.append(bottom)
    p3 = p3.add_run(name_section)
    p3.font.size = Pt(20)
    document.add_paragraph()

  if proj.summary_widget.is_active:
    new_section('Report Summary')
    summarry_widget_image(document, proj)
    document.add_page_break()

  if proj.volume_widget.is_active or proj.content_volume_top_5_source_widget.is_active or proj.content_volume_top_5_authors_widget.is_active or proj.content_volume_top_5_countries_widget.is_active:
    new_section('Content Volume')
    volume_widget_image(document, proj)
    content_volume_top_5_source_widget_image(document, proj)
    content_volume_top_5_authors_widget_image(document, proj)
    content_volume_top_5_countries_widget_image(document, proj)
    document.add_page_break()
  
  if proj.top_10_authors_by_volume_widget.is_active or proj.top_10_brands_widget.is_active or proj.top_10_countries_widget.is_active or proj.top_10_languages_widget.is_active:
    new_section('Top 10')
    top_10_authors_by_volume_widget_image(document, proj)
    top_10_sources_widget_image(document, proj)
    top_10_countries_widget_image(document, proj)
    top_10_languages_widget_image(document, proj)
    document.add_page_break()

  if proj.volume_widget.is_active or proj.top_10_authors_by_volume_widget.is_active or proj.top_10_brands_widget.is_active or proj.top_10_countries_widget.is_active or proj.top_10_languages_widget.is_active:
    new_section('Sentiment Top 10')
    sentiment_top_10_sources_widget_image(document, proj)
    sentiment_top_10_authors_widget_image(document, proj)
    sentiment_top_10_countries_widget_image(document, proj)
    sentiment_top_10_languages_widget_image(document, proj)
    document.add_paragraph()
    document.add_paragraph()
    sentiment_for_period_widget_image(document, proj)
    document.add_page_break()

  if proj.clipping_feed_content_widget.is_active:
    new_section('Clippings: Sample Articles')
    posts = ClippingFeedContentWidget.objects.filter(project_id=project_id).values(
        'post__entry_title',
        'post__feed_language__language',
        'post__feedlink__alexaglobalrank',
        'post__sentiment',
        'post__feedlink__source1',
        'post__feedlink__country',
        'post__entry_published',
        'post__entry_summary',
        )
    for each in posts:
      title = document.add_table(rows=1, cols=1)
      for row in title.rows:
        for cell in row.cells:
          shade_obj = OxmlElement('w:shd')
          shade_obj.set(qn('w:fill'), "#c7cacc")
          cell._tc.get_or_add_tcPr().append(shade_obj)# set silver background color
      heading_cells = title.rows[0].cells
      run = heading_cells[0].add_paragraph().add_run(each['post__entry_title'])
      run.font.size = Pt(11)
      document.add_paragraph(each['post__entry_summary'], style='pPostContent')  
      table = document.add_table(rows=4, cols=5)
      count = 0
      for row in table.rows:
        if count == 0:
          for cell in row.cells:
            shade_obj = OxmlElement('w:shd')
            shade_obj.set(qn('w:fill'), "#f0f1f2")
            cell._tc.get_or_add_tcPr().append(shade_obj)# set silver background color
            count += 1
        else:
          for cell in row.cells:
            shade_obj = OxmlElement('w:shd')
            shade_obj.set(qn('w:fill'), "#ffffff")
            cell._tc.get_or_add_tcPr().append(shade_obj)# set silver background color
            count = 0               

      heading_cells = table.rows[0].cells
      heading_cells[0].add_paragraph('Media Channel')
      heading_cells[1].add_paragraph('Language')
      heading_cells[2].add_paragraph('Potential reach')
      heading_cells[3].add_paragraph('Sentiment')
      heading_cells[4].add_paragraph('Source')
      sec_row = table.rows[1].cells
      sec_row[0].add_paragraph('Online')
      sec_row[1].add_paragraph(each['post__feed_language__language'])
      sec_row[2].add_paragraph(str(each['post__feedlink__alexaglobalrank']))
      sec_row[3].add_paragraph(each['post__sentiment'])
      sec_row[4].add_paragraph(each['post__feedlink__source1'])
      heading_cells = table.rows[2].cells
      heading_cells[0].add_paragraph('Source country')
      heading_cells[1].add_paragraph('Domestic Rank')
      heading_cells[2].add_paragraph('Global Rank')
      heading_cells[3].add_paragraph('Date')
      sec_row = table.rows[3].cells
      sec_row[0].add_paragraph(each['post__feedlink__country'])
      sec_row[1].add_paragraph('1')
      sec_row[2].add_paragraph('1')
      sec_row[3].add_paragraph(each['post__entry_published'].strftime("%d.%m.%Y"))
      document.add_paragraph()
      document.add_paragraph()   
  return document
