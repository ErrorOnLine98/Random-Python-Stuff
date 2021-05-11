# function build Max Heap where value  
# of each child is always smaller  
# than value of their parent  
def build_max_heap(arr, num):
    for i in range(num):

        # if child is bigger than parent  
        if arr[i] > arr[int((i - 1) / 2)]:
            j = i

            # swap child and parent until  
            # parent is smaller  
            while arr[j] > arr[int((j - 1) / 2)]:
                (arr[j],
                 arr[int((j - 1) / 2)]) = (arr[int((j - 1) / 2)],
                                           arr[j])
                j = int((j - 1) / 2)


arr = [73, 6, 24, 101, 27, 15, 8, 99, 72, 25, 18, 84]
n = len(arr)
print("Given array: ")
for k in range(n):
    print(arr[k], end=" ")
print()
build_max_heap(arr, n)
print("Max Heap: ")
for l in range(n):
    print(arr[l], end=" ")
