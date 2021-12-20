#bubble  
def bubble_sort(nums):
    length=len(nums)
    for i in range(length):
        for j in range(length-1-i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums


def select_sort(nums):
    length=len(nums)
    for i in range(length):
        min_idx=i 
        for j in range(i+1,length):
            if nums[j]<nums[min_idx]:
                min_idx=j 
        if i!=min_idx:nums[i],nums[min_idx]=nums[min_idx], nums[i]
    return nums


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



#merge_sort
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


#quick  sort
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


# shell sort

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



#heap_sort

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




nums=[10,3,4,2,1, 9 ,20,1,0,-1]

ret=heap_sort(nums)
print(ret)

