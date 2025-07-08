import nonebot
from nonebot.adapters.onebot.v11 import Adapter as onebot11Adapter   # 避免重复命名
from pathlib import Path
# 初始化 NoneBot
nonebot.init()

# 注册适配器
driver = nonebot.get_driver()
driver.register_adapter(onebot11Adapter)
# driver.register_adapter(ConsoleBotAdapter)
# 在这里加载插件
# nonebot.load_builtin_plugins("echo")  # 内置插件
# nonebot.load_plugin("thirdparty_plugin")  # 第三方插件
# nonebot.load_plugins("awesome_bot/plugins")  # 本地插件

nonebot.load_plugin(Path("./plugins/SJsystem/RandSJ.py"))
nonebot.load_plugin(Path("./plugins/Chat/chat.py"))
# nonebot.load_plugin(Path("./plugins/Fluffle/Fluffle.py"))



if __name__ == "__main__":
    nonebot.run()