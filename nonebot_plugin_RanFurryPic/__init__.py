from nonebot.plugin import on_command
from nonebot import logger
from nonebot.adapters.onebot.v11 import MessageSegment
import requests
from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name="nonebot-plugin-RanFurryPic",
    description="基于NoneBot2进行适配的兽云随机毛图插件",

    type="application",
    # 发布必填，当前有效类型有：`library`（为其他插件编写提供功能），`application`（向机器人用户提供功能）。

    homepage="https://github.com/Ekac00/nonebot-plugin-RanFurryPic/",
    # 发布必填。

    supported_adapters={"~onebot.v11", "~fastapi"},
    # 支持的适配器集合，其中 `~` 在此处代表前缀 `nonebot.adapters.`，其余适配器亦按此格式填写。
    # 若插件可以保证兼容所有适配器（即仅使用基本适配器功能）可不填写，否则应该列出插件支持的适配器。
)

furry = on_command("来只毛", aliases={"毛毛", "furry"}, priority=10, block=True)

@furry.handle()
async def handle_get_pic():
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    # 发送图片ID请求
    id_url = "https://cloud.foxtail.cn/api/function/random?name=&type="
    pic_id = ""
    id_response = requests.get(id_url, headers=headers)
    if id_response.status_code == 200:
        pic_json = id_response.json()
        pic_id = pic_json["picture"]["picture"]
        logger.success(f"状态码:{id_response.status_code}\n原始内容:{id_response.text}\n图片ID:{pic_id}")
    else:
        logger.error(f"请求失败!\n状态码:{id_response.status_code}")
        furry.finish(f"请求失败!\n状态码:{id_response.status_code}")

    # 发送图片请求
    pic_url = "https://cloud.foxtail.cn/api/function/pictures?picture=" + pic_id
    pic_id_url = ""
    pic_response = requests.get(pic_url, headers=headers)
    if pic_response.status_code == 200:
        url_json = pic_response.json()
        pic_id_url = url_json["url"]
        logger.success(f"状态码:{pic_response.status_code}\n原始内容:{pic_response.text}\n图片url:{pic_id_url}")
        # await furry.finish(pic_id_url)
    else:
        logger.error(f"请求失败!\n状态码:{pic_response.status_code}")
        furry.finish(f"请求失败!\n状态码:{pic_response.status_code}")

    # 发送图片
    name = pic_json["picture"]["name"]
    suggest = pic_json["picture"]["suggest"]
    await furry.finish(MessageSegment.image(pic_id_url) + f"好的嗷呜～\n毛毛名称:{name}\n留言:{suggest}\n图片UID:{pic_id}")