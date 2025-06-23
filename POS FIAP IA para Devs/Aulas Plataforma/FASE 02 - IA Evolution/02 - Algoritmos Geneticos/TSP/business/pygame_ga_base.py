import pygame
import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from typing import List, Tuple

# Global variables for Genetic Algorithm control

# Pygame settings
WIDTH, HEIGHT = 800, 400
NODE_RADIUS = 10
FPS = 30
PLOT_X_OFFSET = 450

# Genetic Algorithm parameters
N_CITIES = 15
POPULATION_SIZE = 100
MUTATION_PROBABILITY = 0.5

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

matplotlib.use("Agg")


class PyGameGA:
    """
    A base class for implementing Genetic Algorithms with Pygame visualization.
    It provides methods for initializing the Pygame display, handling events,
    drawing cities and paths, and plotting fitness values.
    """

    def initialize_pygame_display(self):
        """
        Initializes the Pygame display and sets up the screen.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Genetic Algorithm Visualization - TSP Solver")
        self.clock = pygame.time.Clock()

    def update_pygame_running(self, running: bool = True) -> bool:
        """
        Handles Pygame events to check if the application should continue running.

        Parameters:
        - running (bool): A boolean indicating whether the application is currently running.

        Returns:
        bool: A boolean indicating whether the application should continue running based on user input.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return False
        return running

    def update_pygame_display(self, best_fitness_values, best_solution, population) -> bool:
        """
        Updates the Pygame display with the current state of the genetic algorithm.

        Parameters:
        - best_fitness_values (list): A list of the best fitness values for each generation.
        - best_solution (list): The best solution found by the genetic algorithm.
        - population (list): The current population of solutions.

        Returns:
        bool: Always returns True.
        """
        self.screen.fill(WHITE)
        self.draw_plot(self.screen, list(range(len(best_fitness_values))),
                       best_fitness_values, y_label="Fitness - Distance (pxls)")

        self.draw_cities(self.screen, self.cities_locations, RED, NODE_RADIUS)
        self.draw_paths(self.screen, best_solution, BLUE, width=3)
        self.draw_paths(self.screen, population[1], rgb_color=(128, 128, 128), width=1)

    def flip_pygame_display(self) -> None:
        """
        Update the Pygame display to show the current frame.
        """
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    def close_pygame_display(self) -> None:
        """
        Close the Pygame display and quit Pygame.
        """
        pygame.quit()
        sys.exit()

    def draw_cities(self, screen: pygame.Surface, cities_locations: List[Tuple[int, int]], rgb_color: Tuple[int, int, int], node_radius: int) -> None:
        """
        Draws circles representing cities on the given Pygame screen.

        Parameters:
        - screen (pygame.Surface): The Pygame surface on which to draw the cities.
        - cities_locations (List[Tuple[int, int]]): List of (x, y) coordinates representing the locations of cities.
        - rgb_color (Tuple[int, int, int]): Tuple of three integers (R, G, B) representing the color of the city circles.
        - node_radius (int): The radius of the city circles.
        """
        for city_location in cities_locations:
            pygame.draw.circle(screen, rgb_color, city_location, node_radius)

    def draw_plot(self, screen: pygame.Surface, x: list, y: list, x_label: str = 'Generation', y_label: str = 'Fitness') -> None:
        """
        Draw a plot on a Pygame screen using Matplotlib.

        Parameters:
        - screen (pygame.Surface): The Pygame surface to draw the plot on.
        - x (list): The x-axis values.
        - y (list): The y-axis values.
        - x_label (str): Label for the x-axis (default is 'Generation').
        - y_label (str): Label for the y-axis (default is 'Fitness').
        """
        fig, ax = plt.subplots(figsize=(4, 4), dpi=100)
        ax.plot(x, y)
        ax.set_ylabel(y_label)
        ax.set_xlabel(x_label)
        plt.tight_layout()

        canvas = FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_argb()

        size = canvas.get_width_height()
        surf = pygame.image.fromstring(raw_data, size, "ARGB")
        screen.blit(surf, (0, 0))

    def draw_paths(self, screen: pygame.Surface, path: List[Tuple[int, int]], rgb_color: Tuple[int, int, int], width: int = 1):
        """
        Draw a path on a Pygame screen.

        Parameters:
        - screen (pygame.Surface): The Pygame surface to draw the path on.
        - path (List[Tuple[int, int]]): List of tuples representing the coordinates of the path.
        - rgb_color (Tuple[int, int, int]): RGB values for the color of the path.
        - width (int): Width of the path lines.
        """
        pygame.draw.lines(screen, rgb_color, True, path, width=width)

    def draw_text(self, screen: pygame.Surface, text: str, color: pygame.Color) -> None:
        """
        Draw text on a Pygame screen.

        Parameters:
        - screen (pygame.Surface): The Pygame surface to draw the text on.
        - text (str): The text to be displayed.
        - color (pygame.Color): The color of the text.
        """
        pygame.font.init()

        font_size = 15
        my_font = pygame.font.SysFont('Arial', font_size)
        text_surface = my_font.render(text, False, color)

        cities_locations = []  # Assuming you have this list defined somewhere
        text_position = (np.average(np.array(cities_locations)[:, 0]), HEIGHT - 1.5 * font_size)

        screen.blit(text_surface, text_position)

