import torch
import os
import re
import cv2
import argparse
import imutils
import pytesseract
import numpy as np
from pytesseract import Output
from .preprocess import process_image, clean_ocr_text


def ocr(path):
    if path != None:
        cleaned = []
        fix_angle = 0
        custom_config = r'-l train --psm 6 -c tessedit_char_whitelist="آابپتثجچحخدذرزژس ش ص ض ط ظ ع غ ف ق ک گ ملی ن و ه ی  ١۲۳۴۵۶۷۸۹"'
        # rotated = imutils.rotate_bound(cv2.imread(path),angle=fix_angle)
        rotated = process_image(path)
        ocr = pytesseract.image_to_string(rotated, lang='fas')
        cleaned_ocr = clean_ocr_text(ocr)
        concated_text = ' '.join(cleaned_ocr)

        # rotated = imutils.rotate_bound(cv2.imread(path), angle=fix_angle)

        cleaned.append(concated_text)
        return cleaned
    else:
        return "Can not read"
