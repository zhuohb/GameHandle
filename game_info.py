# 单角色模式,刷完就退出
SINGLE_ROLE_MODEL = 'single'
# 多角色模式,轮流刷完所有角色
MULTIPLE_ROLE_MODEL = 'multiple'


class GlobalConfig:
    """
    全局配置,只会执行一次
    """

    def __init__(self):
        # 是否每日签到
        self.isMrqd = False
        # 是否宠物加油
        self.isCwjy = False
        # 是否领取每周成长
        self.isLqMzczrw = False
        # 是否领取通用邮件
        self.isLqTyyj = False


class RoleConfig:
    """
    角色配置,个性化每个角色的配置
    """

    def __init__(self):
        # 是否公会签到
        self.isGhqd = False
        # 是否公会任务领取
        self.isGhrwlq = False
        # 是否公会建筑升级
        self.isGhjzsj = False
        # 是否领取每日成长
        self.isLqMrczrw = False
        # 是否领取个人邮件
        self.isLqGryj = False
        # 是否执行材料副本
        self.isClfb = False
        # 选择材料副本类型,0为默认
        self.selectClfbType = '0'
        # 是否执行精英副本
        self.isJyfb = False
        # 选择精英副本类型,0为默认
        self.selectJyfbType = '0'
        # 是否执行周常副本
        self.isZcfb = False
        # 选择周常副本类型,0为默认
        self.selectZcfbType = '0'
        # 是否执行金钩海兵王
        self.isJghbw = False
        # 是否执行奈特的金字塔
        self.isNtdjzt = False
        # 选择奈特的金字塔类型,0为默认
        self.selectNtdjztType = '0'
        # 是否执行武陵道场
        self.isWldc = False
        # 是否执行唐云的料理店
        self.isTydlld = False
        # 是否执行怪物乐园
        self.isGwly = False
        # 选择怪物乐园类型,0为默认
        self.selectGwlyType = '0'


class GameInfo:
    """
    统筹所有配置信息
    """

    def __init__(self, role_total, current_role_index, global_config: GlobalConfig, role_config_list: list[RoleConfig]):
        # 每页固定角色数量
        self.rolePerPageCount = 7
        # 角色总数,从1开始.从0还刷鸡毛
        self.roleTotal = role_total
        # 当前角色索引,从1开始
        self.currentRoleIndex = current_role_index
        # 全局配置
        self.globalConfig = global_config
        # 所有角色的配置,数量要和当前角色索引一致
        self.roleConfigList = role_config_list
