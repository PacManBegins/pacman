# Main file of our Pac-Man copy
# Pac-Man Begins : A Unyss creation
# PCB Version : alpha 0.0.1
# File version : 1


class PacMan:
    # Here are the main PacMan properties. All are initialized as default
    name = 'Bernard'
    life = 1
    x, y = 0,0
    orientation = 'R'
    godmod = False # Define if PacMan is allowed to fight ghosts

    def __init__ (self,name):
        self.name = name

    def movement(self, dep):
        if(dep=='U'):
            pass
        elif(dep=='D'):
            pass
        elif(dep=='L'):
            pass
        elif(dep=='R'):
            pass
        else:
            print("Error #1 : The 'dep' parameter seems incorrect.")

    # Return all the PacMan Properties as a list
    def data(self):
        liste = [self.name, self.life, self.x, self.y,
        self.orientation, self.godmod]
        return liste


pacman = PacMan('Sheldon')
print(pacman.data())
