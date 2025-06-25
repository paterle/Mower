import pytest
from robot import Robot 

def test_spin_left():
    robot = Robot(0, 0, 'N', [])
    robot.spin_left()
    assert robot.orientation == 'W'
    robot.spin_left()
    assert robot.orientation == 'S'

def test_spin_right():
    robot = Robot(0, 0, 'N', [])
    robot.spin_right()
    assert robot.orientation == 'E'
    robot.spin_right()
    assert robot.orientation == 'S'

def test_move_north():
    robot = Robot(1, 2, 'N', [])
    robot.move(5, 5)
    assert (robot.x, robot.y) == (1, 3)

def test_move_east():
    robot = Robot(1, 2, 'E', [])
    robot.move(5, 5)
    assert (robot.x, robot.y) == (2, 2)

def test_move_south():
    robot = Robot(1, 2, 'S', [])
    robot.move(5, 5)
    assert (robot.x, robot.y) == (1, 1)

def test_move_west():
    robot = Robot(1, 2, 'W', [])
    robot.move(5, 5)
    assert (robot.x, robot.y) == (0, 2)

def test_out_of_bounds():
    robot = Robot(0, 0, 'S', [])
    robot.move(5, 5)
    assert (robot.x, robot.y) == (0, 0)
    robot = Robot(0, 0, 'W', [])
    robot.move(5, 5)
    assert (robot.x, robot.y) == (0, 0)

def test_process_instructions():
    robot = Robot(1, 2, 'N', list("LMLMLMLMM"))
    x, y, orientation = robot.process_instructions(5, 5)
    assert (x, y, orientation) == (1, 3, 'N')

    robot = Robot(3, 3, 'E', list("MMRMMRMRRM"))
    x, y, orientation = robot.process_instructions(5, 5)
    assert (x, y, orientation) == (5, 1, 'E')

    robot = Robot(2, 3, 'S', list("MMRMMRXRRM")) 
    with pytest.raises(ValueError) as excinfo:
        robot.process_instructions(5, 5)
    assert "Invalid instruction" in str(excinfo.value)
