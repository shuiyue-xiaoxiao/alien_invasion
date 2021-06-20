class Settings:
    """存储游戏《外星人入侵》中所有的类"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 250, 210)
        self.bullet_allowed = 3

        # 速度设置
        self.ship_speed = 1.0