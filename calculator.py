import pygame
import sys

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = (475, 575)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (100, 150, 250)
FONT = pygame.font.Font(None, 50)
SMALL_FONT = pygame.font.Font(None, 40)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Calculator")

buttons = [
    ('1', 50, 150, 80, 80), ('2', 150, 150, 80, 80), ('3', 250, 150, 80, 80), ('/', 350, 150, 80, 80),
    ('4', 50, 250, 80, 80), ('5', 150, 250, 80, 80), ('6', 250, 250, 80, 80), ('*', 350, 250, 80, 80),
    ('7', 50, 350, 80, 80), ('8', 150, 350, 80, 80), ('9', 250, 350, 80, 80), ('-', 350, 350, 80, 80),
    ('C', 50, 450, 80, 80), ('0', 150, 450, 80, 80), ('=', 250, 450, 80, 80), ('+', 350, 450, 80, 80)
]

# Variables for calculation
current_input = ''
result = ''

# Draw button
def draw_button(label, x, y, w, h):
    pygame.draw.rect(screen, GRAY, (x, y, w, h))
    text = FONT.render(label, True, BLACK)
    text_rect = text.get_rect(center=(x + w / 2, y + h / 2))
    screen.blit(text, text_rect)

# Function to evaluate the input expression
def evaluate_expression(expression):
    try:
        return str(eval(expression))
    except Exception:
        return "Error"

running = True
while running:
    screen.fill(WHITE)

    # Draw display area
    pygame.draw.rect(screen, BLUE, (50, 50, 380, 80), border_radius=10)
    display_text = FONT.render(current_input or result or "0", True, WHITE)
    display_rect = display_text.get_rect(right=375, centery=90)
    screen.blit(display_text, display_rect)

    # Draw buttons
    for button in buttons:
        draw_button(*button)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
            mouse_x, mouse_y = event.pos
            
            # Check if any button is clicked
            clicked_button = None
            for label, x, y, w, h in buttons:
                if x <= mouse_x <= x + w and y <= mouse_y <= y + h:
                    clicked_button = label
                    break
            
            # Handle the clicked button
            if clicked_button:
                if clicked_button == 'C':
                    current_input = ''
                    result = ''
                elif clicked_button == '=':
                    result = evaluate_expression(current_input)
                    current_input = ''
                else:
                    current_input += clicked_button

    pygame.display.flip()

pygame.quit()
sys.exit()