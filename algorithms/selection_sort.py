def selection_sort(array):
    steps = []

    # Look through all elements starting from the non sorted ones
    # csi : Current_Smallest_Index
    for i in range(len(array)):
        csi = i
        for j in range(i, len(array) ):
            # Compare the current smallest element to every next element
            steps.append(("compare", csi, j, array.copy()))
            if array[csi] > array[j]:
                csi = j
        # After finding the smallest element swap it to the lowest non sorted index
        array[i], array[csi] = array[csi], array[i]
        steps.append(("swap", i, csi, array.copy()))
    # When sorting is completed
    steps.append(("done", array))
    return steps
