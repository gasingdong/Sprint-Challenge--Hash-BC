#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    for i in range(0, length):
        weight = weights[i]
        complement = hash_table_retrieve(ht, limit - weight)
        if complement is not None:
            first = complement
            second = i
            return (first, second) if first >= second else (second, first)
        hash_table_insert(ht, weight, i)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
