// 获取表单元素，后续用于监听表单提交事件
const imageMatchForm = document.getElementById('imageMatchForm');
const adbForm = document.getElementById('adbForm');
// 获取用于显示连接结果消息的 div 元素
const imageMatchFormMessageDiv = document.getElementById('imageMatchFormMessage');
const messageDiv = document.getElementById('adbMessage');

// 为表单添加 submit 事件监听器，当用户提交表单时会触发回调函数
adbForm.addEventListener('submit', async (e) => {
    // 阻止表单的默认提交行为，避免页面刷新
    e.preventDefault();

    // 获取用户输入的设备 IP 地址
    const ip = document.getElementById('ip').value;
    // 创建一个 FormData 对象，用于收集表单数据
    const formData = new FormData();
    // 将 IP 地址添加到 FormData 对象中
    formData.append('ip', ip);

    try {
        // 使用 fetch API 发起一个异步的 POST 请求到 /connect_adb 接口
        const response = await fetch('/connect_adb', {
            // 请求方法为 POST
            method: 'POST',
            // 请求体为包含 IP 地址的 FormData 对象
            body: formData
        });

        // 检查响应状态是否为成功（状态码 200 - 299）
        if (response.ok) {
            // 将响应数据解析为 JSON 格式
            const data = await response.json();
            // 将解析后的消息显示在 messageDiv 元素中
            messageDiv.textContent = data.message;
        } else {
            // 如果响应状态不是成功，显示请求出错的消息
            messageDiv.textContent = '请求出错';
        }
    } catch (error) {
        // 如果在请求过程中发生错误，显示错误信息
        messageDiv.textContent = `发生错误: ${error.message}`;
    }
});

// 为 imageMatchForm 添加 submit 事件监听器
imageMatchForm.addEventListener('submit', async (e) => {
    // 阻止表单的默认提交行为，避免页面刷新
    e.preventDefault();

    // 获取用户上传的图像文件
    const largeImage = document.getElementById('large_image').files[0];
    // 创建一个 FormData 对象，用于收集表单数据
    const formData = new FormData();
    // 将图像文件添加到 FormData 对象中
    formData.append('large_image', largeImage);

    try {
        // 使用 fetch API 发起一个异步的 POST 请求到 /submit 接口
        const response = await fetch('/submit', {
            // 请求方法为 POST
            method: 'POST',
            // 请求体为包含图像文件的 FormData 对象
            body: formData
        });

        // 检查响应状态是否为成功（状态码 200 - 299）
        if (response.ok) {
            // 将响应数据解析为 JSON 格式
            const data = await response.json();
            // 获取消息和处理后的图像数据
            const outputImage = data.output_image;

            // 如果有处理后的图像数据，更新 img 元素的 src 属性
            if (outputImage) {
                const imgElement = imageMatchFormMessageDiv.querySelector('img');
                imgElement.src = outputImage;
                imgElement.style.display = 'block'; // 显示图像
            }
        }
    } catch (error) {
        // 如果在请求过程中发生错误，显示错误信息
        imageMatchFormMessageDiv.textContent = `发生错误: ${error.message}`;
    }
});