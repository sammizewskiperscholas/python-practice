#Count Positives - Given a list of numbers, create a function to replace last value with number of positive values.
#  Example, count_positives([-1,1,1,1]) changes list #to [-1,1,1,3] and returns it. 
#  (Note that zero is not considered to be a positive number).

def count_positives(num_list):
    count = 0
    new_list = []
    for n in num_list:
        if n > 0:
            count +=1
            new_list.append(n)
        else:
            new_list.append(n)
    new_list[len(num_list)-1] = count
    return new_list

print(count_positives([-1,1,1,1]))
