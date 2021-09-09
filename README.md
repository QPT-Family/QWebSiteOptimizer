# QWebSiteOptimizer - Web站点速度选优工具
[![Downloads](https://static.pepy.tech/personalized-badge/qwebsite?period=total&units=international_system&left_color=grey&right_color=orange&left_text=Pypi%20User)](https://pepy.tech/project/qwebsite)
![GitHub forks](https://img.shields.io/github/forks/QPT-Family/QWebSiteOptimizer)
![GitHub Repo stars](https://img.shields.io/github/stars/QPT-Family/QWebSiteOptimizer)
![GitHub](https://img.shields.io/github/license/QPT-Family/QWebSiteOptimizer)
![](https://img.shields.io/badge/支持系统-Win/Linux/MAC-9cf)
  
在访问GitHub等网站时，DNS解析到的IP地址可能并不是最快，过慢的节点会严重影响我们的访问情况，故制作出这样的工具来进一步优化网络质量。  

* 由于该方案并非为VPN等方式进行的速度优化，以下几点需要您注意：
  1. 后续访问对应网站时仍可能需要您重新启动该程序进行优化。
  2. 优化情况取决与您的DNS配置情况以及网络本身质量，必要时请自行搜索如何修改本机DNS。
  3. 这些方式并不如专有VPN稳定，也并非科学上网，仅仅是速度优化而已。换句话就是政策不允许访问的依旧不会让您访问。

* 目前仅提供修改Hosts方式，后续版本将增加镜像源加速功能。

> 本程序源码完全开源开放，默认仅优化GitHub站点，后续将提供自定义网站优化教程。

## 安装方式

```
python -m pip install qwebsite
```
or
```
python -m pip install qwebsite -i https://mirrors.bfsu.edu.cn/pypi/web/simple
```
## 使用教程

还没做GUI和镜像源优化方式，目前仅提供以下操作，勉强够用  

* 优化命令  
  * Windows  
  ```
  python -m qwebsite
  ```
  * Linux or MacOS  
  ```
  sudo python -m qwebsite
  ```
* 恢复命令  
  * Windows[建议管理员模式运行]  
  ```
  python -m qwebsite -r True
  ```
  * Linux or MacOS  
  ```
  sudo python -m qwebsite -r True
  ```

## 开源协议
本项目使用GNU LESSER GENERAL PUBLIC LICENSE(LGPL)开源协议。
