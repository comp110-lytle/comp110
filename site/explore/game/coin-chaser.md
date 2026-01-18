---
title: Coin Chaser pygame demo
author:
  - Ben Hites
page: explore
template: overview
---

## Here is a quick tutorial for TA’s to run, so that you grasp the basic concepts of the pygame library.

## Lets start by installing the pygame library, in your vscode terminal : 'python -m pip install pygame'

### Here is what a boilerplate pygame environment looks like:
```{.python .numberLines startFrom="1"}
# Import and initialize the pygame library
import pygame
 
pygame.init()
 
# Set up the drawing window
screen = pygame.display.set_mode([800, 500])
                               
# pygame clock object controls tick rate
clock = pygame.time.Clock()
# Run until the user asks to quit
running = True
 
while running:
    clock.tick(60)
 
    # Fill background
    screen.fill((120, 200, 255))
 
    # Checks every frame for any user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    pygame.display.flip()
 
# Done! Time to quit.
pygame.quit()
```
 






### Lets try creating a pygame rect object and draw it on screen:
```{.python .numberLines startFrom="1"}
# Run until the user asks to quit
clock = pygame.time.Clock()
running = True
 
# (x, y, width, height)
rect: pygame.Rect = pygame.Rect(20, 20, 50, 50)
 

# Fill background
screen.fill((120, 200, 255))

# Draw rect (window, color(rgb), rect object)
pygame.draw.rect(screen, (150, 10, 245), rect)
```
## Now there should be a rectangle on the screen in the upper left corner. This is the bread and butter for creating and displaying objects, most students will be using rectangles or circles to display on screen.  

### Next, let's get our mouse position and lock the rectangle to move with it.
```{.python .numberLines startFrom="1"}
while running:
    clock.tick(60)
    # get_pos() gets the x,y position of the mouse and that is then offset by 25
    rect.x = pygame.mouse.get_pos()[0] - 25
    rect.y = pygame.mouse.get_pos()[1] - 25
```

This is all we need! Since every frame we are drawing the rectangle using its location, changing its location we can easily move the object dynamically based on user input. At this point, your rectangle should appear locked onto the cursor. Students should approach moving objects during the game in this way.

### Now let’s add a coin and test pygames collisions
```{.python .numberLines startFrom="1"}
coin = pygame.Rect(200, 300, 25, 25)

(pygame has a lot of attributes for rect objects like centerx (location of middle of rect on x-axis))
 pygame.draw.rect(screen, (150, 10, 245), rect)
 # draw circle (window, color(rgb), position (x,y), radius)
 pygame.draw.circle(screen, (235, 162, 52), (coin.centerx, coin.centery), 15)
```

On screen should be a golden circle (coin), even though we created a rectangle object to represent the position. This rectangle can be viewed as a “hit box” or a rectangle around our coin that can be used to more easily calculate collisions using pygame.

### Pygame Collisions
```{.python .numberLines startFrom="1"}
pygame.draw.circle(screen, (235, 162, 52), (coin.centerx, coin.centery), 15)
hit = coin.colliderect(rect)
        if(hit):
            // destroy coin and increment score
```
Pygame’s colliderect is a method of a rect, takes another rect, and returns a bool as to whether they overlap. This bool can be used to execute collision behavior which I have left out.

## Extra:
If you are feeling adventurous try adding a list of coins, and use for loops to draw, check collisions, and remove coins when the player hits them!

Check out the pygame documentation for the rect object, it will be super helpful for students and for you
