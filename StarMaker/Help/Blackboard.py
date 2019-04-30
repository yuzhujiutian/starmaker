# coding=utf-8
# 项目3的最终代码

import random
import time


# 创建一个类，可实例化成具体的游戏角色
class Role:
    def __init__(self, name):
        self.name = name
        self.life = random.randint(100, 150)
        self.attack = random.randint(30, 50)


# 创建3个子类，可实例化为3个不同的职业

class Knight(Role):
    def __init__(self, name='【圣光骑士】'):
        Role.__init__(self, name)  # 继承了超类的构造函数，所以，self.name = name 不用重复写。
        self.life = int(self.life * 1.5)  # 这里有个小技巧：用 int 函数保证属性改变后，显示的数值仍是整值。
        self.attack = int(self.attack * 0.8)

    def fight_buff(self, opponent, str1, str2):
        if opponent.name == '【暗影刺客】':
            self.attack = round(self.attack * 1.5)
            print('『%s』【圣光骑士】对 『%s』【暗影刺客】说：“让无尽光芒制裁你的堕落！”' % (str1, str2))


class Assassin(Role):
    def __init__(self, name='【暗影刺客】'):
        Role.__init__(self, name)
        # print(self.life,self.attack)
        self.life = int(self.life * 0.8)
        self.attack = int(self.attack * 1.5)

    # 职业克制关系
    def fight_buff(self, opponent, str1, str2):
        if opponent.name == '【精灵弩手】':
            self.attack = round(self.attack * 1.5)
            print('『%s』【暗影刺客】对 『%s』【精灵弩手】说：“主动找死，就别怪我心狠手辣。”' % (str1, str2))


class Bowman(Role):
    def __init__(self, name='【精灵弩手】'):
        Role.__init__(self, name)
        self.life = int(self.life * 1.2)
        self.attack = int(self.attack * 1.2)

    def fight_buff(self, opponent, str1, str2):
        if opponent.name == '【圣光骑士】':
            self.attack = round(self.attack * 1.5)
            print('『%s』【精灵弩手】对 『%s』【圣光骑士】说：“骑着倔驴又如何？你都碰不到我衣服。”' % (str1, str2))


# 创建一个类，可生成3V3并展示：可分为：欢迎语→随机生成→展示角色
class Game:
    def __init__(self):
        self.players = []  # 存玩家顺序
        self.enemies = []  # 存敌人顺序
        self.score = 0  # 比赛积分
        self.i = 0  # 记轮次
        # 依次执行以下函数
        self.game_start()  # 欢迎语
        self.born_role()  # 随机生成6个角色
        self.show_role()  # 展示角色
        self.order_role()  # 排序并展示
        self.pk_role()  # 让双方 Pk 并展示结果
        self.show_result()  # 展示最终结局

    # 欢迎语
    def game_start(self):
        print('------------ 欢迎来到“炼狱角斗场” ------------')
        print('在昔日的黄昏山脉，奥卢帝国的北境边界上，有传说中的“炼狱角斗场”。')
        print('鲜血与战斗是角斗士的归宿，金钱与荣耀是角斗士的信仰！')
        print('今日，只要你【你的队伍】能取得胜利，你将获得一笔够花500年的财富。')
        time.sleep(2)
        print('将随机生成【你的队伍】和【敌人队伍】！')
        input('\n狭路相逢勇者胜，请按任意键继续。\n')

    # 随机生成6个角色
    def born_role(self):
        for i in range(3):
            self.players.append(random.choice([Knight(), Assassin(), Bowman()]))
            self.enemies.append(random.choice([Knight(), Assassin(), Bowman()]))

    # 展示角色
    def show_role(self):
        print('----------------- 角色信息 -----------------')
        print('你的队伍：')
        for i in range(3):
            print('『我方』%s 血量：%s  攻击：%s' %
                  (self.players[i].name, self.players[i].life, self.players[i].attack))
        print('--------------------------------------------')

        print('敌人队伍：')
        for i in range(3):
            print('『敌方』%s 血量：%s  攻击：%s' %
                  (self.enemies[i].name, self.enemies[i].life, self.enemies[i].attack))
        print('--------------------------------------------')
        input('请按回车键继续。\n')

    # 排序并展示
    def order_role(self):
        order_dict = {}
        for i in range(3):
            order = int(input('你想将 %s 放在第几个上场？(输入数字1~3)' % self.players[i].name))
            order_dict[order] = self.players[i]
        self.players = []
        for i in range(1, 4):
            self.players.append(order_dict[i])
        print('\n你的队伍出场顺序是：%s、%s、%s'
              % (self.players[0].name, self.players[1].name, self.players[2].name))
        print('敌人队伍出场顺序是：%s、%s、%s'
              % (self.enemies[0].name, self.enemies[1].name, self.enemies[2].name))

    # 让双方 Pk 并展示结果
    def pk_role(self):
        for i in range(3):
            print('\n----------------- 【第%s轮】 -----------------' % (i + 1))
            # 每一局开战前加buff
            self.players[i].fight_buff(self.enemies[i], '我方', '敌方')
            self.enemies[i].fight_buff(self.players[i], '敌方', '我方')
            input('\n战斗双方准备完毕，请按回车键继续。')
            print('--------------------------------------------')

            while self.players[i].life > 0 and self.enemies[i].life > 0:
                self.enemies[i].life -= self.players[i].attack
                self.players[i].life -= self.enemies[i].attack
                print('我方%s 发起了攻击，敌方%s 剩余血量 %s' %
                      (self.players[i].name, self.enemies[i].name, self.enemies[i].life))
                print('敌方%s 发起了攻击，我方%s 剩余血量 %s' %
                      (self.enemies[i].name, self.players[i].name, self.players[i].life))
                print('--------------------------------------------')
                time.sleep(1)
            if self.players[i].life <= 0 and self.enemies[i].life > 0:
                print('\n很遗憾，我方%s 挂掉了！' % (self.players[i].name))
                self.score -= 1
            elif self.players[i].life > 0 and self.enemies[i].life <= 0:
                print('\n恭喜，我方%s 活下来了。' % (self.players[i].name))
                self.score += 1
            else:
                print('\n我的天，他们俩都死了啊！')

    # 展示最终结局
    def show_result(self):
        input('\n请按回车查看最终结果。\n')
        if self.score > 0:
            print('【最终结果】\n你赢了，最终的财宝都归你了！')
        elif self.score == 0:
            print('【最终结果】\n你没有胜利，但也没有失败，在夜色中灰溜溜离开了奥卢帝国。')
        else:
            print('【最终结果】\n你输了。炼狱角斗场又多了几具枯骨。')


game = Game()

if __name__ == '__main__':
    pass
