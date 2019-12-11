LAYER_WIDTH = 25
LAYER_HEIGHT = 6

def main():
    layers = read_image_data()
    layer_with_most_zeroes = layer_with_least_ocurrences_of_digit(layers, '0')
    print(number_multiple(layer_with_most_zeroes,'1', '2')) #this gives 2356
    
    layers_as_arr = []
    for layer in layers:
       layers_as_arr.append([layer[i:i+LAYER_WIDTH] for i in range(0, len(layer),LAYER_WIDTH )])

    final_image = construct_final_image(layers_as_arr)
    pretty_print(final_image) #this gives PZEKB

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

def construct_final_image(layers):
        final_image = [['' for x in range (LAYER_WIDTH)] for x in range(LAYER_HEIGHT)]
        for i in range(LAYER_HEIGHT):
            for n in range(LAYER_WIDTH):
                final_image[i][n] = get_pixel(layers,i,n)
        return final_image

def get_pixel(layers, i, n):
    for layer in layers:
        if layer[i][n] == '0':
            return '0'
        elif layer[i][n] == '1':
            return '1'
    return ''
    
def pretty_print(arr):
    for row in range(LAYER_HEIGHT):
        this_row = []
        for col in range(LAYER_WIDTH):
            if arr[row][col] == '1':
                this_row.append('1')
            else:
                this_row.append(' ')
        print(''.join(this_row))        

if __name__ == "__main__":
    main()