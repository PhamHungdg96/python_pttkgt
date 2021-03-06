class Vertex:
    def __init__(self,start_time=0,end_time=0,status=0,index=0,group=0):
        self.start_time=start_time
        self.end_time=end_time
        self.status=status
        self.index=index
        self.group=group
    def reset(self):
        self.start_time=self.end_time=self.status=self.group=0

class MaTranKe:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.Arr=[[0]*width]*height

def init(file_name):
    f=open(file_name)
    line=f.readline().split(" ")
    numbers=map(lambda x:int(x),line)
    if len(numbers)==1:
        arr = MaTranKe(numbers[0],numbers[0])
        for i in range(arr.height):
            line=f.readline().split(" ")
            numbers=map(lambda x:int(x),line)
            arr.Arr[i]=numbers
        f.close()
        return arr
    else:
        f.close()
        MaTranKe(0,0)
def run(mang_vertex,matran,index,cur_time):
    mang_vertex[index].start_time=cur_time
    cur_time+=1
    mang_vertex[index].status=1
    for i in range(len(mang_vertex)):
        if mang_vertex[i].status==0 and matran.Arr[index][i]>0:
            cur_time=run(mang_vertex,matran,i,cur_time)
            cur_time+=1
    mang_vertex[index].status=1
    mang_vertex[index].end_time=cur_time
    return cur_time

def reverse_matrix(matran):
    for i in range(matran.height):
        for j in range(i+1,matran.width):
            temp = matran.Arr[i][j]
            matran.Arr[i][j]=matran.Arr[j][i]
            matran.Arr[j][i]=temp

def prog():
    arr = init('C:\\Users\\phamh\\Documents\\GitHub\\algorithm_pttkgt\\input.txt')
    mang_vertex = [Vertex() for i in range(arr.height)]
    run(mang_vertex,arr,0,0)
    for i in range(len(mang_vertex)):
        print "dinh %d: %d %d" % (i+1,mang_vertex[i].start_time,mang_vertex[i].end_time)

#prog()