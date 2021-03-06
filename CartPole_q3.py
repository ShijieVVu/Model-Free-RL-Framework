from src import DQN_implementation as dqn
from os import remove
from glob import glob

identifier = "CartPole_q3"

# start training
dqn.main(env_name="CartPole-v0", identifier=identifier,model_name="MLP", max_iteration=100000, epsilon=0.5, epsilon_decay=4.5e-4,
         epsilon_min=0.05, interval_iteration=1000, gamma=0.99, test_size=20, learning_rate=0.0001,
         use_replay_memory=True, memory_size=50000, burn_in=10000)
