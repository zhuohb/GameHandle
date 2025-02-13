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


@flask_app.route('/match', methods=['POST'])
def match():
    small_image_name = request.form.get('small_image_name')
    large_image = request.files['large_image']
    img_mat = cv2.imdecode(np.frombuffer(large_image.read(), np.uint8), cv2.IMREAD_COLOR)

    output_image = util.web_match(img_mat, global_vars.template_mat_map[small_image_name])

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
