# objective is to get the cart to the flag.
# for now, let's just move randomly:

import gym
import numpy as np

env = gym.make("MountainCar-v0")
env.reset()
for _ in range(100000):
    env.render()
    env.step(env.action_space.sample()) # take a random action
env.close()

