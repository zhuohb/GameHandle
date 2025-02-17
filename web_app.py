import subprocess

import cv2
import numpy as np
from flask import Flask, render_template, request, jsonify

import global_vars
from utils import img_util, adb_util

flask_app = Flask(__name__)


@flask_app.route('/')
def index():
    return render_template('index.html')


@flask_app.route('/match', methods=['POST'])
def match():
    ip = request.form.get('ip')
    small_image_name = request.form.get('templateName')

    adb_util.connect(ip)
    screenshot = adb_util.screenshot(ip)

    output_image = img_util.web_match(screenshot, global_vars.template_mat_map[small_image_name])

    return jsonify({'output_image': output_image})
