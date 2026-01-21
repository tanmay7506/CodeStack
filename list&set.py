# aim is to learn and use all operations on set and list 
def list_mutating_operations(items:list, item1, item2):
    # sort the `items` inplace
    items.sort()
    print("sorted:",items)

    # add item1 to the `items` at the end
    items.append(item1)
    print("append:",items)

    # add item2 at index 3
    items.insert(3, item2)
    print("insert:",items)

    # extend `items` with the first three elements in `items`
    items.extend(items[0:3])
    print("extend:", items)

    # pop the fifth element and store it in variable `popped_item`
    popped_item = items.pop(4)
    print("pop:",items)

    # remove first occurance of `item2` from the list
    items.remove(item2)
    print("remove:",items)

    # make the element at index 4 None
    items[4] = None
    print("modify_index:",items)

    # make the even indices None
    items[0::2] = len(items[0::2])*[None]
    print("modify_slice:",items)

    # delete the third last element
    items.pop(-3)
    print("delete_index:",items)

    # delete the even indices
    del items[0::2]
    print("delete_slice:",items)

    return items, popped_item 

def list_non_mutating_operations(items:list, item1, item2):

    # print the sorted version of items
    print("sorted:",sorted(items))

    # print a lsit with item1 appended to the `items` at the end
    print("append:", items + [item1])

    # print a list with item2 added to items at index 3
    print("insert:", items[0:3] + [item2] + items[3:])

    # print a list with the first three elements in `items` added to the end of the `items` again
    print("extend:", items + items[0:3])

    #  print a list with the fifth element from `items` removed
    print("pop:", items[0:4] + items[5:])

    # print a list with first occurance of `item2` removed from `items` 
    items_copy = items.copy()
    items_copy.remove(item2)
    print("remove:",items_copy) # hint: you may want to use index

    # print a list with the fourth element of `items` changed to None
    items_copy1 = items.copy()
    items_copy1[3] = None
    print("modify_index:", items_copy1)

    # print a list with the even indices changed to None
    items_copy2 = items.copy()
    items_copy2[0::2] = len(items_copy2[0::2])*[None]
    print("modify_slice:",items_copy2)

    # print a list with the even indices removed
    items_copy3 = items.copy()
    del items_copy3[0::2] 
    print("delete_slice:",items_copy3)

    return items

def do_set_operation(set1, set2, set3, item1, item2):
    # add item1 to set1
    set1.add(item1)
    print(sorted(set1))
    
    # remove item2 from set1. What if item2 is not in set1?
    set1.remove(item2)
    print(sorted(set1))

    # add elements from set2 to set1
    set1.update(set2)
    print(sorted(set1))

    # remove all elements from set1 that are in set3
    set1.difference_update(set3)
    print(sorted(set1))

    # print the common elements in both set2 and set3 as a sorted list.
    print(sorted(set2.intersection(set3)))

    # print all unique elements present in set1, set2 an set3 as a sorted list
    print(sorted(set1.union(set2 | set3)))

    # print all unique elements that are in set2 but not in set3 as a sorted list
    print(sorted(set2.difference(set3)))

    # print all the non common elements from both set2 and set3
    print(sorted((set2 | set3).difference(set2 & set3)))

    return set1,sorted(set1),sorted(set2),sorted(set3)
