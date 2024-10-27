import gym
from gym import spaces
import numpy as np
from stable_baselines3 import PPO


class LegendFixedPlayerEnv(gym.Env):
    def __init__(self):
        super(LegendFixedPlayerEnv, self).__init__()
        # 状态空间：包含怪物的相对坐标和角度
        self.observation_space = spaces.Box(low=-500, high=500, shape=(10, 3), dtype=np.float32)  # 每个怪物的x, y和角度

        # 动作空间：8种移动 + 攻击
        self.action_space = spaces.Discrete(9)

        # 初始化环境
        self.reset()

    def reset(self):
        # 初始化怪物位置并转换为相对坐标和角度
        self.monsters = [self._generate_monster() for _ in range(np.random.randint(1, 10))]
        return self._get_obs()

    def _generate_monster(self):
        x, y = np.random.randint(-500, 500, size=2)
        angle = np.arctan2(y, x)
        return np.array([x, y, angle])

    def _get_obs(self):
        # 返回每个怪物的相对x, y位置以及角度信息
        return np.array(self.monsters[:10])

    def step(self, action):
        reward = -0.1  # 每一步的时间惩罚
        done = False

        if action < 8:  # 移动
            movement = [[0, 10], [0, -10], [-10, 0], [10, 0], [-7, 7], [-7, -7], [7, 7], [7, -7]]
            self.monsters = [self._update_monster_position(monster, movement[action]) for monster in self.monsters]
        elif action == 8:  # 攻击
            reward += self._attack_monsters()

        # 检查是否怪物清理完毕
        if not self.monsters:
            done = True

        return self._get_obs(), reward, done, {}

    def _update_monster_position(self, monster, movement):
        # 更新怪物相对位置和角度信息
        monster[:2] -= movement  # 更新相对坐标
        monster[2] = np.arctan2(monster[1], monster[0])  # 计算相对角度
        return monster

    def _attack_monsters(self):
        reward = 0
        to_remove = []
        for i, monster in enumerate(self.monsters):
            if np.linalg.norm(monster[:2]) < 50:  # 距离小于50则攻击命中
                reward += 10
                to_remove.append(i)

        # 一次性击中多个怪物的奖励
        if len(to_remove) > 1:
            reward += 5 * len(to_remove)

        # 移除被击中的怪物
        self.monsters = [m for i, m in enumerate(self.monsters) if i not in to_remove]
        return reward


# 创建和训练模型
env = LegendFixedPlayerEnv()
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)
model.save("legend_fixed_player_model")
