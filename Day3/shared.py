def get_wire_paths():
    f = open("data.txt", mode='r')
    if f.mode == "r":
        paths = f.readlines()
        f.close()
        path_a = paths[0].split(',')
        path_b = paths[1].split(',')
        return [path_a, path_b]
    else:
        return None