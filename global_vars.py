# 缓存的模板匹配图像,避免每次都要进行读取和转换
template_mat_map = {}
# 角色在角色页中的位置
role_position = {
    1: (269, 233, 10, 10),
    2: (465, 237, 10, 10),
    3: (651, 241, 10, 10),
    4: (166, 524, 10, 10),
    5: (364, 529, 10, 10),
    6: (549, 526, 10, 10),
    7: (751, 525, 10, 10)
}

# 模板-关闭
模板_关闭_菜单 = '关闭_菜单'
模板_关闭_日常玩法 = '关闭_日常玩法'
# 模板-广告
模板_广告_前往商店 = '广告_前往商店'
模板_广告_快乐成长派对 = '广告_快乐成长派对'
模板_广告_日程管理 = '广告_日程管理'
模板_广告_王中王争霸战 = '广告_王中王争霸战'
模板_广告_首充福利 = '广告_首充福利'
模板_广告_25元 = '广告_25元'
# 模板-角色
模板_更改角色_主页 = '更改角色_主页'
模板_更改角色_主页_主力 = '更改角色_主页_主力'
模板_角色列表_游戏开始 = '角色列表_游戏开始'
模板_角色列表_第1页 = '角色列表_第1页'
模板_角色列表_第2页 = '角色列表_第2页'
模板_角色列表_第3页 = '角色列表_第3页'
模板_角色列表_第4页 = '角色列表_第4页'
模板_角色列表_第5页 = '角色列表_第5页'
# 角色页的页码
role_page_num = {
    1: 模板_角色列表_第1页,
    2: 模板_角色列表_第2页,
    3: 模板_角色列表_第3页,
    4: 模板_角色列表_第4页,
    5: 模板_角色列表_第5页
}
模板_通用_勾选框 = '通用_勾选框'

# 模板-桌面
模板_桌面_创建队伍 = '桌面_创建队伍'
# 模板-自动战斗
模板_自动战斗_主页 = '自动战斗_主页'
# 模板-菜单
模板_菜单_个人主页 = '菜单_个人主页'
# 模板-副本
模板_副本通用_日常玩法_主页 = '日常玩法_主页'
模板_副本通用_入场 = '副本_入场'
模板_副本通用_入场_已完成 = '副本_入场_已完成'
模板_副本通用_确定 = '副本_确定'
模板_副本通用_离开 = '副本_离开'
模板_副本通用_放弃 = '副本_放弃'
模板_副本通用_快速组队 = '副本_快速组队'
模板_副本通用_快速组队_已完成 = '副本_快速组队_已完成'

模板_材料副本_入口 = '材料副本_入口'
模板_材料副本_主页 = '材料副本_主页'
模板_精英副本_入口 = '精英副本_入口'
模板_精英副本_主页 = '精英副本_主页'
模板_周常副本_入口 = '周常副本_入口'
模板_周常副本_主页 = '周常副本_主页'

模板_远征队_入口 = '远征队_入口'
模板_远征队_主页 = '远征队_主页'
模板_远征队_副本内再次挑战 = '远征队_副本内再次挑战'
模板_远征队_副本内已完成 = '远征队_副本内已完成'

模板_公会_主页 = '公会_主页'
模板_公会_加入公会 = '公会_加入公会'
模板_公会_公会信息 = '公会_公会信息'
模板_公会_公会目录 = '公会_公会目录'

模板_邮件_主页 = '邮件_主页'
模板_邮件_通用 = '邮件_通用'
模板_邮件_个人 = '邮件_个人'
模板_邮件_全部领取 = '邮件_全部领取'
模板_邮件_确认 = '邮件_确认'
模板_邮件_勾选框 = '邮件_勾选框'
模板_邮件_确定 = '邮件_确定'
模板_邮件_删除 = '邮件_删除'
模板_邮件_已全部领取 = '邮件_已全部领取'
模板_邮件_无邮件 = '邮件_无邮件'

# 坐标
坐标_菜单 = (1220, 23, 30, 30)
坐标_菜单_日常玩法 = (1088, 260, 75, 75)
坐标_菜单_公会 = (826, 265, 70, 60)
坐标_菜单_邮件 = (1041, 20, 39, 26)

坐标_副本_入口 = (0, 142, 100, 100)

# 公会任务坐标
坐标_公会_签到奖励 = (1159, 110, 50, 20)
坐标_公会_任务入口 = (35, 477, 85, 25)
坐标_公会_全部领取 = (1123, 667, 85, 20)
坐标_公会_每周任务 = (448, 106, 90, 25)
坐标_公会_加入按钮 = (547, 353, 200, 140)
坐标_公会_快速加入 = (646, 668, 100, 30)
坐标_公会_确认加入 = (742, 515, 100, 30)

# 自动战斗坐标
坐标_自动战斗_领取 = (893, 357, 70, 30)

# 副本类型坐标
材料副本类型 = {
    '1': (60, 125, '射手村'),
    '2': (57, 197, '废弃都市'),
    '3': (53, 261, '阿里安特'),
    '4': (57, 328, '卡帕莱特'),
    '5': (64, 392, '神木村'),
    '6': (55, 460, '龙之峡谷'),
    '7': (64, 525, '玩具城'),
    '8': (53, 590, '武陵桃源')
}

坐标_远征队_扎昆 = (92, 133, 115, 40)
坐标_远征队_暗黑龙王 = (324, 133, 140, 32)
坐标_远征队_品克缤 = (586, 138, 102, 35)
坐标_远征队_堕落女皇希纳斯 = (817, 136, 139, 35)
坐标_远征队_魔王蝙蝠怪 = (1064, 136, 153, 34)
每日远征队 = {
    '1': (坐标_远征队_扎昆, 坐标_远征队_魔王蝙蝠怪),
    '2': (坐标_远征队_暗黑龙王, 坐标_远征队_堕落女皇希纳斯),
    '3': (坐标_远征队_扎昆, 坐标_远征队_品克缤),
    '4': (坐标_远征队_暗黑龙王, 坐标_远征队_魔王蝙蝠怪),
    '5': (坐标_远征队_品克缤, 坐标_远征队_堕落女皇希纳斯),
    '6': (坐标_远征队_扎昆, 坐标_远征队_暗黑龙王, 坐标_远征队_品克缤, 坐标_远征队_堕落女皇希纳斯, 坐标_远征队_魔王蝙蝠怪),
    '7': (坐标_远征队_扎昆, 坐标_远征队_暗黑龙王, 坐标_远征队_品克缤, 坐标_远征队_堕落女皇希纳斯, 坐标_远征队_魔王蝙蝠怪)
}
