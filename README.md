### 视频行为分析系统v4
* 作者：北小菜 
* 官网：http://www.beixiaocai.com
* 邮箱：bilibili_bxc@126.com
* QQ：1402990689
* 微信：bilibili_bxc
* 哔哩哔哩主页：https://space.bilibili.com/487906612
* gitee下载地址：https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4
* github下载地址：https://github.com/any12345com/BXC_VideoAnalyzer_v4

### 软件介绍
* 基于C++开发的视频行为分析系统v4版本，可以在不用考虑音视频开发，编解码开发，界面开发等情况下， 只需要训练自己的模型，开发自己的算法插件，就可以轻松实现出任何想要的视频行为检测，比如周界入侵，烟火检测，打架，斗殴，跌倒，人群聚集，电动车，垃圾箱，抽烟，攀爬，离岗睡岗，安全帽，充电桩，工作服， 疲劳检测，交通拥堵等等。

### 仓库提交记录删除原因说明
* 因为gitee或github对代码仓库的存储上限均是1G，因此每隔一段时间仓库容量都会用尽，所以每隔一段时间都需要清空一次仓库
* 为了方便大家下载视频行为分析系统v4历史版本，下面提供了历史版本下载表
* [历史版本下载表](https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4/wikis/常见问题/历史版本下载表)

### 版本介绍
| 操作系统 | 硬件 | 推理引擎 | 下载地址 |
| :----: | :----: | :----: | :----- |
| Windows10/11 | intel | openvino | [下载](https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4/wikis/Windows版本/Windows版本) |
| Windows10/11 | intel+nvidia | openvino+tensorrt | [下载](https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4/wikis/Windows版本/下载Windows支持TensorRT的版本) |
| Windows10/11 | amd,,, | onnxruntime | [下载](https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4/wikis/Windows版本/下载Windows支持onnxruntime的版本) |
| Ubuntu20/22 | intel+nvidia | openvino+tensorrt | [下载](https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4/wikis/Linux版本/Ubuntu版本) |
| Ubuntu20/22 | rk3588 | rknpu | [下载](https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4/wikis/Linux版本/RK3588版本) |


### 使用说明
* [启动配置](https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4/wikis/启动配置)
* [支持哪些硬件](https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4/wikis/支持哪些硬件)
* [windows+openvino版本](https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4/wikis/Windows版本/Windows版本)
* [windows+tensorrt版本](https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4/wikis/Windows版本/下载Windows支持TensorRT的版本)
* [windows+onnxruntime版本](https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4/wikis/Windows版本/下载Windows支持onnxruntime的版本)
* [ubuntu+tensorrt版本](https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4/wikis/Linux版本/Ubuntu版本)
* [ubuntu+rk3588版本](https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4/wikis/Linux版本/RK3588版本)
* [ffmpeg推流模拟摄像头](https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4/wikis/视频流管理/FFmpeg推流模拟摄像头)
* [算法管理](https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4/wikis/算法管理/算法管理)
* [基础算法管理](https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4/wikis/算法管理/基础算法管理)
* [行为算法管理](https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4/wikis/算法管理/行为算法管理)
* [布控管理](https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4/wikis/布控管理/布控管理)
* [报警接口](https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4/wikis/报警管理/报警接口)
* [报警过滤器](https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4/wikis/报警管理/报警过滤器)
* [开放接口](https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4/wikis/开放接口/开放接口)


# 版本历史
### v4.413
* 发布时间 2024.05.17
* （1）新增用户模块模块，区分管理员和普通用户，管理员可以增删改查用户
* （2）提升配置扩展能力，配置参数全部转移至配置文件，下载地址，文档地址，logo，作者链接等均可以修改
* （3）修复此前版本报警过滤器的bug
* （4）统一软件启动图标

#### v4.412
* 发布时间 2024.05.14
* （1）优化此前串行算法流的性能问题，此前的检测->分类或检测->追踪均有大幅度性能提升
* （2）修复分析器多进程的bug

#### v4.411
* 发布时间 2024.05.13
* （1）优化机器授权码授权检测逻辑，将所有检测逻辑全部移动至分析器模块
* （2）减少各个子模块频繁检测导致性能浪费 

#### v4.410
* 发布时间 2024.05.11
* （1）新增支持自定义报警过滤器功能，可以在报警前调用自己的报警过滤器，用于提前验证报警是否为误报
* （2）修复此前版本ONVIF功能的bug

#### v4.409
* 发布时间 2024.05.07
* （1）新增支持ONVIF搜索功能，ONVIF自动获取地址功能，ONVIF获取设备信息功能，ONVIF截屏功能
* （2）新增支持视频流手动录像功能，手动截图功能
* （3）新增支持可自定义配置存储根路径，已将报警数据移至该路径，后续录像截屏数据均会放在该路径
* （4）优化报警数据存储结构，扩展报警描述文本信息
* （5）优化后台管理依赖库，去除未使用依赖库，提高web访问性能

#### v4.408
* 发布时间 2024.05.01
* （1）新增支持检测算法->分类算法->行为算法的模式，对解决算法误报非常有效
* （2）新增支持OpenVINO推理追踪算法
* （3）优化原有TensorRT推理追踪算法的计算性能
* （4）升级OpenVINO依赖库，由2023.3.0升级至2024.1.0，新版本稳定性有所提升
* （5）优化合成报警视频质量，改善合成视频时丢帧问题
* 特别说明：本次版本优化的内容较多，也进行了比较完整的测试，建议升级至该版本
* 注：生产环境建议使用TensorRT，OpenVINO虽然安装简单，但是性能和稳定性远不如TensorRT。即便是本次版本花费了不少时间和精力去兼容OpenVINO版追踪算法和分类算法，但兼容OpenVINO只是为了降低大家体验该软件的门槛

#### v4.407
* 发布时间 2024.04.20
* （1）优化播放h265视频流性能问题

#### v4.406
* 发布时间 2024.04.18
* （1）优化报警视频合成模块，修复报警视频的不固定问题
* （2）新增支持设置报警封面帧在报警视频中的位置
* （3）改善包含报警视频的报警信息的触发延迟时间
* （4）修复GB28181接入视频流模块的sip信令中，客户端主动bye的资源释放问题
* （5）修复后台管理模块新增视频流不支持特殊字符的问题
* （6）修复部分linux系统修改视频分辨率花屏问题

#### v4.405
* 发布时间 2024.04.13
* （1）新增支持GB28181视频流接入协议
* （2）后台管理模块升级依赖库

#### v4.404
* 发布时间 2024.04.07
* （1）算法模块新增支持TensorRT推理yolo8-pose模型
* （2）算法流新增支持人体关键点渲染

#### v4.403
* 发布时间 2024.04.02
* （1）后台管理调整UI主题
* （2）启动配置扩展硬件编解码配置项

#### v4.402
* 发布时间 2024.03.29
* （1）优化布控推流延迟问题
* （2）优化启动器的日志记录问题

#### v4.401
* 发布时间 2024.03.28
* （1）基础算法管理模块新增支持上传engine格式的模型
* （2）基础算法api类型扩展上传字段，扩展字段包括布控编号，算法编号，扩展字段，osd字段
* （3）行为算法api类型扩展上传字段，扩展字段包括布控编号，算法编号，扩展字段，osd字段

#### v4.40
* 发布时间 2024.03.24
* （1）分析器重构算法模块计算流程，重构后可支持不同算法模型的层级调用，并支持多种不同类型的算法框架
* （2）分析器新增支持检测算法>>追踪算法>>行为算法的新模式
* （3）分析器新增支持越线检测算法，可以用来检测目标是否逆行
* （4）后台管理重构布控页面的区域绘制功能，并新增越线检测绘制功能
* （5）后台管理重构上传基础算法模型的功能，TensorRT新增支持上传onnx格式的模型，OpenVINO新增支持上传bin+xml压缩的tar包

#### v4.398
* 发布时间 2024.03.18
* （1）重构算法模块结构，重构后可支持算法模型的层级调用，并支持多种常见的算法层级调用流程
* （2）优化算法实例管理器，解决此前算法实例自定义缓存时长的bug

#### v4.397
* 发布时间 2024.03.15
* （1）新增支持可配置硬件解码路数和硬件编码路数（提升性能）
* （2）优化启动环境检查功能，优化软件监控功能，优化日志

#### v4.396
* 发布时间 2024.03.08
* （1）修复OSD参数的bug
* （2）修复英伟达多显卡计算的bug
* （3）修复自定义API类型的基础算法接入的bug

#### v4.395
* 发布时间 2024.03.04
* （1）完善OSD参数，支持默认字体大小，默认字体颜色，默认字体行间距
* （2）导入摄像头模板支持自定义摄像头编号

#### v4.394
* 发布时间 2024.02.29
* （1）扩展OSD参数，支持自定义任意位置的OSD贴图，并且支持中文内容的贴图
* （2）扩展布控参数，支持更多自定义功能
* （3）完善开放接口的字段校验功能

#### v4.393
* 发布时间 2024.02.24
* （1）扩展算法检测模式，在原有自由竞争模式的基础上，扩展支持可配置间隔帧检测，扩展支持可配置间隔秒检测
* （2）修复二次开发报警接口测试功能

#### v4.392
* 发布时间 2024.02.21
* （1）分析器新增验证TensorRT模型是否正常的命令行功能
* （2）后台管理扩展布控参数

#### v4.391
* 发布时间 2024.02.19
* （1）修复后台管理sql语句bug
* （2）扩展报警数据的上传参数

#### v4.39
* 发布时间 2024.02.16
* （1）基础算法模型实例化时支持自定义设置并发数量，提升硬件性能利用率
* （2）修复基础算法模型加密的bug

#### v4.38
* 发布时间 2024.02.07
* （1）算法推理引擎支持 TensorRT-yolo5，TensorRT-yolo8，OpenVINO-yolo5，OpenVINO-yolo8，OpenVINO-ResNet34
* （2）openvino版本升级

#### v4.37
* 发布时间 2024.02.06
* （1）修复报警视频合成缓存清理bug
* （2）修复启动器控制bug
* （3）优化启动器调度性能
* （4）修复视频转码bug

#### v4.36
* 发布时间 2024.02.03
* （1）完善布控轮巡功能
* （2）布控轮巡功能支持分屏预览功能

#### v4.35
* 发布时间 2024.02.01
* （1）修复4.34版本配置模型缓存时长的bug
* （2）优化后台管理UI
* （3）扩展报警数据接口接入功能，新增支持接入kafka，redis，mongodb

#### v4.34
* 发布时间 2024.01.28
* （1）新增支持配置项，模型缓存时长
* （2）新增支持配置项，重启时是否启用全部摄像头转发
* （3）新增支持布控轮巡功能
* （4）新增支持配置项，轮巡时是否启用自动管理转发（如果启用：轮巡布控时，自动开启摄像头转发，布控轮巡结束时，自动关闭摄像头转发）
* （5）新增支持布控分页功能
* （6）新增支持摄像头批量开启转发和关闭转发功能
* （7）新增支持通过复制批量为离线摄像头设置布控
* （8）修复4.33版本模型加密功能的bug

#### v4.33
* 发布时间 2024.01.22
* （1）新增支持算法模型加密功能
* （2）新增支持火焰报警监测和烟雾报警监测功能

#### v4.32
* 发布时间 2024.01.13
* （1）新增支持加密狗（加密锁）授权
* （2）优化授权逻辑，修复此前机器授权码的bug
* （3）扩展系统前端自定义的功能范围


#### v4.31
* 发布时间 2024.01.10
* （1）新增支持自定义报警数据接口功能
* （2）新增支持自定义系统名称，作者名称，作者链接，logo，title等功能
* （3）新增支持查询布控数据和查询视频流数据等开放接口功能
* （4）新增支持自定义合成报警视频时长，自定义报警视频延迟推送时长

### v4.3
* 发布时间 2024.01.07
* （1）支持h265视频流播放
* （2）支持分屏功能，1分屏，4分屏，9分屏，16分屏，并支持全屏播放
* （3）支持在单屏或多分屏播放时，自适应转码视频分辨率，提升播放体验效果
* （4）优化后台管理功能逻辑
* （5）优化转码逻辑，提升性能
* （6）优化分析器调度逻辑

#### v4.25
* 发布时间 2023.12.30
* （1）优化算法实时处理推流的视频质量
* （2）基础算法模型新增可配置参数，可配置模型精度，预处理宽高，nms阈值，分类阈值

#### v4.24
* 发布时间 2023.12.28
* （1）解决报警延迟问题，已实现实时报警 
* （2）解决原报警视频合成方案导致的处理器和内存的过度消耗问题，大幅度提升软件性能
* （3）优化算法渲染推流，提高算法渲染推流流畅性
* （4）新增支持Ubuntu系统

#### v4.23
* 发布时间 2023.12.20
* （1）优化视频分析器的调度逻辑
* （2）新增支持英伟达显卡TensorRT推理。

#### v4.22
* 发布时间 2023.12.14
* （1）分析器在布控时新增推理设备是否支持的检测
* （2）分析器优化报警合成队列的使用机制
* （3）后台管理新增新版本检测功能，新版本弹窗提示功能

#### v4.21
* 发布时间 2023.12.13
* （1）优化解码和分析以及推流的队列内存复用
* （2）优化算法推流的流畅性

### v4.2
* 发布时间 2023.12.10
* （1）解决系统稳定性问题，已经可以非常稳定的运行在配置比较一般的Windows设备（4000元左右的8G内存轻薄本，也可以非常稳定的布控10-20路1080p视频流）
* （2）系统启动时新增环境检测功能，环境检测包括端口占用检测，程序重开检测，后续会增加处理器支持检测，显卡支持检测
* （3）FFmpeg-4.4升级至FFmpeg6.0

#### v4.12
* 发布时间 2023.12.9
* （1）解决视频分析器在大规模布控情况下，布控超过1小时，必崩溃的稳定性问题。（与视频流拉流解码时线程安全有关，OpenCV-3.4.10版本有关）
* （2）OpenCV-3.4.10升级至OpenCV-4.7.0，考虑到该项目目标是让足够多的普通笔记本电脑能够运行，因此该OpenCV库未扩展cuda模块，仅扩展了dnn模块。（注意：仅有支持N卡的机器才能运行包含cuda模块的OpenCV库）

#### v4.11
* 发布时间 2023.12.7
* （1）视频分析器优化布控调节，解决因为超量布控导致的程序崩溃
* （2）后台管理支持批量布控，布控复制，布控日志查询

### v4.1
* 发布时间 2023.12.5
* （1）视频分析器新增支持API类型的基础算法接入
* （2）后台管理新增支持API类型的基础算法
* （3）后台管理基础算法支持设置布控数量上限

### v4.0
* 发布时间 2023.12.3
* （1）视频分析服务优化合成报警视频的质量
* （2）视频分析服务优化因电脑性能不佳导致数据阻塞引起的程序崩溃（数据阻塞的原因在于消费速度小于生产速度）
* （3）视频分析服务支持动态模型实例化，动态模型删除，而不再是此前的指定启动模型实例，运行过程中不可删除，不可销毁
* （4）视频分析服务支持模型实例复用，多路布控共用同一个模型时，只开启一个模型实例
* （5）视频分析服务支持模型实例删除，多路布控共用同一个模型时，当该模型实例对应的所有布控都取消时，该模型实例也会取消并被删除
* （6）视频分析服务支持自动调节，在运行过程中可以根据资源的消耗情况，自动调节可支持的布控数量
* （7）视频分析服务支持无限次重试拉流，无限次重试推流
* （8）后台管理优化UI
* （9）后台管理支持自定义添加摄像头，批量导入摄像头，批量转发，自启动转发
* （10）后台管理支持自定义添加算法，包括基础算法和行为算法，对于基础算法，用户可以添加自己训练的模型，对于行为算法，可以选用系统内置的行为算法，也可以自己通过接口或动态库的方式，二次开发（通过这里预留的二次开发功能，可以轻松做出各种场景安全检测的视频行为分析系统，比如打架，跌倒，人群聚集，离岗睡岗，安全帽检测等等）
* （11）后台管理支持自定义添加报警声音，每一个布控东可以自定义独一无二的报警声
* （12）后台管理优化布控功能，新增报警视频类型的选项，报警图片数量的选项，布控目标的选项，阈值的选项。
* （13）后台管理优化报警查看功能，报警产生时页面自动刷新，并播放报警声音，新增报警详情页，可以进入报警详情页下载报警产生的视频和图片资料
* （14）使用视频行为分析系统v4版本的二次开发功能，可以直接就做场景安全检测功能上的开发，使用者再也不用考虑，流媒体开发，音视频开发，编解码开发，后台管理等。


### v1,v2,v3版本相关链接

* v1版本视频介绍地址 https://www.bilibili.com/video/BV1dG4y1k77o
* v1版本源码讲解（1）拉流，解码，实时算法分析，合成报警视频，编码，推流 https://www.bilibili.com/video/BV1L84y177xc
* v1版本源码讲解（2）音频解码，音频重采样，音频编码，合成报警视频 https://www.bilibili.com/video/BV1984y1L7zB
* v2版本视频介绍地址 https://www.bilibili.com/video/BV1CG411f7ak
* v3版本视频介绍地址 https://www.bilibili.com/video/BV1Xy4y1P7M2
* v1版本开源地址 https://gitee.com/Vanishi/BXC_VideoAnalyzer_v1
* v2版本开源地址 https://gitee.com/Vanishi/BXC_VideoAnalyzer_v2
* v3版本安装包下载地址 https://gitee.com/Vanishi/BXC_VideoAnalyzer_v3
* v3版本源码购买地址（淘宝） https://item.taobao.com/item.htm?id=746326947806
* v3版本源码购买地址（闲鱼） https://h5.m.goofish.com/item?id=744350097882

<img width="720" alt="控制面板" src="https://gitee.com/Vanishi/images/raw/master/BXC_VideoAnalyzer_v4/v4.409/1.png">
<img width="720" alt="报警视频管理" src="https://gitee.com/Vanishi/images/raw/master/BXC_VideoAnalyzer_v4/v4.409/2.png">
<img width="720" alt="摄像头管理" src="https://gitee.com/Vanishi/images/raw/master/BXC_VideoAnalyzer_v4/v4.409/3.png">
<img width="720" alt="算法管理" src="https://gitee.com/Vanishi/images/raw/master/BXC_VideoAnalyzer_v4/v4.409/4.png">
<img width="720" alt="添加算法" src="https://gitee.com/Vanishi/images/raw/master/BXC_VideoAnalyzer_v4/v4.409/5.png">
<img width="720" alt="布控管理" src="https://gitee.com/Vanishi/images/raw/master/BXC_VideoAnalyzer_v4/v4.409/6.png">
<img width="720" alt="添加布控" src="https://gitee.com/Vanishi/images/raw/master/BXC_VideoAnalyzer_v4/v4.409/7.png">
<img width="720" alt="系统维护" src="https://gitee.com/Vanishi/images/raw/master/BXC_VideoAnalyzer_v4/v4.409/8.png">
<img width="720" alt="关于系统" src="https://gitee.com/Vanishi/images/raw/master/BXC_VideoAnalyzer_v4/v4.409/9.png">
