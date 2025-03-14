# Install: pip install stable-baselines3 gym pandas yfinance
import gym
from gym import spaces
import numpy as np
from stable_baselines3 import PPO
import yfinance as yf

class TradingEnv(gym.Env):
    def __init__(self, data):
        super(TradingEnv, self).__init__()
        self.data = data
        self.action_space = spaces.Discrete(3)  # Buy, Sell, Hold
        self.observation_space = spaces.Box(low=0, high=np.inf, shape=(4,), dtype=np.float32)
        self.current_step = 0
        self.balance = 10000
        self.position = 0

    def reset(self):
        self.current_step = 0
        self.balance = 10000
        self.position = 0
        return self._get_obs()

    def step(self, action):
        price = self.data.iloc[self.current_step]["Close"]
        if action == 0 and self.balance >= price:  # Buy
            self.position += 1
            self.balance -= price
        elif action == 1 and self.position > 0:  # Sell
            self.position -= 1
            self.balance += price

        self.current_step += 1
        done = self.current_step >= len(self.data) - 1
        reward = self.balance + self.position * price - 10000  # Profit
        return self._get_obs(), reward, done, {}

    def _get_obs(self):
        return np.array([self.data.iloc[self.current_step]["Close"], self.balance, self.position, self.current_step], dtype=np.float32)

# Load historical data
data = yf.download("BTC-USD", start="2024-01-01", end="2025-03-13")
env = TradingEnv(data)
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)

# Backtest
obs = env.reset()
for _ in range(len(data)):
    action, _ = model.predict(obs)
    obs, reward, done, _ = env.step(action)
    if done:
        break
print(f"Final Balance: {env.balance}")