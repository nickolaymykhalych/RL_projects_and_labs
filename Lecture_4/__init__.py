import numpy as np
import gym
from Lecture_4.evolution_algorithms import Evolution_algorithms
from Lecture_4.cartpole_solution import f

if __name__ == '__main__':
    API_KEY = "sk_yy5S2r1SmOL5ZZcNuL5IA"

    env = gym.make('CartPole-v0')
    env = gym.wrappers.Monitor(env, 'cartpole', force=True)
    # env.reset()
    alg = Evolution_algorithms(f, env).cem(n_iter=6)

    env.close()
    gym.upload('cartpole', api_key=API_KEY)