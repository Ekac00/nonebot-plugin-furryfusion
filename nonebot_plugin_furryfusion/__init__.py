import httpx
from nonebot import require
require("nonebot_plugin_htmlrender")
from nonebot_plugin_htmlrender import text_to_pic
from PIL import Image
import io
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.plugin import on_command

fusion_activity = on_command("兽聚动态", priority=10, block=True)

@fusion_activity.handle()
async def fusion_activity_function():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    url = "https://api.furryfusion.net/service/activity"
    async with httpx.AsyncClient() as client:
        url_get = await client.get(url, headers=headers)
    # getapi
    url_json = url_get.json()
    # 获取返回json
    data = url_json["data"]
    # 取json中的data值
    data_len = len(data)
    # 获取json中的data值长度
    # 以下循环取值
    message = ""
    for num in range(data_len):
        title = data[num]["title"]
        name = data[num]["name"]
        state_num = data[num]["state"]
        state_main = ["活动结束", "预告中", "售票中", "活动中", "活动取消"]
        group_json = data[num]["groups"][0]
        # 未取值
        address = data[num]["address"]
        time_day = data[num]["time_day"]
        time_start = data[num]["time_start"]
        time_end = data[num]["time_end"]
        state = state_main[state_num]
        # picture 未写
        message = message + f"\n--------------------\n兽聚名称：{title}\n兽聚主题：{name}\n兽聚状态：{state}\n兽聚Q群：{group_json}\n兽聚地址：{address}\n举办天数：{str(time_day)}天\n举办时间：{time_start}~{time_end}\n--------------------\n"
    
    pic = await text_to_pic(text=message)
    a = Image.open(io.BytesIO(pic))
    a.save("temp.png", format="PNG")
    await fusion_activity.finish("\n====兽聚动态====" + MessageSegment.image(pic) + "====兽聚动态====", at_sender=True)
