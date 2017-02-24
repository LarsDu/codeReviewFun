'''
This code demonstrates object oriented encapsulation with a "Vehicle" class

This was a 2 hour Insight project

Original version acquire from: http://codereview.stackexchange.com/questions/155913/create-two-vehicles-move-them-on-a-grid-based-on-user-input

Revised by Larry Du

'''

class MapGrid():
    
    def __init__(self,width,height):
        """MapGrid class encapsulates the map our vehicle is moving around on

        :param width: width of the map (integer)
        :param height: height of the map (integer)
        :returns: 
        :rtype: None
        """
        self.width = int(width)
        self.height = int(height)

class Vehicle():

    #Class attributes 
    directions = ['N','E','S','W']
    num_directions = len(directions)
    movement = {'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W':(-1,0)}
    

    
    def __init__(self, x, y, face,mapgrid):
        """Create a Vehicle object

        :param x: x position (integer)
        :param y: y position (integer)
        :param face: The direction the vehicle is facing. Can be 'N','E','S', or 'W'
        :param mapgrid: A MapGrid object to define the space in which our vehicle is moving 
        :returns: 
        :rtype: None

        """
        
        self.x = int(x)
        self.y = int(y)
        self.face = face
        self.mapgrid = mapgrid

    def run_commands(self,command_list):
        command_dict = {'L': self.turn_left, 'R': self.turn_right, 'M': self.move}
        for command in command_list:
            command_dict[command]()
    
    def turn_left(self):
        self.face = Vehicle.directions[(Vehicle.directions.index(self.face)-1)%
                                                           Vehicle.num_directions]

    def turn_right(self):
        self.face = Vehicle.directions[(Vehicle.directions.index(self.face)+1)%
                                                            Vehicle.num_directions]
    def move(self):
        new_x = self.x + Vehicle.movement[self.face][0]
        new_y = self.y + Vehicle.movement[self.face][1]
        #first_vehicle_x and first_vehicle_y are used globally and break encapsulation
        if new_x in xrange(self.mapgrid.width+1):
            self.x = new_x
        if new_y in xrange(self.mapgrid.height+1):
            self.y = new_y

    

#Functions for user input:            
def check_grid_size_input():
    while True:
        dim_list = raw_input("Enter map grid size (ie: 10 10): ").strip().split()
        width,height = dim_list[0],dim_list[1]
        if len(dim_list)>2:
            print ("Invalid number of inputs, try again")
        else:
            break
    return (int(width),int(height))
            
def check_inital_pos_input():
    while True:
        pos = raw_input("Enter inital x,y, and face (ie:5 5 N): ").strip().split()
        x,y,face = pos[0],pos[1],pos[2]
        if len(pos) > 3:
            print ("Invalid number of inputs, try again.")
        else:
            break
    return (int(x),int(y),str(face))
    
def check_commands_input():
    while True:
        try:
            mov = raw_input("Enter commands as string (ie: LRMLML): ")
            break
        except:
            print ("Invalid input")
    return mov    
            
         
           
def vehicle_from_input():
    """Creates vehicle from set of command line inputs
    :returns: a Vehicle object containing a MapGrid
    :rtype: Vehicle 
    """

    width,height = check_grid_size_input()
    init_x,init_y,init_face = check_inital_pos_input()
    moves = check_commands_input()

    ret_vehicle = Vehicle(init_x,init_y,init_face,MapGrid(width,height))
    return (ret_vehicle,moves)
    
   


def main():

    vehicle_one,v1_moves = vehicle_from_input()
    vehicle_two,v2_moves = vehicle_from_input()
    
    vehicle_one.run_commands(v1_moves)
    vehicle_two.run_commands(v2_moves)
    
    print vehicle_one.x, vehicle_one.y, vehicle_one.face
    print vehicle_two.x, vehicle_two.y, vehicle_two.face


if __name__ == "__main__":
    main()
