import httpx
from nonebot.plugin import on_command
from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name="nonebot-plugin-furryfusion",
    description="基于NoneBot2进行适配的兽聚动态查询插件",
    usage="使用“兽聚动态”查询最新兽聚",

    type="application",
    # 发布必填，当前有效类型有：`library`（为其他插件编写提供功能），`application`（向机器人用户提供功能）。

    homepage="https://github.com/Ekac00/nonebot-plugin-furryfusion",
    # 发布必填。

    supported_adapters={"~onebot.v11"},
    # 支持的适配器集合，其中 `~` 在此处代表前缀 `nonebot.adapters.`，其余适配器亦按此格式填写。
    # 若插件可以保证兼容所有适配器（即仅使用基本适配器功能）可不填写，否则应该列出插件支持的适配器。
)

fusion_activity = on_command("兽聚动态", priority=10, block=True)

@fusion_activity.handle()
async def fusion_activity_function():
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    url = "https://api.furryfusion.net/service/activity"
    params = {}
    url_get = httpx.get(url, params=params, headers=headers, cookies=None, proxies=None)
    #getapi
    url_json = url_get.json()
    #获取返回json
    data = url_json["data"]
    #取json中的data值
    data_len = len(data)
    #获取json中的data值长度
    #以下循环取值
    message = ""
    for num in range(data_len):
        title = data[num]["title"]
        name = data[num]["name"]
        state_num = data[num]["state"]
        state_main = ["活动结束","预告中","售票中","活动中","活动取消"]
        group_json = data[num]["groups"][0]
        #未取值
        address = data[num]["address"]
        time_day = data[num]["time_day"]
        time_start = data[num]["time_start"]
        time_end = data[num]["time_end"]
        state = state_main[state_num]
        #picture 未写
        message = message + f"\n--------------------\n兽聚名称：{title}\n兽聚主题：{name}\n兽聚状态：{state}\n兽聚Q群：{group_json}\n兽聚地址：{address}\n举办天数：{str(time_day)}天\n举办时间：{time_start}~{time_end}\n--------------------\n"

    message_end = "====兽聚动态====" + message + "====兽聚动态===="
    await fusion_activity.finish(message_end, at_sender=True)
