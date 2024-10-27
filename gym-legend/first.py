import gym
from gym import spaces
import numpy as np
import pyautogui
from stable_baselines3 import PPO
import Find_Pic  # 假设这是您的图片查找模块


class LegendGameEnv(gym.Env):
    def __init__(self):
        super(LegendGameEnv, self).__init__()

        # 定义状态空间：包含怪物的相对坐标
        self.observation_space = spaces.Box(low=-500, high=500, shape=(10, 2), dtype=np.float32)

        # 定义动作空间：8种移动 + 攻击
        self.action_space = spaces.Discrete(9)

        self.reference_point = (533, 309)  # 角色在屏幕中心
        self.reset()

    def reset(self):
        # 重置环境并返回初始状态
        return self._get_obs()

    def _get_obs(self):
        # 获取当前怪物相对于屏幕的坐标
        far_coordinates, close_coordinates = Find_Pic.find_and_process_targets()

        # 确保返回形状为 (10, 2) 的数组
        if len(far_coordinates) < 10:
            # 如果怪物少于10个，用零填充
            far_coordinates = np.array(far_coordinates + [[0, 0]] * (10 - len(far_coordinates)))
        else:
            far_coordinates = np.array(far_coordinates)[:10]  # 只取前10个怪物

        return far_coordinates



    def step(self, action):
        reward = 0
        done = False

        if action < 8:  # 移动
            direction = self._get_direction(action)
            self._move_character(direction)
        elif action == 8:  # 攻击
            reward += self.click_attack()

        # 更新观察
        obs = self._get_obs()

        # 判断是否没有怪物，如果是则结束
        if len(obs) == 0:
            done = True

        return obs, reward, done, {}

    def _get_direction(self, action):
        # 定义移动的目标坐标
        target_coordinates = {
            0: (544, 182),  # up
            1: (538, 495),  # down
            2: (350, 310),  # left
            3: (769, 303),  # right
            4: (382, 159),  # up_left
            5: (691, 173),  # up_right
            6: (388, 467),  # down_left
            7: (711, 435)  # down_right
        }
        return target_coordinates[action]

    def _move_character(self, target):
        # 使用右键点击并移动到指定坐标
        x, y = target
        pyautogui.mouseDown(button='right')
        pyautogui.moveTo(x, y, duration=0.5)
        pyautogui.mouseUp(button='right')
        print(f"Moving character to {target}")

    def click_attack(self):
        # 查找“自动挂机”标记并点击攻击
        zidong_tag = Find_Pic.find_image_on_screen('../legend-r/img/自动挂机.png')
        if zidong_tag:
            pyautogui.click(zidong_tag[0], zidong_tag[1])
            return 10  # 每次成功攻击的奖励
        return 0





# 训练模型
env = LegendGameEnv()
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)

# 保存模型
model.save("legend_agent_model")
print("Model saved as 'legend_agent_model'")
