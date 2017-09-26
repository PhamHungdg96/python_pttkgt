import DFS

def Kosaraju(mang_vertex,matran):
    cur_time = 0
    not_end=True
    while not_end:
        not_end=False
        for i in range(len(mang_vertex)):
            if mang_vertex[i].start_time == 0:
                not_end = True
                DFS.Dfs(mang_vertex,matran,i,cur_time)
                break
    for i in range(len(mang_vertex)):
        print "dinh %d: %d %d" %(i+1,mang_vertex[i].start_time,mang_vertex[i].end_time)
        



matran = DFS.init('c:\\Users\PHAM_DUNG\\myproject\\algorithm\\input_kosaraju.txt')
mang_vertex = [DFS.Edge() for i in range(matran.height)]
Kosaraju(mang_vertex,matran)