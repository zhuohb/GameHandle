from utils import game_util
from web_app import flask_app

if __name__ == '__main__':
    directory_path = './image'
    game_util.load_template_images_from_directory(directory_path)
    # 启动 Flask 应用，开启调试模式，指定端口为 8080 调试模式启动需要删除debug=True
    # flask_app.run(debug=True, port=8080)
    flask_app.run(port=8080)
