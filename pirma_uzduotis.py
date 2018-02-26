"""
This is program created by Domantas Alenskas
for Python course 2018
"""

import sys


def handle_params():
    """
    Handles params given when launching the program.
    There are default params as well.
    """
    context = {'action_b': '2 begins ANA',
               'action_c': '13 float ASC',
               'action_d': '[14, 21]',
               'action_e': '\t'}

    size = len(sys.argv)
    if size > 1:
        context['action_b'] = sys.argv[1]
    if size > 2:
        context['action_c'] = sys.argv[4]
    if size > 3:
        context['action_d'] = sys.argv[3]
    if size > 4:
        context['action_e'] = sys.argv[4]
    # ignore others

    return context


def make_uppercase(data):
    """
    Converts all lowercase symbols from data to uppercase
    """
    temp_data = []
    for line in data:
        temp_data.append(line.upper())
    return temp_data


def action_b(context, data):
    """
    Filters data by given context.
    This function returns filtered data,
    records which does not meet the requirements
    are thrown out.
    """
    context = context.split()
    column = int(context[0]) - 1
    condition = context[1]
    string_to_find = context[2]

    result = [] # this is our result, currently its empty list
    for line in data:
        if condition == 'begins':
            if line[column].startswith(string_to_find):
                result.append(line)
    return result


def action_c(context, data):
    """
    Sorts data by given context.
    Returns data sorted by given
    column and order.
    """
    context = context.split()
    column = int(context[0]) - 1
    order = context[2]
    temp_list = []
    if order == "ASC":
        reverse = False
    else:
        reverse = True
    for line in sorted(data, key=lambda line: line[column], reverse=reverse):
        temp_list.append(line)
    return temp_list


def action_d(context, data):
    """
    Returns data with 2 columns swapped.
    Column places taken from context.
    """
    context = context.split(',')
    first_column = int(context[0].replace('[', '')) - 1
    second_column = int(context[1].replace(']', '')) - 1
    temp_list = []

    for line in data:
        temp = line[first_column]
        line[first_column] = line[second_column]
        line[second_column] = temp
        temp_list.append(line)
    return temp_list


def write_to_file(data, file_name, delimiter):
    """
    Used to write data to file while
    separating records by given delimiter.
    """
    file = open(file_name, "w")
    for line_of_data in data:
        temp = ""
        for element in line_of_data:
            temp = temp + element + delimiter  # j stand for one
        temp = temp + '\n'
        file.write(temp)
    file.close()


def read_from_file(file_name):
    """
    Used to read data from file
    """
    file = open(file_name, 'r')
    list_to_return = []

    for line in file:
        line = line.rstrip()
        list_to_return.append(line.split(','))
    return list_to_return


def main():
    """
    Main function where everything is handled
    """
    context = handle_params()

    data = read_from_file('input01.csv')

    headers = data[0]
    del data[0]  # lets save and remove headers so it would be easier to sort
    headers = make_uppercase(headers)

    data = action_b(context['action_b'], data)
    data = action_c(context['action_c'], data)
    data.insert(0, headers)  # lets add headers back because all sorting is over
    data = action_d(context['action_d'], data)
    write_to_file(data, 'o​utput01_​DomantasAlenskas.txt', context['action_e'])


main()
