
from pathlib import Path

from PIL import Image

from pyler_default import time_format


def get_tag(exif_info, tag_name):
    # https://www.vieas.com/exif23.html
    # https://www.cipa.jp/std/documents/j/DC-008-2012_J.pdf
    exif_tag = {
            'ImageDescription': 0x010e,
            'Make': 0x010f,
            'Model': 0x0110,
            'Orientation': 0x0112,
            'XResolution': 0x011a,
            'YResolution': 0x011b,
            'ResolutionUnit': 0x0128,
            'DateTime': 0x0132,
            'YCbCrPositioning': 0x0213,
            'Exif IFD Pointer': 0x8769,
            }

    field = exif_tag[tag_name]
    if field not in exif_info:
        return None
    else:
        return exif_info[field]


def main(item: Path):
    stat = item.stat()
    with Image.open(item) as img_data:
        width = img_data.width
        height = img_data.height
        img_exif = img_data.getexif()

    res = '''
created: {}
Exif Date: {}
Make: {}
Model: {}
Size: {}x{}'''.format(time_format(stat.st_birthtime),
                      get_tag(img_exif, 'DateTime'),
                      get_tag(img_exif, 'Make'),
                      get_tag(img_exif, 'Model'),
                      width, height
                      )
    return res
