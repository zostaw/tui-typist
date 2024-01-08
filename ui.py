#!/usr/bin/env python
# from pyray import *
# init_window(800, 450, "Hello")
# while not window_should_close():
#     begin_drawing()
#     clear_background(WHITE)
#     draw_text("Hello world", 190, 200, 20, VIOLET)
#     end_drawing()
# close_window()

# import raylib as rl
import math
from pyray import *


def point_in_circle_sector(center, radius, angle_start, angle_end, point):
    # Calculate the relative position of the point to the center
    dx = point[0] - center[0]
    dy = point[1] - center[1]
    angle = math.atan2(dy, dx) * (180 / math.pi)

    # Normalize the angle to 0-360 degrees range
    if angle < 0:
        angle += 360

    distance_squared = dx**2 + dy**2
    within_radius = distance_squared <= radius**2

    if angle_end < angle_start:
        return within_radius and (angle >= angle_start or angle <= angle_end)
    else:
        return within_radius and (angle >= angle_start and angle <= angle_end)


def main():
    # Initialize the screen width and height
    screen_width = 800
    screen_height = 450
    init_window(screen_width, screen_height, "UI with Circular Buttons")

    # Button dimensions and positions
    center = Vector2(screen_width // 2, screen_height // 2)
    radius = 100

    # Set the FPS
    set_target_fps(60)

    sectors = {
        'down': (45, 135),
        'left': (135, 225),
        'up': (225, 315),
        'right': (315, 45)  # Note that we go past 360 degrees to cover the rest of the circle.
    }

    # Define colors for each sector
    colors = {
        'up': RED,
        'right': GREEN,
        'down': BLUE,
        'left': YELLOW,
    }

    # Game loop
    while not window_should_close():
        mouse_point = Vector2(get_mouse_x(), get_mouse_y())

        if is_mouse_button_pressed(MOUSE_LEFT_BUTTON):
            for name, (angle_start, angle_end) in sectors.items():
                if point_in_circle_sector((center.x, center.y), radius, angle_start, angle_end, (mouse_point.x, mouse_point.y)):
                    print(f"{name} button pressed")

        # Start drawing
        begin_drawing()
        clear_background(BLACK)

        # Draw circular buttons (sectors)
        for name, (angle_start, angle_end) in sectors.items():
            angle_length = angle_end - angle_start
            #draw_circle_sector_lines(center, radius, angle_start, angle_length, 10, colors[name])
            draw_circle_sector(center, radius, angle_start, angle_length, 536, colors[name])

        # Finish drawing
        end_drawing()

    # De-Initialization
    close_window()


if __name__ == "__main__":
    main()
