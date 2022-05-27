# Taking input 

n = int(input("Enter number of elements : "))

    # Read input
res = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]
    # Mean
m = len(res)
  
get_sum = sum(res)
mean = get_sum / m
  
print("Mean / Average is: " + str(mean))

    # Median
n = len(res)
res.sort()
  
if n % 2 == 0:
    median1 = res[n//2]
    median2 = res[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = res[n//2]
    print("Median is: " + str(median))

#Mode
    n = len(res)
    
    data = Counter(res)
    get_mode = dict(data)
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
    
    if len(mode) == n:
        get_mode = "No mode found"
    else:
        get_mode = "Mode is / are: " + ', '.join(map(str, mode))
        
    print(get_mode)