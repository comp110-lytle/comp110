---
title: Game Dev Workshop
author:
  - Ben Hites
page: explore
template: overview
---

### Starter Code

```{.python .numberLines startFrom="1"}
    import sys, pygame

    # screen size
    size = width, height = 640, 480

    # constants
    RED = (240, 20, 20)
    LIGHT_BLUE = (51, 153, 255)
    GOLD = (255, 204, 0)
    DARK_PINK = (102, 0, 51)
    PINK = (255, 51, 153)
    # screen and clock objects
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    # ball rectangle object
    ball: pygame.Rect = pygame.Rect(5, height/2, 50, 50)

    # obstacle rectangle objects
    obstacle_top: pygame.Rect = pygame.Rect(0, -25, width, height/2)
    obstacle_bottom: pygame.Rect = pygame.Rect(0, height - 175, width, height/2)
    obstacle_list: list[pygame.Rect] = [obstacle_top, obstacle_bottom]

    # goal rectangle object
    goal: pygame.Rect = pygame.Rect(width-75, height/2, 50, 50)

    def main():
        # starts pygame window and systems
        pygame.init()
        # place mouse in right place and make it invisible
        pygame.mouse.set_pos(15, (height+40)/2)
        pygame.mouse.set_visible(False)
        while 1:
            # Sets frame rate
            time_delta = clock.tick(60)/1000.0

            # fill background with solid color
            screen.fill(LIGHT_BLUE)

            # draw obstacles
            pygame.draw.rect(screen, RED, obstacle_top)
            pygame.draw.rect(screen, RED, obstacle_bottom)

            # draw goal
            pygame.draw.circle(screen, GOLD, (goal.centerx, goal.centery), goal.width / 2)

            # pygame boilerplate for handling keyboard and mouse inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): sys.exit()

            # allow movement if player has reset
            (ball.centerx, ball.centery) = pygame.mouse.get_pos()

            # check collisions with obstacles, reset ball if it touches wall
            for obstacle in obstacle_list:
                if ball.colliderect(obstacle):
                    pygame.mouse.set_pos(15, (height+40)/2)

            # check win condition
            if ball.colliderect(goal):
                print("You Won!")
                sys.exit()

            # draw ball and it's collision rectangle
            pygame.draw.rect(screen, DARK_PINK, ball)
            pygame.draw.circle(screen, PINK, (ball.centerx, ball.centery), ball.width / 2)


            # after all our drawing is done, "flip" the new frame onto the screen
            pygame.display.flip()


    if __name__ == '__main__':
        main()
```
