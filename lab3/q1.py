class subgen:
    def my_subset(self,arr):
        my_ans=[[]]
        for i in arr:
            my_ans+=[s+[i] for s in my_ans]
        return my_ans
arr=[1,2,3,4]
my_s=subgen()
my_ans=my_s.my_subset(arr)
print(my_ans)