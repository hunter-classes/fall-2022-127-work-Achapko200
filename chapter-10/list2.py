def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return avg

print("The average is", cal_average([18,25,3,41,5]))




def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((4,9,16)))
