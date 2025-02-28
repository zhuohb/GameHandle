import subprocess
import time
from functools import wraps


# 定义重试装饰器
def retry(max_retries=3, delay=2):
    """
    重试装饰器，当函数执行失败时自动重试。
    :param max_retries: 最大重试次数（默认3次）
    :param delay: 重试间隔（默认2秒）
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except subprocess.CalledProcessError as e:
                    print(f"函数执行失败: {e}")
                    print(f"重试中... ({retries + 1}/{max_retries})")
                    time.sleep(delay)
                    retries += 1
            print(f"重试{max_retries}次后命令失败,中止")
            return None  # 返回None表示命令失败
        return wrapper
    return decorator


# 定义ADB命令执行函数
@retry(max_retries=3, delay=2)
def execute_adb_command(command):
    """
    执行ADB命令并返回输出。
    :param command: ADB命令（列表形式）
    :return: 命令输出（成功时）或None（失败时）
    """
    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=True  # 如果命令失败，会抛出CalledProcessError
    )
    return result.stdout.strip()


# 示例：执行ADB命令
if __name__ == "__main__":
    # 定义要执行的ADB命令
    adb_command = ["adb", "devices"]

    # 执行命令
    output = execute_adb_command(adb_command)

    if output:
        print("ADB command succeeded:")
        print(output)
    else:
        print("ADB command failed after multiple retries.")
