from widgets.common_widget.summary import *
from project.models import *
from quickchart import QuickChart
import json

def create_summary_widget_image(project_id, widget_pk):
  from PIL import Image, ImageDraw, ImageFont
  res = summary_widget(project_id, widget_pk)
  res = json.loads(res.content)
  # Open an Image
  img = Image.open('tmp/mask.png')
  # Call draw Method to add 2D graphics in an image
  I1 = ImageDraw.Draw(img)
  myFont = ImageFont.truetype('DejaVuSerif-Bold.ttf', 18)
  # Add Text to an image
  I1.text((20, 53), str(res['posts']), font=myFont, fill=(0, 0, 0))
  I1.text((155, 53), str(res['neut']), font=myFont, fill=(0, 0, 0))
  I1.text((290, 53), str(res['neg']), font=myFont, fill=(0, 0, 0))
  I1.text((425, 53), str(res['pos']), font=myFont, fill=(0, 0, 0))
  I1.text((20, 163), str(res['sources']), font=myFont, fill=(0, 0, 0))
  I1.text((155, 170), str(res['reach']), font=ImageFont.truetype('DejaVuSerif-Bold.ttf', 12), fill=(0, 0, 0))
  I1.text((290, 163), str(res['countries']), font=myFont, fill=(0, 0, 0))
  I1.text((425, 163), str(res['authors']), font=myFont, fill=(0, 0, 0))


  img.save("tmp/summary_widget.png")
