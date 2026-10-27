import pygame
from algorithms.bubble_sort import bubble_sort
from algorithms.selection_sort import selection_sort

# variables
run = True
finished = False

array_original = [5, 3, 8, 6, 2, 7, 4, 1]
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
    finished = False
    current_step = 0

start_sorting(selected_algorithm)

# pygame window
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# main loop
while run:
    # event handling, when the user clicks something
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # TO-DO: initialize a clock to control the speed of the visualization
    # TO-DO: display the current algorithm name on the screen
    # TO-DO: show duplicated array as bars on the screen
    # TO-DO: wait for a short time before each step of the algorithm
    # TO-DO: call next step of the algorithm and update the displayed array accordingly
    # TO-DO: if the step requires it, then show i and j in a different color / highlight them in some way
    # TO-DO: user can select which algorithm to visualize from a list of available algorithms (keys of the algorithms dictionary)
    pygame.display.update()

pygame.quit()