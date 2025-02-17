// 获取表单元素，后续用于监听表单提交事件
const imageMatchForm = document.getElementById('imageMatchForm');

// 获取用于显示连接结果消息的 div 元素
const imageMatchFormMessageDiv = document.getElementById('imageMatchFormMessage');

// 为 imageMatchForm 添加 submit 事件监听器
imageMatchForm.addEventListener('submit', async (e) => {
    // 阻止表单的默认提交行为，避免页面刷新
    e.preventDefault();

    const ip = document.getElementById('ip').value;
    const templateName = document.getElementById('templateName').value;

    // 创建一个 FormData 对象，用于收集表单数据
    const formData = new FormData();
    // 将图像文件添加到 FormData 对象中
    formData.append('templateName', templateName);
    formData.append('ip', ip);

    try {
        const response = await fetch('/match', {
            method: 'POST',
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