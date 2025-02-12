import subprocess

import cv2
import numpy as np
from flask import Flask, render_template, request, jsonify

import global_vars
import util

flask_app = Flask(__name__)


@flask_app.route('/')
def index():
    return render_template('index.html')


@flask_app.route('/submit', methods=['POST'])
def submit():
    large_image = request.files['large_image']
    large_img = cv2.imdecode(np.frombuffer(large_image.read(), np.uint8), cv2.IMREAD_COLOR)

    small_img = global_vars.small_img

    output_image = util.perform_template_matching(large_img, small_img)

    return jsonify({'output_image': output_image})


@flask_app.route('/connect_adb', methods=['POST'])
def connect_adb():
    ip = request.form.get('ip')
    try:
        # 执行 ADB 连接命令
        result = subprocess.run(['adb', 'connect', ip], capture_output=True, text=True)
        if "connected to" in result.stdout:
            adb_message = f"成功连接到设备 {ip}"
        else:
            adb_message = f"连接失败: {result.stderr}"
    except Exception as e:
        adb_message = f"发生错误: {str(e)}"

    return jsonify({'message': adb_message})
