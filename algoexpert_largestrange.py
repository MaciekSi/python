# solution for Largest Range question from algoexpert.io

def sort(array):
    def booble(array):
        any_switch = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
                any_switch = True
        return any_switch

    while booble(array):
        pass


def largest_range(array):
    sort(array)

    last_value = array[0]
    length_of_seq = 1
    len_of_longest_seq = length_of_seq
    index_of_smallest_in_longest_seq = 0
    biggest_num_in_longest_seq = last_value

    for i in range(1, len(array)):
        # current value is one of number of current sequence
        if (last_value + 1) == array[i] or last_value == array[i]:
            length_of_seq += 1

            # save values of current biggest sequence
            if length_of_seq > len_of_longest_seq:
                len_of_longest_seq = length_of_seq
                biggest_num_in_longest_seq = array[i]
                index_of_smallest_in_longest_seq = i - len_of_longest_seq + 1
        # end of sequence
        else:
            length_of_seq = 1
        last_value = array[i]

    first_num_in_biggest_seq = array[index_of_smallest_in_longest_seq]
    last_num_in_biggest_seq = biggest_num_in_longest_seq
    return [first_num_in_biggest_seq, last_num_in_biggest_seq]


if __name__ == '__main__':
    array = [19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14]
    print(largest_range(array))