import unittest
from unittest.mock import patch, call
import subprocess
from decorator.retry_decorator import retry, execute_adb_command

class TestRetryDecorator(unittest.TestCase):

    @patch('subprocess.run')
    def test_retry_success(self, mock_run):
        # 模拟成功的命令执行
        mock_run.return_value.stdout = "Success"
        mock_run.return_value.returncode = 0

        @retry(max_retries=3, delay=1)
        def test_command():
            return execute_adb_command(["echo", "test"])

        result = test_command()
        self.assertEqual(result, "Success")
        mock_run.assert_called_once()

    @patch('subprocess.run')
    def test_retry_failure(self, mock_run):
        # 模拟失败的命令执行
        mock_run.side_effect = subprocess.CalledProcessError(1, 'cmd')

        @retry(max_retries=3, delay=1)
        def test_command():
            return execute_adb_command(["echo", "test"])

        result = test_command()
        self.assertIsNone(result)
        self.assertEqual(mock_run.call_count, 3)

    @patch('subprocess.run')
    def test_retry_partial_success(self, mock_run):
        # 模拟前两次失败，第三次成功的命令执行
        mock_run.side_effect = [subprocess.CalledProcessError(1, 'cmd'), subprocess.CalledProcessError(1, 'cmd'), subprocess.CompletedProcess(args=['cmd'], returncode=0, stdout="Success")]

        @retry(max_retries=3, delay=1)
        def test_command():
            return execute_adb_command(["echo", "test"])

        result = test_command()
        self.assertEqual(result, "Success")
        self.assertEqual(mock_run.call_count, 3)

if __name__ == '__main__':
    unittest.main()