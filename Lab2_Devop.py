print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
        print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    split_input = input().split(",")
    float_list = [float(x) for x in split_input]
    return float_list      

def calc_average_temp(m):
    
    avg = sum(m) / len(m)
    print("Average temperature: ", avg)
    return avg


def find_min_max(x):
    min_temp = min(x)
    max_temp = max(x)
    min_max = [min_temp, max_temp]
    print("Minimum temperature: ", min_temp)
    print("Maximum temperature: ", max_temp)
    return min_max

def sort_temperature(p):
    sort_temperature = sorted(p)
    print("Sorted temperatures: ", sort_temperature)    
    return sort_temperature

def calc_median_temp(v):
    n = len(v)
    sorted_temps = v
    if n%2 == 0:
        median_temp = (sorted_temps[n//2 - 1] + sorted_temps[n//2]) / 2
    else:
        median_temp = sorted_temps[n//2]

    print("Median temperature: ", median_temp)
    return median_temp

