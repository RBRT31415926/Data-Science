import matplotlib.pyplot as plt

def assignment(new_list, new_index, old_list, old_index):
    new_list[new_index] = old_list[old_index]


def mergeSort(input_list):
    if (
        len(input_list) > 1
    ):
        # Teile die Liste mittig in zwei neue Listen
        mid = len(input_list) // 2
        left = input_list[:mid]
        right = input_list[mid:]
        # Rekursiver Aufruf mit den Teillisten
        mergeSort(left)
        mergeSort(right)

        left_iter = 0
        right_iter= 0
        combined_iter = 0
        
        # Iteriere über beide Teillisten
        while left_iter < len(left) and right_iter< len(right):
            # Falls das derzeitige Element in left kleiner ist, füge es zuerst 
            # in die neue Liste
            if left[left_iter] <= right[right_iter]:
                assignment(input_list, combined_iter, left, left_iter)
                left_iter += 1
            # Sonst füge das Element aus der rechten Liste hinzu
            else:
                assignment(input_list, combined_iter, right, right_iter)
                right_iter+= 1
            combined_iter += 1

        # Falls alle Elemente einer Teilliste einsortiert sind, füge alle restlichen
        # Elemente der anderen Liste danach hinzu.
        while left_iter < len(left):
            input_list[combined_iter] = left[left_iter]
            left_iter += 1
            combined_iter += 1

        while right_iter< len(right):
            input_list[combined_iter] = right[right_iter]
            right_iter+= 1
            combined_iter += 1


test_input = [54, 26, 93, 17, 77, 31, 44, 55, 20]

list_indices = range(len(test_input))

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, sharey = True, figsize=(14, 7))

ax1 = plt.subplot(1, 2, 1)
plt.ylabel("Wert", fontsize=20) 
plt.xlabel("Position in Liste", fontsize=20)
plt.scatter(list_indices, test_input, label="Listeneintrag")
plt.title("Liste vor Mergesort",fontsize=20)
plt.legend(loc="upper right", frameon=True, fontsize=15)

mergeSort(test_input)

ax2 = plt.subplot(1, 2, 2)
plt.xlabel("Position in Liste", fontsize=20)
plt.scatter(list_indices, test_input, label="Listeneintrag")
plt.title("Liste nach Mergesort", fontsize=20)
plt.legend(loc="upper left", frameon=True, fontsize=15);
