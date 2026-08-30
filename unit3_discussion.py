"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

This program demonstrates how Python lists behave when elements
are inserted, removed, and searched.

Topics demonstrated:
- List insertion
- List deletion
- Linear search
- Index validation
- Exception handling
- Edge-case handling
- Real-world list usage
- Basic Big-O performance analysis
"""


def insert_at(lst, index, value):
    """
    Insert a value into the list at the specified index.

    Parameters:
        lst (list): The list being modified.
        index (int): The position where the value should be inserted.
        value: The value to insert.

    Returns:
        None
    """

    # Python's insert() places the new value at the specified index.
    # Existing elements at that position and later are shifted one
    # position to the right.
    #
    # Inserting near the beginning can require many elements to be
    # shifted, making the operation O(n) in the worst case.
    # Inserting at the end does not require existing elements to
    # shift, so it is approximately O(1).
    lst.insert(index, value)


def delete_at(lst, index):
    """
    Remove and return the value at the specified index.

    Parameters:
        lst (list): The list being modified.
        index (int): The position of the value to remove.

    Returns:
        The removed value.

    Raises:
        IndexError: If the specified index does not exist.
    """

    # Validate the index before deleting. This is important because
    # attempting to remove a nonexistent position should produce a
    # clear error rather than silently returning None.
    #
    # None could be a legitimate value stored in a list, so using
    # None to indicate an error would create ambiguity.
    #
    # Negative indexes are valid in Python. For example, -1 refers
    # to the last element in the list.
    if not (-len(lst) <= index < len(lst)):
        raise IndexError(
            f"Index {index} is invalid for a list of length {len(lst)}."
        )

    # Removing an element causes elements after it to shift one
    # position to the left. Therefore, deletion from the beginning
    # or middle can require shifting multiple elements and is O(n).
    #
    # Removing the final element does not require shifting other
    # elements and is approximately O(1).
    return lst.pop(index)


def search_value(lst, value):
    """
    Search for a value within the list.

    Parameters:
        lst (list): The list to search.
        value: The value being searched for.

    Returns:
        The index of the value if found, otherwise -1.
    """

    # This is a linear search because the list is examined
    # sequentially from the first element toward the last.
    #
    # Best case: the value is found at the first position, O(1).
    # Worst case: every element must be examined, O(n).
    for index in range(len(lst)):
        if lst[index] == value:
            return index

    # Returning -1 indicates that the value was not found.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # INSERTION TESTS
    # ===============================

    print("\n=== INSERTION TESTS ===")

    # Create a list containing several values.
    numbers = [10, 20, 30, 40, 50]

    print("Original list:", numbers)

    # Insert at the beginning.
    # Existing elements must shift one position to the right.
    insert_at(numbers, 0, 5)
    print("After inserting 5 at the beginning:", numbers)

    # Insert in the middle.
    # Elements from the insertion point onward shift to the right.
    insert_at(numbers, 3, 25)
    print("After inserting 25 in the middle:", numbers)

    # Insert at the end.
    # No existing elements need to be shifted.
    insert_at(numbers, len(numbers), 60)
    print("After inserting 60 at the end:", numbers)

    # ===============================
    # DELETION TESTS
    # ===============================

    print("\n=== DELETION TESTS ===")

    # Delete from the beginning.
    # Removing the first element causes the remaining elements
    # to shift one position to the left.
    removed = delete_at(numbers, 0)
    print("Removed from beginning:", removed)
    print("Updated list:", numbers)

    # Delete from the middle.
    # Elements after the deleted value shift left to fill the gap.
    middle_index = len(numbers) // 2
    removed = delete_at(numbers, middle_index)
    print("Removed from middle:", removed)
    print("Updated list:", numbers)

    # Delete from the end.
    # No other elements need to shift when the final element
    # is removed.
    removed = delete_at(numbers, len(numbers) - 1)
    print("Removed from end:", removed)
    print("Updated list:", numbers)

    # ===============================
    # SEARCH TESTS
    # ===============================

    print("\n=== SEARCH TESTS ===")

    # Search for a value that exists in the list.
    # The function returns the position where the value is found.
    search_result = search_value(numbers, 25)

    if search_result != -1:
        print("Value 25 was found at index:", search_result)
    else:
        print("Value 25 was not found.")

    # Search for a value that does not exist.
    # The function scans the list sequentially and returns -1.
    search_result = search_value(numbers, 100)

    if search_result != -1:
        print("Value 100 was found at index:", search_result)
    else:
        print("Value 100 was not found. Search returned -1.")

    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASES ===")

    # Edge Case 1:
    # Attempt to delete an invalid index.
    #
    # delete_at() raises an IndexError instead of returning None.
    # The try/except block allows the program to handle the error
    # without terminating.
    try:
        delete_at(numbers, 100)
    except IndexError as error:
        print("Invalid deletion handled:", error)

    # Edge Case 2:
    # Search for a value that is not contained in the list.
    # The complete list is searched before returning -1.
    missing_value = search_value(numbers, 999)

    if missing_value == -1:
        print("Search edge case: value 999 was not found.")

    # Edge Case 3:
    # Insert into an empty list.
    # Python allows insertion at index 0 into an empty list.
    empty_list = []
    insert_at(empty_list, 0, 100)
    print("Insert into empty list:", empty_list)

    # Edge Case 4:
    # Attempt to delete from an empty list.
    # An IndexError is raised and handled with try/except.
    empty_list = []

    try:
        delete_at(empty_list, 0)
    except IndexError as error:
        print("Delete from empty list handled:", error)

    # ===============================
    # REAL-WORLD SCENARIO
    # ===============================

    print("\n=== REAL-WORLD SCENARIO ===")

    # Scenario:
    # A small store keeps a list of customer orders in the order
    # that they were received.
    orders = ["Order #101", "Order #102", "Order #103"]

    print("Original orders:", orders)

    # A new priority order needs to be added to the beginning.
    # This demonstrates insertion at the beginning of a real-world list.
    insert_at(orders, 0, "Priority Order #100")
    print("After adding priority order:", orders)

    # A cancelled order is removed from the middle of the list.
    cancelled_order = delete_at(orders, 2)
    print("Cancelled order removed:", cancelled_order)
    print("Updated orders:", orders)

    # Search for a specific order to determine its current position.
    order_index = search_value(orders, "Order #103")

    if order_index != -1:
        print("Order #103 is currently at index:", order_index)
    else:
        print("Order #103 was not found.")

    # This scenario demonstrates why list operations matter in
    # real-world applications. Adding or removing items near the
    # beginning of a list may require many elements to shift.
    # Searching may also require checking many elements sequentially.
    # For very large datasets, data structures designed for specific
    # operations may provide better performance.


if __name__ == "__main__":
    main()