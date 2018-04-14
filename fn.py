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

print(sort(asdasdas,4))
