# Main file of our Pac-Man copy
# Pac-Man Begins : A Unyss creation
# PCB Version : alpha 0.0.1
# File version : 2

# Pygame is the main graphic library we use
import pygame

import settings

# Define if Pac-Man or ghosts can go in a direction
def allowedToMov(x,y ,direction):
    return True


class PacMan:
    # Here are the main PacMan properties. All are initialized as default
    name = 'Bernard'
    life = 1
    x, y = 0,0
    orientation, wantedOrientation, isMoving = 'R', 'R', False
    godmod = False # Define if PacMan is allowed to fight ghosts

    def __init__ (self,name):
        self.name = name

    # Handle the user volunteer of changing Pac-Man Orientation
    def changeOrientation(self, changeMov):
        if(changeMov!='U' and changeMov!='D' and changeMov!='L'
          and changeMov!='R'):
            print("Error #1 : the 'changeMov' parameter seems incorrect.")

        else:
            wantedOrientation = changeMov
            # If Pac-Man can mov now in the wanted orientation, we change is
            # orientation and allow him to move on. If he can't, we record
            # the 'wanted Direction' in case if he stop is course, he will
            # rotate in this orientation.
            if(allowedToMov(self.x, self.y, self.wantedOrientation)):
                orientation = wantedOrientation
                isMoving = True

    # Handle the movement of Pac-Man.
    def movement(self):
        if(orientation=='U'):
            pass
        elif(orientation=='D'):
            pass
        elif(orientation=='L'):
            pass
        elif(orientation=='R'):
            pass

        if(not(isMoving)):
            orientation = wantedOrientation


    # Return all the PacMan Properties as a list
    def data(self):
        liste = [self.name, self.life, self.x, self.y,
        self.orientation, self.wantedOrientation, self.isMoving,
        self.godmod]
        return liste


pacman = PacMan('Sheldon')
print(pacman.data())

windows = pygame.display.set_mode((settings.width, settings.height))
