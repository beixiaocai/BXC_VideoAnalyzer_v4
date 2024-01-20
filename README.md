### 视频行为分析系统v4
* 作者：北小菜 
* 个人网站：http://www.any12345.com
* 邮箱：bilibili_bxc@126.com
* QQ：1402990689
* 微信：bilibili_bxc
* 哔哩哔哩主页：https://space.bilibili.com/487906612
* gitee安装包下载地址：https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4
* github安装包下载地址：https://github.com/any12345com/BXC_VideoAnalyzer_v4

### 软件介绍
* 基于视频行为分析系统v4系列软件，可以在不用考虑音视频开发，编解码开发，界面开发等情况下，
只需要训练自己的模型，开发自己的算法插件，就可以轻松实现出任何想要的视频行为检测，比如周界入侵，烟火检测，打架，斗殴，跌倒，人群聚集，电动车，垃圾箱，抽烟，攀爬，离岗睡岗，安全帽，充电桩，工作服，
疲劳检测，交通拥堵等等。


### 使用说明
* [Windows版本使用说明](https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4/wikis/Windows版本)
* [Ubuntu版本使用说明](https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4/wikis/Ubuntu版本)
* [FFmpeg推流模拟摄像头使用说明](https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4/wikis/FFmpeg推流模拟摄像头)
* [支持哪些硬件使用说明](https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4/wikis/支持哪些硬件)
* [二次开发算法使用说明](https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4/wikis/二次开发算法)
* [二次开发报警接口使用说明](https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4/wikis/二次开发报警接口)
* [启动配置使用说明](https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4/wikis/启动配置)
* [布控参数使用说明](https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4/wikis/布控参数)
* [版本历史](https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4)


# 版本历史

## 如需TensorRT版本请注意
* （1）Windows版支持TensorRT+OpenVINO的分析器，请下载对应版本 Analyzer+library 替换到软件的Analyzer模块 网盘链接：https://pan.baidu.com/s/19sgSxAriNneRT9s44o_5eA 提取码：1220
* （2）软件依赖库内置CUDA库版本是12.0，所以想要运行CUDA12.0，英伟达显卡驱动必须满足最低驱动版本要求，否则无法运行
* （3）CUDA版本与英伟达显卡驱动版本关系表：[查看版本关系表](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html)
* （4）英伟达显卡驱动下载地址：[下载英伟达显卡驱动](https://www.nvidia.cn/Download/index.aspx?lang=cn)


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
* 特别注意事项
* （1）由于TensorRT必须在内置英伟达显卡的设备上运行，而且依赖库非常庞大，所以分析器模块分为两种版本，非nvidia显卡版和nvidia显卡版。
* （2）gitee下载的本软件，默认内置的是非nvidia显卡版分析器，如需nvidia显卡版分析器，请到下面的网盘链接下载并替换
* nvidia显卡版分析器百度网盘下载链接：https://pan.baidu.com/s/19sgSxAriNneRT9s44o_5eA 提取码：1220
* （3）软件依赖库内置CUDA库版本是12.0，所以想要运行CUDA12.0，英伟达显卡驱动必须满足最低驱动版本要求，否则无法运行
* （4）CUDA版本与英伟达显卡驱动版本关系表：[查看版本关系表](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html)
* （5）英伟达显卡驱动下载地址：[下载英伟达显卡驱动](https://www.nvidia.cn/Download/index.aspx?lang=cn)

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
* v4.1视频介绍地址 [https://www.bilibili.com/video/BV1dH4y1C7hY](https://www.bilibili.com/video/BV1dH4y1C7hY)
* （1）视频分析器新增支持API类型的基础算法接入
* （2）后台管理新增支持API类型的基础算法
* （3）后台管理基础算法支持设置布控数量上限

### v4.0
* 发布时间 2023.12.3
* v4.0视频介绍地址 [https://www.bilibili.com/video/BV1gM411d72k](https://www.bilibili.com/video/BV1gM411d72k)
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
* （15）此前购买v3版本的用户，需要等后续v3.1的升级版。流媒体服务本次无更新。


### v1,v2,v3版本相关链接

* v1版本视频介绍地址 https://www.bilibili.com/video/BV1dG4y1k77o
* v1版本源码讲解（1）拉流，解码，实时算法分析，合成报警视频，编码，推流 https://www.bilibili.com/video/BV1L84y177xc
* v1版本源码讲解（2）音频解码，音频重采样，音频编码，合成报警视频 https://www.bilibili.com/video/BV1984y1L7zB
* v2版本视频介绍地址 https://www.bilibili.com/video/BV1CG411f7ak
* v3版本视频介绍地址 https://www.bilibili.com/video/BV1Xy4y1P7M2
* v3版本安装包下载地址 https://gitee.com/Vanishi/BXC_VideoAnalyzer_v3
* v3版本源码购买地址（淘宝） https://item.taobao.com/item.htm?id=746326947806
* v3版本源码购买地址（闲鱼） https://h5.m.goofish.com/item?id=744350097882


<img width="720" alt="控制面板" src="https://gitee.com/Vanishi/images/raw/master/BXC_VideoAnalyzer_v4/index.png">
<img width="720" alt="报警视频管理" src="https://gitee.com/Vanishi/images/raw/master/BXC_VideoAnalyzer_v4/alarm_index.png">
<img width="720" alt="摄像头管理" src="https://gitee.com/Vanishi/images/raw/master/BXC_VideoAnalyzer_v4/stream_index.png">
<img width="720" alt="行为算法管理" src="https://gitee.com/Vanishi/images/raw/master/BXC_VideoAnalyzer_v4/behaviour_index.png">
<img width="720" alt="基础算法管理" src="https://gitee.com/Vanishi/images/raw/master/BXC_VideoAnalyzer_v4/algorithm_index.png">
<img width="720" alt="添加基础算法" src="https://gitee.com/Vanishi/images/raw/master/BXC_VideoAnalyzer_v4/algorithm_add.png">
<img width="720" alt="音频管理" src="https://gitee.com/Vanishi/images/raw/master/BXC_VideoAnalyzer_v4/audio_index.png">
<img width="720" alt="布控管理" src="https://gitee.com/Vanishi/images/raw/master/BXC_VideoAnalyzer_v4/control_index.png">
<img width="720" alt="添加布控" src="https://gitee.com/Vanishi/images/raw/master/BXC_VideoAnalyzer_v4/control_add.png">
<img width="720" alt="系统维护" src="https://gitee.com/Vanishi/images/raw/master/BXC_VideoAnalyzer_v4/system_index.png">
<img width="720" alt="版本" src="https://gitee.com/Vanishi/images/raw/master/BXC_VideoAnalyzer_v4/version.png">

