import Lab2_Devop as Lab2

def test_find_min_max():
    expected_min = 1
    expected_max = 6
    test_list = [1,6,4,3,5,2]
    min_temp, max_temp = Lab2.find_min_max(test_list)
    assert (min_temp == expected_min)
    assert (max_temp == expected_max)


def test_calc_average_temp():
    expected_result = 3.5
    test_list = [1,2,3,4,5,6]
    result = Lab2.calc_average_temp(test_list)
    assert (result == expected_result)

def test_median_temp():
    expected_result = 3.5
    test_list = [1,2,3,4,5,6]
    result = Lab2.calc_median_temp(test_list)
    assert (result == expected_result)