# A program that prints and tracks if a salesperson has met
# his sales quota
QUOTA = 70000
sales = float(input('Enter your sales amount: '))
if sales >= QUOTA:
    sales_quota_met = True
else:
    sales_quota_met = False

if sales_quota_met:
    print('You met your sales quota!')
else:
    print('You did not meet the sales quota.')
    

