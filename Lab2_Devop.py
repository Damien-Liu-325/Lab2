print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    input()
    split_input = input().split(",")
    float_list = [float(x) for x in split_input]
    return float_list    

def calc_average_temp():
    avg = sum(get_user_input()) / len(get_user_input())

def find_min_max():
    min_temp = min(get_user_input())
    max_temp = max(get_user_input())
    min_max = [min_temp, max_temp]
    return min_max
def sort_temperature():
    print("sort_temperature")

def calc_median_temp():
    print("calc_median_temp")
