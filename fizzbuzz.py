def generate(upto):
    for num in range(1,upto+1):
        return(fizzbuzz(num))
       
       
       
       
       
       
def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return(num)

generate(20)

        




