from src import DQN_implementation as dqn
from os import remove
from glob import glob

identifier = "CartPole_q1"

# start training
dqn.main(env_name="CartPole-v0", identifier=identifier, model_name="linear", max_iteration=1000000, epsilon=0.5, epsilon_decay=4.5e-6,
         epsilon_min=0.05, interval_iteration=10000, gamma=0.99, test_size=20, learning_rate=0.002,
         use_replay_memory=False, memory_size=None, burn_in=None)
