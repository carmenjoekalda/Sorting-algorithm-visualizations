import pygame
from algorithms.bubble_sort import bubble_sort
from algorithms.selection_sort import selection_sort

# variables
run = True
finished = False

array_original = [17, 4, 23, 9, 1, 26, 13, 20, 6, 28, 11, 3, 19, 25, 8, 15, 2, 22, 10, 27, 5, 16, 24, 12, 7, 21, 14, 18]
array_duplicate = array_original.copy()

algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort
}
selected_algorithm = "Bubble Sort"

steps = []
current_step = 0

# reset these 5 variables when calling this function (when choosing a new algorithm and at initialization)
def start_sorting(name):
    global selected_algorithm, array_duplicate, steps, finished, current_step
    
    selected_algorithm = name
    array_duplicate = array_original.copy()
    steps = algorithms[name](array_duplicate)
    array_duplicate = array_original.copy()
    finished = False
    current_step = 0

start_sorting(selected_algorithm)

# pygame window
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sorting Algorithm Visualizer")

title_font = pygame.font.SysFont("Arial", 32)

bar_spacing = 5
bar_width = 21

# main loop
while run:
    # display black screen and draw the elements on it
    # display the title (name of the selected algorithm)
    title = title_font.render(f"Algorithm: {selected_algorithm}", True, white)
    title_div = title.get_rect(center=(SCREEN_WIDTH // 2, 30))
    
    SCREEN.fill(black)
    SCREEN.blit(title, title_div)

    # display the array as bars on the screen
    for i in range(len(array_duplicate)):
        # calculate the height and position coordinates
        bar_height = array_duplicate[i] * 15
        bar_x = 30 + i * (bar_width + bar_spacing)
        bar_y = SCREEN_HEIGHT - bar_height - 50

        # draw the bar on the screen
        pygame.draw.rect(
            SCREEN,
            white,
            (bar_x, bar_y, bar_width, bar_height)
        )

    # event handling, when the user clicks something
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # TO-DO: initialize a clock to control the speed of the visualization
    # TO-DO: wait for a short time before each step of the algorithm
    # TO-DO: call next step of the algorithm and update the displayed array accordingly
    # TO-DO: if the step requires it, then show i and j in a different color / highlight them in some way
    # TO-DO: user can select which algorithm to visualize from a list of available algorithms (keys of the algorithms dictionary)
    pygame.display.update()

pygame.quit()