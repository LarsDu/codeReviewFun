'''
General comments:
This code needs substantial refactoring. 
Use of global variables breaks encapsulation
Classes definitions should not be inlined in the code


'''

directions = ['N','E','S','W'] 

movement = {'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W':(-1,0)}
commands = {'L': 'turn_left', 'R': 'turn_right', 'M': 'move'}

## LDu: Uppercase variable names should be used on constant values
# Using map 
GRID_MAX_X, GRID_MAX_Y = map(int, raw_input().split())

first_vehicle_x = None
first_vehicle_y = None

## LDu: This class should be in it's own file and should not follow the variable
## declarations above

class Vehicle():
    def __init__(self, x, y, face):
        self.x = x
        self.y = y
        #You may want to use self._dir here as dir is a python reserved keyword
        self.dir = face

    def turn_left(self):
        self.dir = directions[(directions.index(self.dir)-1)%len(directions)]

    def turn_right(self):
        self.dir = directions[(directions.index(self.dir)+1)%len(directions)]

    def move(self):
        new_x = self.x + movement[self.dir][0]
        new_y = self.y + movement[self.dir][1]
        #first_vehicle_x and first_vehicle_y are used globally and break encapsulation
        if new_x != first_vehicle_x or new_y != first_vehicle_y:
            #GRID_MAX_X and GRID_MAX_Y also break encapsulation
            if new_x in xrange(GRID_MAX_X+1):
                self.x = new_x
            if new_y in xrange(GRID_MAX_Y+1):
                self.y = new_y


#These commands should be in a separate main() function

#These two raw_input() should be grouped with the earlier raw_input call for clarity
#Might want to insert a case for user inputs split by commas as well as spaces
vehicle_one_pos = raw_input().split()
#There needs to be a command line prompt asking for input (and specifying type of input)
#This input also ought to be type checked or type cast here.
vehicle_one_commands = raw_input()


vehicle_one = Vehicle(int(vehicle_one_pos[0]), int(vehicle_one_pos[1]), vehicle_one_pos[2])
for command in vehicle_one_commands:
    #Needs more comments
    eval("vehicle_one.{0}()".format(commands[command]))

first_vehicle_x = vehicle_one.x
first_vehicle_y = vehicle_one.y


vehicle_two_pos = raw_input().split()
vehicle_two_commands = raw_input()

vehicle_two = Vehicle(int(vehicle_two_pos[0]), int(vehicle_two_pos[1]), vehicle_two_pos[2])
for command in vehicle_two_commands:
    eval("vehicle_two.{0}()".format(commands[command]))

print vehicle_one.x, vehicle_one.y, vehicle_one.dir
print vehicle_two.x, vehicle_two.y, vehicle_two.dir
