# PERMUTATIONS IN STRINGS CONCEPT 

def permute(nums,index):
    #BASE CASE
    if index==len(nums):
        print("".join(nums))
        return
    #TRY EVERY CHARACTER
    for i in range(index,len(nums)):
        #SWAP CASE
        nums[index],nums[i]=nums[i],nums[index]
        #RECURSIVE CASE
        permute(nums,index+1)
        #BACKTRACKING CASE
        nums[index],nums[i]=nums[i],nums[index]
s="ABC"
permute(list(s),0)