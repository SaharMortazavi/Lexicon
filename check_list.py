def CheckList(nums):
    for i in nums:
        if nums[0]==1 and nums[1]==1 and nums[2]==2 and nums[3]==3 and nums[4]==1:
            return True
        else:
            return False
print(CheckList(nums=[1,1,2,3,1]))

    