import time
def sum_of_number(n):
    sum =0
    start_time = time.time()
    for i in range(1,n):
        sum +=i
    end_time = time.time()
    return sum,end_time-start_time

n=50000000
print("Time to sum 1 to ",n," and required time to calculate is :", sum_of_number(n))
