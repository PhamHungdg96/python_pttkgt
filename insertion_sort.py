def insertion_sort(ds):
    for i in range(len(ds)):
        cur_value = ds[i];
        j = i-1;
        while j>=0 and ds[j]>cur_value:
             ds[j+1]=ds[j]
             j=j-1
        ds[j+1]=cur_value

ds = [9,4,8,1,5,7,3,6,2]

insertion_sort(ds)

print ds
