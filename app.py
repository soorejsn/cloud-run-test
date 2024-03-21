from flask import Flask
from PIL import Image
import pytesseract

# CV Imports
import os
import cv2
import time
import binascii
import numpy as np
import pandas as pd

from datetime import datetime
from json import JSONDecodeError
from google.oauth2.service_account import Credentials as ServiceAccountCredentials

# DMS Imports
import requests
import google
requests.packages.urllib3.disable_warnings()
import json
from flask import Flask, request
# GoogleCloud Imports

import base64

@app.route("/", methods=["POST"])
def main():
      print("In main function")
      envelope = request.get_json()

      # if not envelope:
      #     msg = "no Pub/Sub message received"
      #     print(f"error: {msg}")
      #     return f"Bad Request: {msg}", 400

      # if not isinstance(envelope, dict) or "message" not in envelope:
      #     msg = "invalid Pub/Sub message format"
      #     print(f"error: {msg}")
      #     return f"Bad Request: {msg}", 400

      event = envelope["message"]
      print("Event message -------- ", event)

      content = cv2.imread('test_img.png')
      texts = pytesseract.image_to_string(content)
      print("Extracted texts --------", texts)