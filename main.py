def twoSum(nums, target):
  Answer = []
  flag=0
  for i in range(len(nums)):
    for j in range(len(nums)):
      if(i!=j):
        if(nums[i] + nums[j] == target):
          Answer.append(i)
          Answer.append(j)
          flag=1
          break;
    if(flag==1):
      break;
  return Answer
