import subprocess
import time


def is_adb_running():
    try:
        subprocess.check_output(['adb', 'devices'], stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError:
        return False


def start_adb_server():
    print("ADB server is not running. Starting...")
    subprocess.run(['adb', 'start-server'])


if __name__ == "__main__":
    while True:
        if not is_adb_running():
            start_adb_server()
        time.sleep(5)  # 每隔5秒检查一次
