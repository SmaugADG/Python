class Settings:
    '''存储所有设置'''
    def __init__(self):
        '''初始化游戏设置'''
        # 屏幕设置
        self.screen_width=800
        self.screen_height=900
        self.bg_color=(230,230,230)

        # 子弹设置
        self.bullet_speed=1.5
        # self.bullet_width=3
        self.bullet_width=400
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullet_allowed=3


        # 飞船设置
        self.ship_speed=1.5
        self.ship_limit=3

        # 外星人设置
        self.alien_speed=1.0
        self.fleet_drop_speed=100
        self.fleet_direction=1
