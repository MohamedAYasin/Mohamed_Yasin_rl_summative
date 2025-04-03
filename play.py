import pygame
import time
import random
from environment.custom_env import EducationHubEnv  # Import the custom environment
from environment.rendering import render_school_env  # Import rendering function

class GameState:
    def __init__(self):
        self.total_reward = 0.0
        self.steps = 0
        self.episode = 1
        self.ep_start_time = time.time()
        self.exploration_steps = 7  # Ensure the agent moves up and down before heading to school
        self.exploring = True  # Start in exploration mode

def log_episode(state):
    """Log episode statistics to console."""
    elapsed = time.time() - state.ep_start_time
    avg_reward = state.total_reward / state.steps if state.steps > 0 else 0
    summary = (
        f"Episode {state.episode} finished: Total Reward: {state.total_reward:.2f} | "
        f"Steps: {state.steps} | Average Reward per Step: {avg_reward:.2f} | "
        f"Episode Duration: {elapsed:.2f} seconds"
    )
    print(summary)
    print("-" * 60)
    return summary

def get_exploratory_action(env):
    """Move randomly up or down to explore different columns."""
    return random.choice([2, 3])  # Move Up or Down

def get_greedy_action(env):
    """Choose an action that moves the agent toward the school."""
    ax, ay = env.agent_pos
    sx, sy = env.school_pos

    if ax < sx:
        return 1  # Move Right
    elif ax > sx:
        return 0  # Move Left
    elif ay < sy:
        return 2  # Move Up
    elif ay > sy:
        return 3  # Move Down
    return 1  

def play():
    
    pygame.init()
    window_size = 500
    screen = pygame.display.set_mode((window_size, window_size), pygame.OPENGL | pygame.DOUBLEBUF)
    pygame.display.set_caption("Education Hub - RL Agent Navigation")

    env = EducationHubEnv(grid_size=5, max_steps=100, render_mode='human')
    obs, _ = env.reset()
    clock = pygame.time.Clock()
    state = GameState()

    running = True
    while running:
        clock.tick(1)  
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # action based on exploration phase
        if state.exploring:
            action = get_exploratory_action(env)
            state.exploration_steps -= 1
            if state.exploration_steps <= 0:
                state.exploring = False  # Switch to goal-seeking
        else:
            action = get_greedy_action(env)
        
        obs, reward, terminated, truncated, _ = env.step(action)
        state.total_reward += reward
        state.steps += 1

        # Render the environment
        render_school_env(env, screen)

        if terminated or truncated:
            log_episode(state)
            obs, _ = env.reset()
            state.episode += 1
            state.total_reward = 0.0
            state.steps = 0
            state.ep_start_time = time.time()
            state.exploration_steps = 7  
            state.exploring = True  

    pygame.quit()

if __name__ == '__main__':
    play()
