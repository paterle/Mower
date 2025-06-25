class Robot:
    ORIENTATIONS = ['N', 'E', 'S', 'W']
    def __init__(self, x, y, orientation, instructions):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.instructions= instructions

    def spin_left(self):
        idx = Robot.ORIENTATIONS.index(self.orientation)
        self.orientation = Robot.ORIENTATIONS[(idx - 1) % 4]

    def spin_right(self):
        idx = Robot.ORIENTATIONS.index(self.orientation)
        self.orientation = Robot.ORIENTATIONS[(idx + 1) % 4]

    def move(self, x_max, y_max):
         # Check area boundaries before moving
        if ((self.x == x_max and self.orientation == 'E') or
            (self.x == 0 and self.orientation == 'W') or
            (self.y == y_max and self.orientation == 'N') or
            (self.y == 0 and self.orientation == 'S')):
            pass  
        elif self.orientation == 'N':
            self.y += 1
        elif self.orientation == 'S':
            self.y -= 1
        elif self.orientation == 'E':
            self.x += 1
        elif self.orientation == 'W':
            self.x -= 1
    def process_instructions(self, x_max, y_max):
        for instruction in self.instructions:
            if instruction == 'M':
                self.move(x_max, y_max)
            elif instruction == 'L':
                self.spin_left()
            elif instruction == 'R':
                self.spin_right()
            else:
                raise ValueError(f"Invalid instruction: '{instruction}'. Only allowed L, R, M.")
        return self.x, self.y, self.orientation