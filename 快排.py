

def quickSortCell(list,low,high):
    pivot = list[low]
    while low < high:
        while low < high and list[high]>= pivot:
            high -= 1
        list[low] = list[high]
        while low < high and list[low]<= pivot:
            low += 1
        list[high] = list[low]
    list[low] = pivot
    return low
def quickSort(list, low, high):
    if len(ll)<=1:
        return ll
    if low<high:
        mid = quickSortCell(list,low,high)
        quickSort(list,low,mid-1)
        quickSort(list,mid+1,high)
    return list
if __name__ == '__main__':
    ll = [3,5,1,2,4]
    print(quickSort(ll,0,len(ll)-1))