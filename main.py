from robot import Robot
from pathlib import Path
#Function for processing programme input
def process_input(name_file):
    input_path = Path('input.txt')
    if not input_path.exists():
        raise FileNotFoundError("El archivo input.txt no existe en el directorio actual.")
    elif input_path.stat().st_size == 0:
        raise ValueError("El archivo input.txt está vacío.")
    else:
        with open(name_file, 'r') as f:
            lines = [line.strip() for line in f]
            print("INPUT:")
            for line in lines:
                print(line)
        # First line. Coordinates of the area
        x_max_floor = int(lines[0][0])
        y_max_floor = int(lines[0][1])

        # Lines for robots (position and moves)
        robots = []
        if ((len(lines)-1)%2!=0):
            print(f"Error: No hay 2 lineas por robot")
            exit(1)
        for i in range(1, len(lines), 2):
            pos_line = lines[i]
            inst_line = lines[i + 1]
            x= int(pos_line[0])
            y= int(pos_line[1])
            orientation= pos_line[3]
            instructions= list(inst_line)
            robot=Robot(x,y,orientation,instructions)

            robots.append(robot)

        return x_max_floor,y_max_floor, robots


def main():
    
    try:
        x_max_floor, y_max_floor, robots = process_input('input.txt')
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        exit(1)
    
    #Process robot's instructions
    with open('output.txt', 'w') as f:
        print("\nOUTPUT:")
        for robot in robots:
            try:
                x_final,y_final,orientation_final= robot.process_instructions(x_max_floor,y_max_floor)
                f.write(f"{x_final}{y_final} {orientation_final}\n")
                print(f"{x_final}{y_final} {orientation_final}")
            except ValueError as e:
                print(f"Error en instrucciones del robot: {e}")
                exit(1)

if __name__ == "__main__":
    main()