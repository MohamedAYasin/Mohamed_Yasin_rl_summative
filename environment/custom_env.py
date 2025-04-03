import gym
from gym import spaces
import numpy as np

class EducationHubEnv(gym.Env):
    """Custom reinforcement learning environment where an agent navigates to a school."""

    def __init__(self, grid_size=5, max_steps=100, render_mode=None):
        super(EducationHubEnv, self).__init__()
        self.grid_size = grid_size
        self.max_steps = max_steps
        self.steps = 0

        # Action space: 0 = Left, 1 = Right, 2 = Up, 3 = Down
        self.action_space = spaces.Discrete(4)

        # Observation space (Agent's position in a grid)
        self.observation_space = spaces.Box(low=0, high=self.grid_size - 1, shape=(2,), dtype=np.int32)

        # Initialize positions
        self.agent_pos = (0, 0)
        self.school_pos = (grid_size - 1, grid_size - 1)

    def reset(self, seed=None, options=None):
        """Reset environment to initial state."""
        self.steps = 0
        self.agent_pos = (0, 0)  # Start at bottom-left
        return self._get_obs(), {}

    def step(self, action):
        """Move the agent in the environment based on the selected action."""
        self.steps += 1
        terminated = False
        truncated = self.steps >= self.max_steps
        reward = -0.1  # Small penalty for each step to encourage efficiency

        x, y = self.agent_pos
        if action == 0 and x > 0:        # Move Left
            x -= 1
        elif action == 1 and x < self.grid_size - 1:  # Move Right
            x += 1
        elif action == 2 and y < self.grid_size - 1:  # Move Up
            y += 1
        elif action == 3 and y > 0:        # Move Down
            y -= 1

        self.agent_pos = (x, y)

        # Check if the agent reached the school
        if self.agent_pos == self.school_pos:
            reward += 10  # Large reward for reaching the goal
            terminated = True

        return self._get_obs(), reward, terminated, truncated, {}

    def _get_obs(self):
        """Return the agent's current position as the observation."""
        return np.array(self.agent_pos, dtype=np.int32)

    def render(self):
        """Rendering is handled externally in rendering.py."""
        pass