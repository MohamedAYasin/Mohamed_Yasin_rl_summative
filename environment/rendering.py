# environment/rendering.py
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Color definitions 
COLORS = {
    'background': (0.0, 1.0, 0.0),              # White background
    'cell': (0.4, 0.2, 0.7),                    # Light purple cells
    'grid': (0.8, 0.7, 0.9), 
    'agent_body': (0.0, 0.0, 1.0),              # Blue agent body
    'agent_head': (1.0, 1.0, 0.60),          
    'school': (0.2, 0.6, 0.2)                   # School (green)
}

# Global variables for textures
SCHOOL_TEXTURE = None
BOOK_TEXTURE = None  # Added for the book agent

def load_texture(image_path):
    """Loads an image as an OpenGL texture without flipping it, and with transparency enabled."""
    img = pygame.image.load(image_path) 
    img = img.convert_alpha()       
    img_data = pygame.image.tostring(img, "RGBA", True)
    width, height = img.get_size()

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    # Set texture parameters for wrapping and filtering
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    return texture_id

def draw_textured_rect(x, y, w, h, texture):
    """Draws a rectangle with the given texture and enables alpha blending."""
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture)
    
    # Enable alpha blending
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    glColor3f(1, 1, 1) 
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex2f(x, y)
    glTexCoord2f(1, 0); glVertex2f(x + w, y)
    glTexCoord2f(1, 1); glVertex2f(x + w, y + h)
    glTexCoord2f(0, 1); glVertex2f(x, y + h)
    glEnd()
    
    glDisable(GL_BLEND)
    glDisable(GL_TEXTURE_2D)

def draw_filled_rect(x, y, w, h, color):
    """Draws a filled rectangle."""
    glColor3f(*color)
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x+w, y)
    glVertex2f(x+w, y+h)
    glVertex2f(x, y+h)
    glEnd()

def draw_circle(cx, cy, radius, color, segments=32):
    """Draws a filled circle."""
    glColor3f(*color)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(cx, cy)
    for i in range(segments+1):
        angle = 2 * math.pi * i / segments
        glVertex2f(cx + math.cos(angle) * radius, cy + math.sin(angle) * radius)
    glEnd()

def render_school_env(env, screen):
    """
    Renders the environment onto the provided 'screen'.
    Assumes that 'screen' has already been created (e.g., via pygame.display.set_mode).
    """
    global SCHOOL_TEXTURE, BOOK_TEXTURE

    # Load school texture if not already loaded
    if SCHOOL_TEXTURE is None:
        SCHOOL_TEXTURE = load_texture("school.jpg")  

    # Load book texture if not already loaded
    if BOOK_TEXTURE is None:
        BOOK_TEXTURE = load_texture("study.png")  # Ensure book.png is in 'environment/'

    window_size = screen.get_width()  
    cell_size = window_size / env.grid_size

    # Clear the buffer with the background color.
    glClearColor(*COLORS['background'], 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluOrtho2D(0, env.grid_size, 0, env.grid_size)

    # Drawing cells
    for i in range(env.grid_size):
        for j in range(env.grid_size):
            draw_filled_rect(i, j, 1, 1, COLORS['cell'])
    
    # Drawing grid lines.
    glColor3f(*COLORS['grid'])
    glLineWidth(2)
    glBegin(GL_LINES)
    for i in range(env.grid_size + 1):
        glVertex2f(i, 0)
        glVertex2f(i, env.grid_size)
    for j in range(env.grid_size + 1):
        glVertex2f(0, j)
        glVertex2f(env.grid_size, j)
    glEnd()

    # Drawing school
    sx, sy = env.school_pos  
    draw_textured_rect(sx + 0.1, sy + 0.1, 0.8, 0.8, SCHOOL_TEXTURE)

    # Drawing agent as a book instead of a circle
    ax, ay = env.agent_pos
    draw_textured_rect(ax + 0.2, ay + 0.1, 0.6, 0.6, BOOK_TEXTURE)  # Use book image
    
    pygame.display.flip()
    pygame.time.wait(100)