#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_list = []
    for ind in range(0, list_length):
        try:
            div = my_list_1[ind] / my_list_2[ind]
        except TypeError:
            print('wrong type')
            div = 0
        except ZeroDivisionError:
            print('division by 0')
            div = 0
        except IndexError:
            print('out of range')
            div = 0
        finally:
            div_list.append(div)
    return div_list
