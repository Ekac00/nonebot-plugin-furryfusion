<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-RanFurryPic

_✨ 随机毛图 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/owner/nonebot-plugin-template.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-template">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-template.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

基于NoneBot2进行适配的兽云随机毛图插件

## 📖 介绍

兽云官方插件太复杂？功能太杂？看不懂？不兼容？损坏文件结构？
本插件使用官方<a href="https://console-docs.apipost.cn/preview/6bf01cfebd3e5f96/c4e20a5d1a5db86c?target_id=83fb4f89-221c-4196-bb85-4abf73af73af">API</a>进行编写，无需令牌，无需Token，即可使用随机毛图功能<br><br>
在开始前请先点一个免费的star吧谢谢啦~

<details>
<summary>买家秀</summary>

<img src="https://img2.imgtp.com/2024/05/10/U4xrcU7e.png">

</details>

## 💿 安装

<details open>
<summary>使用 nb-cli 安装（推荐）</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-RanFurryPic

</details>

<details>
<summary>使用PIP安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 输入安装命令

    pip install nonebot-plugin-RanFurryPic

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_RanFurryPic"]


</details>

## ⚙️ 配置

1.0版本暂无配置项，可即安即用。

## 🎉 使用
### 指令表
| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| 来只毛 | 群员 | 否 | 群聊 | 随机毛图 |
| furry | 群员 | 否 | 群聊 | 随机毛图 |
| 毛毛 | 群员 | 否 | 群聊 | 随机毛图 |

## TODO LIST

待解决问题:

 - [x] 使用httpx发送请求，避免线程堵塞(后期：艹这里让星火帮我改一次就过审核了讯飞nb！)
 - [ ] 自定义消息发送结果（指在`.env`中修改
 - [ ] 添加搜毛功能
