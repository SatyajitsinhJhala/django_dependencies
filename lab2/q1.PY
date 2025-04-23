import statistics
my_list=[]

num=int(input("Enter number of elements:"))
for i in range(num):
    curr_element=int(input("Enter elements: "))
    my_list.append(curr_element)
cur_sum=sum(my_list)
my_variance=statistics.variance(my_list)
my_mean=statistics.mean(my_list)
my_standard_deviation=statistics.stdev(my_list)
print("var: "+str(my_variance)+" my_mean "+str(my_mean)+" my_standard_dev "+str(my_standard_deviation))

