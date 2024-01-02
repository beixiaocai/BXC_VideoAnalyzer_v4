

### ffmpeg命令行推流

~~~

//将本地文件推流至VideoAnalyzer（该命令行未经优化，延迟较大）
ffmpeg -re -stream_loop -1  -i test.mp4  -rtsp_transport tcp -c copy -f rtsp rtsp://127.0.0.1:9554/live/test

//将摄像头视频流推流至VideoAnalyzer（该命令行已优化，但仍然存在延迟，如果想要彻底解决推流延迟，可以参考我的视频：https://space.bilibili.com/487906612）
ffmpeg  -rtsp_transport tcp -i url -fflags nobuffer -max_delay 1 -threads 5  -profile:v high  -preset superfast -tune zerolatency  -an -c:v h264 -crf 25 -s 1280*720   -f rtsp -bf 0  -g 5  -rtsp_transport tcp rtsp://127.0.0.1:9554/live/camera

~~~


### 有关ffmpeg推流的几点补充说明

* 通过ffmpeg命令行实现的推流功能，延迟总是存在的，且无法解决。
* 基于ffmpeg开发库可以彻底解决延迟推流的问题，具体可以参考我的视频：https://space.bilibili.com/487906612
