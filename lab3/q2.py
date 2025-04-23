class pair_finder:
    def my_pairs(self,my_arr,target):
        my_ans=[]
        for i in range(len(my_arr)-1):
            for j in range(i+1,len(my_arr)):
                my_sum=my_arr[i]+my_arr[j]
                if(my_sum==target):
                    my_ans.append(my_arr[i])
                    my_ans.append(my_arr[j])
                    break
        return my_ans
arr=[1,2,3,41,1,5]
curr=pair_finder()
target=46
my_ans=curr.my_pairs(arr,target)
print(my_ans)
