def bubble_sort(array):
    steps = []
    n = len(array)

    # Iterate through all array elements
    for i in range(n):
        # Skip last i elements since they are already sorted
        for j in range(0, n-i-1):
            # compare elements that are next to each other
            # if left is greater than right, swap them, otherwise, continue
            steps.append(("compare", j, j+1, array.copy()))
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                steps.append(("swap", j, j+1, array.copy()))
            else:
                steps.append(("no_swap", j, j+1, array.copy()))
    # When sorting has been completed
    steps.append(("done", array.copy()))
    return steps