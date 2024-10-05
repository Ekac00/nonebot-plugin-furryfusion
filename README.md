<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-furryfusion

_✨ 兽聚动态 ✨_

</a>
<a href="https://github.com/Ekac00/nonebot-plugin-furryfusion/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/Ekac00/nonebot-plugin-furryfusion.svg" alt="license">
</a>
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-furryfusion">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-furryfusion.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python">

</div>

基于NoneBot2进行适配的兽聚动态查询插件

## 📖 介绍

本插件使用<a href="https://console-docs.apipost.cn/preview/fcba96ab381efa80/fdb51b00b68a9bbf?target_id=3a8b741e-9648-4469-8f47-98484378fdcf">兽云API</a>进行编写<del>别问我为什么不集成到随机毛图里，问就是报错（</del><br><br>
在开始前请先点一个star吧谢谢啦~<br>
使用过程中遇到任何问题请直接发issues，或到<a href="https://qm.qq.com/q/2OmiBhiPEA">qq群</a>里找糕蛋~

### 作者初中学业繁重，暂时停更
### 回来后会大规模更新本插件
### 可以先看看<a href="https://github.com/TheChenXI">这位老师</a>的<a href="https://github.com/TheChenXI/nonebot-plugin-witff">重制版~</a>

<details>
<summary>买家秀</summary>

<img src="https://img2.imgtp.com/2024/05/12/dQ97OBnd.png">

</details>

## 💿 安装

<details open>
<summary>使用 nb-cli 安装（推荐）</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-furryfusion

</details>

<details>
<summary>使用PIP安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 输入安装命令

    pip install nonebot-plugin-furryfusion

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_furryfusion"]


</details>

## ⚙️ 配置

暂无配置项，即安即用。

## 🎉 使用
### 指令表
| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| 兽聚动态 | 群员 | 否 | 群聊 | 查询兽聚动态（时间可能会有延迟） |

## TODO LIST

待解决问题:

 - [x] 使用httpx发送请求，避免线程堵塞
 - [x] 图片发送
 - [ ] <del>搜兽聚</del>
