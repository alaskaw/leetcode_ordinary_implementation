#1.bubble  
def bubble_sort(nums):
    length=len(nums)
    for i in range(length):
        for j in range(length-1-i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums


#2.select sort
def select_sort(nums):
    length=len(nums)
    for i in range(length):
        min_idx=i 
        for j in range(i+1,length):
            if nums[j]<nums[min_idx]:
                min_idx=j 
        if i!=min_idx:nums[i],nums[min_idx]=nums[min_idx], nums[i]
    return nums


#insert sort
def insert_sort(nums):
    length=len(nums)
    for i in range(1,length):
        pointer=i-1
        cur=nums[i] 
        while pointer>=0 and nums[pointer]>cur:
            nums[pointer+1]=nums[pointer]
            pointer-=1
        nums[pointer+1]=cur
    return nums



#4.merge_sort
def merge(nums1,nums2):
    res=[]
    while nums1 and nums2:
        if nums1[0]<nums2[0]:
            res.append(nums1.pop(0))
        else:
            res.append(nums2.pop(0)) 
    if nums1:res+=nums1
    else:res+=nums2
    return res

def merge_sort(nums):
    length=len(nums)
    if length<=1:return nums
    return merge(merge_sort(nums[0:length//2]),merge_sort(nums[length//2:]))


#5. quick sort
import random
def select_idx(nums,left,right):
    pivot=random.randint(left,right)
    nums[right],nums[pivot]=nums[pivot],nums[right]
    i=left-1
    for j in range(left,right):
        if nums[j]<nums[right]:
            i+=1
            nums[i],nums[j]=nums[j],nums[i]
    i+=1
    nums[i ], nums[right ]=nums[right],nums[i]
    return i

def quick_sort(nums,left,right):
    if left>=right:return 
    pivot=select_idx(nums,left ,right )
    quick_sort(nums,left,pivot-1)
    quick_sort(nums,pivot+1,right)
    return nums

def sortarray(nums):
    length= len(nums)
    nums=quick_sort(nums,0,length-1)
    return nums


#6. shell sort

def shell_sort(nums):
    length=len(nums)
    gap=length//2
    while gap>0:
        for i in range(gap,length):
            j=i
            cur=nums[j]
            while j-gap>=0 and nums[j-gap]>cur:
                nums[j]=nums[j-gap]
                j-=gap
            nums[j]=cur
        gap//=2
    return nums



#7. heap sort

def heapify(nums,length,i):
    largest=i
    left=largest*2+1
    right=largest*2+2
    largest=left if left<length and nums[largest]<nums[left] else largest
    largest=right if right<length and nums[largest]<nums[right] else largest
    if largest!=i : 
        nums[i],nums[largest]=nums[largest],nums[i]
        heapify(nums,length,largest)

def heap_sort(nums):
    length=len(nums)
    for i in range(length-1,-1,-1):
        heapify(nums,length,i)
    for i in range(length-1,0,-1):
        nums[0],nums[i]=nums[i],nums[0]
        heapify(nums,i,0)
    return nums



#8. 桶排序
 def bucket_sort(nums):
    min_val,max_val,length=min(nums),max(nums),len(nums)
    bucket=[0 for _ in range(min_val,max_val+1)]
    for i in range(length):
        bucket[nums[i]-min_val]+=1
    length=len(bucket)
    res=[]
    for i in range(length):
        if bucket[i]!=0:
            res+=[min_val+i]*bucket[i]
    return res









nums=[10,3,4,2,1, 9 ,20,1,0,-1]

ret=heap_sort(nums)
print(ret)

