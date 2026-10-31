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
current_action = None
highlight_i = None
highlight_j = None

# reset these 5 variables when calling this function (when choosing a new algorithm and at initialization)
def start_sorting(name):
    global selected_algorithm, array_duplicate, steps, finished, current_step, current_action, highlight_i, highlight_j
    
    selected_algorithm = name
    array_duplicate = array_original.copy()
    steps = algorithms[name](array_duplicate)
    current_action = None
    highlight_i = None
    highlight_j = None
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

# speed control variables
clock = pygame.time.Clock()
step_delay = 200
last_step_time = 0

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

    # speed control for the algorithm visualization
    clock.tick(60) # 60 fps
    current_time = pygame.time.get_ticks()

    # event handling, when the user clicks something
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # if enough time has passed since the last step, then start updating the variables for the current step
    if current_time - last_step_time >= step_delay and not finished:
        last_step_time = current_time

        if current_step < len(steps):
            current_action = steps[current_step][0]

            # for "done", dont fetch i and j
            if current_action != "done":
                highlight_i = steps[current_step][1]
                highlight_j = steps[current_step][2]

            array_duplicate = steps[current_step][-1].copy()

            # go to the next step
            current_step += 1

        else:
            finished = True

    # TO-DO: if the step requires it, then show i and j in a different color / highlight them in some way
    # TO-DO: user can select which algorithm to visualize from a list of available algorithms (keys of the algorithms dictionary)
    pygame.display.update()

pygame.quit()