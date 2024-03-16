''' Job Scheduling '''
# todo - integrate the concept of DEADLINE in this Program
def schedule(total_time , jobs , profits):
    # sort the profits
    #profits = sorted(profits)
    profits.sort(reverse = True)
    print(profits)
    my_profit = 0
    for i in range(total_time):
        my_profit += profits[i]
        
    print('Total Jobs Done = ' , total_time)
    print('Total Profit earned = ',my_profit)
         
        



n = int(input('Total Time : '))
m = int(input('Total Number of Jobs :'))
profits = []
for index , i in enumerate(range(m)):
    p = int(input(f'Enter profit related with job {index} :'))
    profits.append(p)

schedule(n,m,profits)
    
