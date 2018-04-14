asdasdas= [32, 12, 20, 16, 3, 1, 2];

# 冒泡排序
# 插入排序

def sort(arr,type=1):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if type==1:
                if(arr[j]<arr[i]):
                    temp=arr[j];
                    arr[j]=arr[i];
                    arr[i]=temp;
            else:
                if (arr[j] > arr[i]):
                    temp = arr[j];
                    arr[j] = arr[i];
                    arr[i] = temp;

    return arr

arr1=[213,13,43,12,23]
def insert (arr):
    for curr in range(1,len(arr)):
        up=curr-1
        if arr[curr]<arr[up]:
            temp=arr[curr]
            arr[curr]=arr[up]
            up=up-1
            while up>=0 and temp<arr[up]:
                arr[up+1]=arr[up]
                up=up-1
            arr[up+1]=temp;
    return arr;
print(insert(arr1))








