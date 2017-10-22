###修改版本1
def DFS(Tuple,Start,Sum,Product):
    ret=0;
    for i in range(Start,len(Tuple)):
        if(i>Start and Tuple[i][1]==Tuple[i-1][1]):
            continue;
        curSum=Sum+Tuple[i][1];
        curProduct=Product*Tuple[i][1];
        if(curSum>curProduct):
            ret=ret+1+DFS(Tuple,i+1,curSum,curProduct);
        elif(Tuple[i][1]==1):
            ret=ret+DFS(Tuple,i+1,curSum,curProduct);
        else:
            break;
    return ret;
 
###修改版本2
def DFS_1(Tuple,root,Sum,Product):
    ret=0;
    firstChild_index=root+1;
    for i in range(firstChild_index,len(Tuple)):
        if(i>firstChild_index and Tuple[i][1]==Tuple[i-1][1]):
            continue;  ###根节点的第二个孩子节点开始，如果它跟它的前一个节点值相同就跳过。避免重复序列的出现
        curSum=Sum+Tuple[i][1];
        curProduct=Product*Tuple[i][1];
        if(curSum>curProduct):
            ret=ret+1+DFS_1(Tuple,i,curSum,curProduct);
        else:
            break;
    return ret;
 
     
def main():
    n=int(raw_input());
    rawList=map(int,raw_input().split());
    if(n<=0 ):
        print 0;
        exit();
    rawTuple=[(ind,num) for ind,num in zip(range(n),rawList)];
    tuple_sorted=sorted(rawTuple,key=lambda x:x[1]);
 
    ###call DFS
    print DFS(tuple_sorted,0,0,1);
 
    ###call DFS_1
    if(tuple_sorted[0][1]!=1):  ###符合要求的序列，第一个数字必须是1.
         print 0;
         exit();
    print DFS_1(tuple_sorted,0,1,1); ###就以第一个1为根节点进行深度优先遍历
 
 
main();