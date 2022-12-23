from widgets.common_widget.summary_widget import *
from project.models import *
from quickchart import QuickChart

def create_summary_widget_image(project_id):
  from PIL import Image
  from PIL import ImageDraw
  from PIL import ImageFont
  res = calculate_summary_widget(project_id)
  # Open an Image
  img = Image.open('tmp/mask.png')
  # Call draw Method to add 2D graphics in an image
  I1 = ImageDraw.Draw(img)
  myFont = ImageFont.truetype('DejaVuSerif-Bold.ttf', 20)
  # Add Text to an image
  I1.text((105, 63), str(res['languages']), font=myFont, fill=(255, 255, 255))
  I1.text((105, 180), str(res['posts']), font=myFont, fill=(255, 255, 255))
  I1.text((435, 63), str(res['countries']), font=myFont, fill=(255, 255, 255))
  I1.text((760, 63), str(res['sources']), font=myFont, fill=(255, 255, 255))
  I1.text((435, 180), str(res['reach']), font=myFont, fill=(255, 255, 255))
  img.save("tmp/summary_widget.png")
