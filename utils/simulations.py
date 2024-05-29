import time
import numpy as np
import random as rnd

def simulate_episode(env, policy, steps, sleep_between_frames=0.3, print_info=True):
    obs, _ = env.reset()
    env.render()

    for i in range(steps):
        if print_info:
            print(f"obs: ", obs)
        actions = policy.compute_actions(obs)
        #actions = {agent: np.array([rnd.random()*2-1, rnd.random()*2-1, 1.0], np.float32) for agent in obs.keys()}
        #actions = {agent: env.action_space.sample() for agent in obs.keys()}
        obs, reward, _, _, _ = env.step(actions)
        env.render()
        
        if print_info:
            print(f"action: ", actions)
            print(f"reward: ", reward, "\n")
        time.sleep(sleep_between_frames)

def simulate_random_episode(env, steps, sleep_between_frames=0.3, print_info=True):
    obs, _ = env.reset()
    env.render()

    action_space = env.action_space
    for i in range(steps):
        if print_info:
            print(f"obs: ", obs)
        actions = {agent: action_space.sample() for agent in obs.keys()}
        obs, reward, _, _, _ = env.step(actions)
        env.render()
        if print_info:
            print(f"action: ", actions)
            print(f"reward: ", reward, "\n")
        time.sleep(sleep_between_frames)

def ppo_result_format(result):
    return (f"iteration [{result['training_iteration']}] => " +
          f"episode_reward_mean: {result['sampler_results']['episode_reward_mean']}, " +
          f"episode_len_mean: {result['sampler_results']['episode_len_mean']}, " +
          f"agent_steps_trained: {result['info']['num_agent_steps_trained']}, " +
          f"env_steps_trained: {result['info']['num_env_steps_trained']}, " + 
          f"entropy: {result['info']['learner']['default_policy']['learner_stats']['entropy']}, " +
          f"learning_rate: {result['info']['learner']['default_policy']['learner_stats']['cur_lr']}")