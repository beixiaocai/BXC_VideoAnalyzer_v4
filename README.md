## 视频行为分析系统v4(xcms)
* 作者：北小菜 
* 官网：http://www.beixiaocai.com
* 邮箱：bilibili_bxc@126.com
* QQ：1402990689
* 微信：bilibili_bxc
* 哔哩哔哩主页：https://space.bilibili.com/487906612
* gitee地址：https://gitee.com/Vanishi/BXC_VideoAnalyzer_v4
* github地址：https://github.com/beixiaocai/BXC_VideoAnalyzer_v4

## 简介
* C++开发的视频行为分析系统v4版本，可以在不用考虑音视频开发，编解码开发，界面开发等情况下， 只需要训练自己的模型，开发自己的算法插件，就可以轻松实现出任何想要的视频行为检测，比如周界入侵，烟火检测，打架，斗殴，跌倒，人群聚集，电动车，垃圾箱，抽烟，攀爬，离岗睡岗，安全帽，充电桩，工作服， 疲劳检测，交通拥堵等等。
* 视频行为分析系统的简称 xcms
* 通过本开源平台直接克隆/下载的版本是x86-Windows-ov版

## 软件支持的运行环境介绍
| 架构 | 操作系统 | 硬件 | 推理引擎 | 下载地址 |
| :----: | :----: | :----: | :----: | :----- |
| x86 | Windows | intel,amd | openvino+ort | [下载](https://beixiaocai.yuque.com/org-wiki-beixiaocai-vo72oa/xcms/333803623628302fe6f578cd3485e4be) |
| x86 | Windows | intel,amd+nvidia | openvino+tensorrt+ort | [下载](https://beixiaocai.yuque.com/org-wiki-beixiaocai-vo72oa/xcms/gyvtvcndflyppuhw) |
| x86 | Ubuntu | intel,amd | openvino | [下载](https://beixiaocai.yuque.com/org-wiki-beixiaocai-vo72oa/xcms/944d5586badc8e93686afc522a4feece) |
| x86 | Ubuntu | intel,amd+nvidia | openvino+tensorrt | [下载](https://beixiaocai.yuque.com/org-wiki-beixiaocai-vo72oa/xcms/2713611802e365950bc9c6fef5c6b118) |
| arm | Ubuntu | rk3588 | rknpu | [下载](https://beixiaocai.yuque.com/org-wiki-beixiaocai-vo72oa/xcms/76dbf61f8b5f8ce67891dc3e3f36b686) |
| arm | Ubuntu | 昇腾 | cann | [下载](https://beixiaocai.yuque.com/org-wiki-beixiaocai-vo72oa/xcms/644800c887eb14094e2154882b78e8fc) |
| x86 | Centos | 不限 |  | [下载](https://beixiaocai.yuque.com/org-wiki-beixiaocai-vo72oa/xcms/e382620e4df52bd7628d3fd141a7112d) |
| arm | 麒麟/欧拉/UOS | 不限 |  | [下载](https://beixiaocai.yuque.com/org-wiki-beixiaocai-vo72oa/xcms/e382620e4df52bd7628d3fd141a7112d) |

* [下载x86-Windows-ov版](https://beixiaocai.yuque.com/org-wiki-beixiaocai-vo72oa/xcms/333803623628302fe6f578cd3485e4be)
* [下载x86-Windows-ovtrt版](https://beixiaocai.yuque.com/org-wiki-beixiaocai-vo72oa/xcms/gyvtvcndflyppuhw)
* [下载x86-Ubuntu-ov版](https://beixiaocai.yuque.com/org-wiki-beixiaocai-vo72oa/xcms/944d5586badc8e93686afc522a4feece)
* [下载x86-Ubuntu-ovtrt版](https://beixiaocai.yuque.com/org-wiki-beixiaocai-vo72oa/xcms/2713611802e365950bc9c6fef5c6b118)
* [下载arm-Ubuntu-rk3588版](https://beixiaocai.yuque.com/org-wiki-beixiaocai-vo72oa/xcms/76dbf61f8b5f8ce67891dc3e3f36b686)
* [下载arm-昇腾版](https://beixiaocai.yuque.com/org-wiki-beixiaocai-vo72oa/xcms/644800c887eb14094e2154882b78e8fc)
* [下载x86其他版本](https://beixiaocai.yuque.com/org-wiki-beixiaocai-vo72oa/xcms/e382620e4df52bd7628d3fd141a7112d)
* [下载arm其他版本](https://beixiaocai.yuque.com/org-wiki-beixiaocai-vo72oa/xcms/e382620e4df52bd7628d3fd141a7112d)

## 使用手册
* [简介](https://beixiaocai.yuque.com/org-wiki-beixiaocai-vo72oa/xcms/e05dce83e5129785b9f316978a14b896)
* [版本历史](https://beixiaocai.yuque.com/org-wiki-beixiaocai-vo72oa/xcms/qchculv81t93orwh)
* [软件贴牌](https://beixiaocai.yuque.com/org-wiki-beixiaocai-vo72oa/xcms/e45770b681f5d0a2e0300b94672de1ae)
* [硬件推荐](https://beixiaocai.yuque.com/org-wiki-beixiaocai-vo72oa/xcms/5f5b8c534610b075a56f0dddea6f5bea)
* [软件启动配置](https://beixiaocai.yuque.com/org-wiki-beixiaocai-vo72oa/xcms/7ea49eddd8294dd0b66742647d76bb10)
* [软件性能优化](https://beixiaocai.yuque.com/org-wiki-beixiaocai-vo72oa/xcms/626c74072ae1bdc63e01a04002186a92)
* [咨询问题模板](https://beixiaocai.yuque.com/org-wiki-beixiaocai-vo72oa/xcms/4b66cc754328ce343eea09766b54c464)
* [FFmpeg推USB摄像头](https://beixiaocai.yuque.com/org-wiki-beixiaocai-vo72oa/xcms/0deb4194d8ad8f0ca437263dd40597c0)
* [FFmpeg推流模拟摄像头](https://beixiaocai.yuque.com/org-wiki-beixiaocai-vo72oa/xcms/60850e5f979a8cddc42d5fd4e81fc70f)
* [FFmpeg电脑桌面推流](https://beixiaocai.yuque.com/org-wiki-beixiaocai-vo72oa/xcms/00a95632b189aa5a4e5e6e4ffb2bbd40)
* [浏览器设置网页自动播放声音](https://beixiaocai.yuque.com/org-wiki-beixiaocai-vo72oa/xcms/404272bee98998c7f9217a0a54824a5a)

## 合作授权
* [x86架构版合作授权](https://beixiaocai.yuque.com/org-wiki-beixiaocai-vo72oa/xcms/xmm8h3dc78506ogy)
* [rk3588版合作授权](https://beixiaocai.yuque.com/org-wiki-beixiaocai-vo72oa/xcms/3c2075f1b0d934eac31b89f3f12383ee)
* [昇腾版合作授权](https://beixiaocai.yuque.com/org-wiki-beixiaocai-vo72oa/xcms/qd1ten0dr3t7tn7u)
* [定制版合作](https://beixiaocai.yuque.com/org-wiki-beixiaocai-vo72oa/xcms/ci0h3mahg4zoaa42)


<img width="720" alt="控制面板" src="https://gitee.com/Vanishi/images/raw/master/BXC_VideoAnalyzer_v4/v4.409/1.png">
<img width="720" alt="报警视频管理" src="https://gitee.com/Vanishi/images/raw/master/BXC_VideoAnalyzer_v4/v4.409/2.png">
<img width="720" alt="摄像头管理" src="https://gitee.com/Vanishi/images/raw/master/BXC_VideoAnalyzer_v4/v4.409/3.png">
<img width="720" alt="算法管理" src="https://gitee.com/Vanishi/images/raw/master/BXC_VideoAnalyzer_v4/v4.409/4.png">
<img width="720" alt="添加算法" src="https://gitee.com/Vanishi/images/raw/master/BXC_VideoAnalyzer_v4/v4.409/5.png">
<img width="720" alt="布控管理" src="https://gitee.com/Vanishi/images/raw/master/BXC_VideoAnalyzer_v4/v4.409/6.png">
<img width="720" alt="添加布控" src="https://gitee.com/Vanishi/images/raw/master/BXC_VideoAnalyzer_v4/v4.409/7.png">
<img width="720" alt="系统维护" src="https://gitee.com/Vanishi/images/raw/master/BXC_VideoAnalyzer_v4/v4.409/8.png">
<img width="720" alt="关于系统" src="https://gitee.com/Vanishi/images/raw/master/BXC_VideoAnalyzer_v4/v4.409/9.png">
