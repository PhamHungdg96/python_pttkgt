def merge(left, right):
    i=0
    j=0
    ds = []
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            ds.append(left[i])
            i=i+1
        else:
            ds.append(right[j])
            j=j+1
    if i==len(left):
        while j<len(right):
            ds.append(right[j])
            j=j+1
    else:
        while i<len(left):
            ds.append(left[i])
            i=i+1
    return ds


def merge_sort(ds):
    n =len(ds)
    if n<=1:
        return ds
    med = (n-1)/2;
    return merge(
        merge_sort(ds[0:med+1]),
        merge_sort(ds[med+1:n])
    )

ds = [0,1,2,3,4,5,3,4,2,2,4,4]
print merge_sort(ds)