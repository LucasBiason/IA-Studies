
import pygame
import pylab
import sys
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg


WIDTH, HEIGHT = 800, 400
FPS = 10

matplotlib.use("Agg")


class PyGameGA:
    
    def initialize_pygame_display(self):
        """
        Initializes the Pygame display and sets up the screen.
        """
        pygame.init()
        self.window_size = (WIDTH, HEIGHT)
        self.screen = pygame.display.set_mode(self.window_size )
        pygame.display.set_caption("Genetic Algorithm Visualization - Camouflage Solver")
        self.clock = pygame.time.Clock()
        
    def update_pygame_running(self, running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False  # Quit the game when the 'q' key is pressed
                elif event.key == pygame.K_KP1:
                    self.target_color[0] += 1
                    print(self.target_color)
        return running
    
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
        
    def draw_plot(self, x, y, x_label = 'Generation', y_label = 'Fitness'):
        fig = pylab.figure(
            figsize=[4, 4], # Inches
            dpi=100, # 100 dots per inch, so the resulting buffer is 400x400 pixels
        )
        ax = fig.gca()
        ax.plot(x, y)

        canvas = FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_argb()
        size = canvas.get_width_height()
        surf = pygame.image.fromstring(raw_data, size, "ARGB")
        self.screen.blit(surf, (0,0))
        
    def draw_squares(self, population):
        # Define the number of rows and columns in the matrix
        n = 5  # Change this value to set the size of the matrix (e.g., 5x5)
        # Define the size oqf each square and the distance between squares
        square_size = 50
        distance_between_squares = 10
        x_offset = 450
        y_offset = 50
        # Calculate the total size of the matrix
        matrix_size = n * (square_size + distance_between_squares) - distance_between_squares
        i=0
        # Draw the matrix of squares
        for row in range(n):
            for col in range(n):
                x = col * (square_size + distance_between_squares) + x_offset
                y = row * (square_size + distance_between_squares) + y_offset
                # pygame.draw.rect(screen, (0,0,0), (x-1, y-1, square_size+2, square_size+2))
                pygame.draw.rect(self.screen, (0,0,0), (x, y, square_size+1, square_size+1))
                pygame.draw.rect(self.screen, population[i], (x, y, square_size, square_size))
                i = i+1

    def draw_text(self, text, x_position, y_position, color=(255, 255, 255), font_size=30, font='Arial'):
        # Initialize Pygame font
        pygame.font.init()
        # Set the font and size
        font = pygame.font.SysFont(font, font_size)
        # Render the text
        text_surface = font.render(text, True, color)
        # Get the rectangle containing the text surface
        text_rect = text_surface.get_rect()
        # Set the position of the text
        text_rect.topleft = (x_position, y_position)
        # Blit the text onto the screen
        self.screen.blit(text_surface, text_rect)


