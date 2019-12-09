from shared import get_wire_paths


CENTRAL_PORT = (5000,5000)
intersections = []

def main():
    wire_paths = get_wire_paths()
    print(manhattan_distance(wire_paths)) #this gives 293

def manhattan_distance(wire_paths):
    rows, cols = (20000,20000)
    circuit_board = [["" for i in range(cols)]for i in range(rows)]

    wire_a_path = wire_paths[0]
    wire_b_path = wire_paths[1]

    circuit_board[CENTRAL_PORT[0]][CENTRAL_PORT[1]] = "ab"

    trace_wire(circuit_board, wire_a_path, "a")
    trace_wire(circuit_board, wire_b_path, "b")
    min_distance = rows
    for intersection in intersections:
        x_distance = abs(CENTRAL_PORT[0] - int(intersection.split('/')[0]))
        y_distance = abs(CENTRAL_PORT[1] - int(intersection.split('/')[1]))
        total_distance = x_distance + y_distance
        min_distance = total_distance if total_distance <= min_distance else min_distance
    return min_distance

def trace_wire(circuit_board, wire_path, marker):
    current_port = [CENTRAL_PORT[0],CENTRAL_PORT[1]]
    for move in wire_path:
        steps = ports_to_move(move)
        if move[0] == "L":
            for i in range(steps):
                x_position = current_port[0] - 1
                y_position = current_port[1]
                if circuit_board[x_position][y_position] != "" and circuit_board[x_position][y_position] != marker:
                    intersections.append(str(x_position) + "/" + str(y_position))
                circuit_board[x_position][y_position] += marker
                current_port[0] = x_position
        if move[0] == "R":
            for i in range(steps):
                x_position = current_port[0] + 1
                y_position = current_port[1]
                if circuit_board[x_position][y_position] != "" and circuit_board[x_position][y_position] != marker:
                    intersections.append(str(x_position) + "/" + str(y_position))
                circuit_board[x_position][y_position] += marker
                current_port[0] = x_position
        if move[0] == "U":
           for i in range(steps):
                x_position = current_port[0]
                y_position = current_port[1] - 1
                if circuit_board[x_position][y_position] != "" and circuit_board[x_position][y_position] != marker:
                    intersections.append(str(x_position) + "/" + str(y_position))
                circuit_board[x_position][y_position] += marker
                current_port[1] = y_position
        if move[0] == "D": 
            for i in range(steps):
                x_position = current_port[0]
                y_position = current_port[1] + 1
                if circuit_board[x_position][y_position] != "" and circuit_board[x_position][y_position] != marker:
                    intersections.append(str(x_position) + "/" + str(y_position))
                circuit_board[x_position][y_position] += marker
                current_port[1] = y_position   
      
        
def ports_to_move(move):
    return int(move[1:].replace(' ,', ''))



    

if __name__ == "__main__":
    main()    