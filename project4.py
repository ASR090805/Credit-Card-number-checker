def multiply_by_two(num):
    for i in range(len(num)):
        num[i]*=2
        if num[i]>9:
            num[i]=doubled_val(num[i])
    return num

def doubled_val(val):
    return val-9

def result(total_sum):
    if total_sum%10==0: print('it is a valid Credit Card number')
    else: print('''it is 'not' a valid Credit Card number''')

def valid_num(credit_card):
    num=[int(d) for d in credit_card if d.isdigit()]
    num.reverse()
    odd_index=[]
    even_index=[]
    for i in range(len(num)):
        if i%2==0: even_index.append(num[i])
        else: odd_index.append(num[i])
    odd_index=multiply_by_two(odd_index)
    odd_index_sum=sum(odd_index)
    even_index_sum=sum(even_index)
    result(odd_index_sum+even_index_sum)

credit_card=input('enter your Credit Card number:')
valid_num(credit_card)