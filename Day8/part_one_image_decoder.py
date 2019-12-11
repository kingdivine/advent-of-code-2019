LAYER_WIDTH = 25
LAYER_HEIGHT = 6

def main():
    layers = read_image_data()
    layer_with_most_zeroes = layer_with_least_ocurrences_of_digit(layers, '0')
    print(number_multiple(layer_with_most_zeroes,'1', '2')) #this gives 2356

def read_image_data():
    data = None
    with open('data.txt', mode='r') as f:
        data = f.read()
    
    layer_size = LAYER_WIDTH * LAYER_HEIGHT
    layers = [data[i:i+layer_size ] for i in range(0, len(data), layer_size)]
    return layers

def layer_with_least_ocurrences_of_digit(layers, digit):
    min_count = LAYER_WIDTH * LAYER_HEIGHT
    layer_with_min_count = None
    for layer in layers:
        if layer.count(digit) <= min_count:
            min_count = layer.count(digit)
            layer_with_min_count = layer        
    return layer_with_min_count

def number_multiple(layer, first_digit, second_digit):
    return layer.count(first_digit) * layer.count(second_digit)

if __name__ == "__main__":
    main()