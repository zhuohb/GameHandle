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

// 为图像添加缩放功能
const image = document.getElementById('output-image');
const getCoordinatesButton = document.getElementById('get-coordinates-button');
const coordinateDisplay = document.getElementById('coordinate-display');
const selectedCoordinate = document.getElementById('selected-coordinate');
const zoomRegion = document.getElementById('zoom-region');
let scale = 1;
let isGettingCoordinates = false;

// 等待图片加载完成
image.onload = function () {
    const zoomImage = document.createElement('img');
    zoomImage.src = this.src;
    zoomRegion.appendChild(zoomImage);

    // 监听鼠标滚轮事件
    this.addEventListener('wheel', function (e) {
        e.preventDefault();

        if (e.deltaY < 0) {
            scale += 0.1;
        } else {
            scale -= 0.1;
        }

        scale = Math.max(0.3, Math.min(1, scale));
        this.style.transform = `scale(${scale})`;
    });

    // 监听取坐标按钮点击事件
    getCoordinatesButton.addEventListener('click', function () {
        isGettingCoordinates =!isGettingCoordinates;
        if (isGettingCoordinates) {
            this.textContent = '取消取坐标';
        } else {
            this.textContent = '取坐标';
            coordinateDisplay.style.display = 'none';
            zoomRegion.style.display = 'none';
        }
    });

    // 监听鼠标移动事件
    this.addEventListener('mousemove', function (e) {
        if (isGettingCoordinates) {
            const rect = this.getBoundingClientRect();
            const x = Math.round((e.clientX - rect.left) / scale);
            const y = Math.round((e.clientY - rect.top) / scale);
            coordinateDisplay.style.display = 'block';
            coordinateDisplay.style.left = rect.left + 'px';
            coordinateDisplay.style.top = rect.top + 'px';
            coordinateDisplay.textContent = `当前坐标: (${x}, ${y})`;

            // 显示放大区域
            zoomRegion.style.display = 'block';
            zoomRegion.style.left = (e.clientX + 10) + 'px';
            zoomRegion.style.top = (e.clientY + 10) + 'px';

            // 调整放大图像的位置
            const zoomImage = zoomRegion.querySelector('img');
            zoomImage.style.left = (-x * 5 + 100) + 'px';
            zoomImage.style.top = (-y * 5 + 100) + 'px';
        }
    });

    // 监听鼠标点击事件
    this.addEventListener('click', function (e) {
        if (isGettingCoordinates) {
            const rect = this.getBoundingClientRect();
            const x = Math.round((e.clientX - rect.left) / scale);
            const y = Math.round((e.clientY - rect.top) / scale);
            selectedCoordinate.textContent = `选择的坐标: (${x}, ${y})`;
        }
    });
};
