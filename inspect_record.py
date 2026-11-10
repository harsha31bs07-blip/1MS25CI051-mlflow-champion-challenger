"""Render contact sheets for visual checking of the generated Word record."""
import pymupdf
from PIL import Image, ImageDraw
from config import OUTPUTS

doc = pymupdf.open(OUTPUTS / 'document-preview/Completed_Lab_Record.pdf')
print('Rendered pages:', len(doc))
for start in range(0, len(doc), 8):
    sheet = Image.new('RGB', (1200, 1700), '#bfc8cd')
    for offset in range(min(8, len(doc)-start)):
        page = doc[start+offset]
        pix = page.get_pixmap(matrix=pymupdf.Matrix(.65,.65))
        im = Image.frombytes('RGB', (pix.width,pix.height), pix.samples)
        im.thumbnail((290,790))
        x,y = (offset%4)*300, (offset//4)*850
        sheet.paste(im, (x,y+25))
        ImageDraw.Draw(sheet).text((x+8,y+5), f'Page {start+offset+1}', fill='black')
        assert page.get_text().strip(), f'Blank page {start+offset+1}'
    sheet.save(OUTPUTS / f'document-preview/contact_{start//8+1}.png')
