def addandsubtract():
    numbers=[]
    for i in range(3):
        a= int(input())
        numbers.append(a)
        i+=1
    def add1(numbers):
        add1.sum1 = numbers[0]+numbers[1]
        return add1.sum1
    def subtract1(sum1):
        subtract1.var = add1.sum1 - numbers[2]
        print(subtract1.var)
        return subtract1.var       
    add1(numbers)
    subtract1(add1.sum1) 

addandsubtract()