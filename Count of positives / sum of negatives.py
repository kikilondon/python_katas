def count_positives_sum_negatives(arr):
#check len arr if empty return an empty array 

    if len(arr) == 0:
        return []
#set two variables for sums
    pos_numbers = 0
    neg_numbers = 0
#iterate through arr
    for n in arr:
        if n > 0:#filter positive numbers
            pos_numbers += 1#add pos numbers
        elif n < 0:
            neg_numbers += n 

    return [pos_numbers, neg_numbers]#return the two sums