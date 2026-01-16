while True :
    task = int(input("Enter task number (1-7): "))
    if task == 1:
        #Task 1
        x = int(input("Input first int: "))
        y = int(input("Input second int: "))
        z = str(input("Input function: "))

        bol = True 

        while (bol):
            if (z == "+") :
                print(x + y)
        
            elif (z == "-") :
                print(x - y) 

            elif (z == "*") :
                print(x * y)

            elif (z == "/" and y != 0) :
                print(x / y)  
        
            else:
                print("Error")
            
            bol = False

    elif task == 2:
        #Task 2

        while True:
            x = int(input("Input first int: "))
            y = int(input("Input second int: "))
            z = str(input("Input function: "))

            if (z == "+") :
                print(x + y)
        
            elif (z == "-") :
                print(x - y) 

            elif (z == "*") :
                print(x * y)

            elif (z == "/" and y != 0) :
                print(x / y)  
        
            else:   
                print("Error")
        
    elif task == 3:
        #Task 3
        for i in range(1,21):
            print(i)
            
    elif task == 4:
        #Task 4
        l = []
        for i in range(10):
            a = int(input("Input int`s: "))
            l.append(a)
        
        for j in l:
            print(j ** 2)
        
    elif task == 5:
        #Task 5
        bread = ["white", "brown"]
        meat = ["chicken", "beef"]
        vegetables = ["cucumber", "tomato", "onion"]
        sauces = ["mayo", "ketchup" , "mustard"]

        for b in bread:
            for m in meat:
                for v in vegetables:
                    for s in sauces:
                        print(b ,"bread" , m , v , s)
                    
    elif task == 6:
        #Task 6
        sum_of_e = 0
        sum_of_o = 0

        for i in range(1,101):
            if i % 2 == 0:
                sum_of_e += i
            else:
                sum_of_o += i
            
        print("Sum of even numbers:",sum_of_e)
        print("Sum of odd numbers:",sum_of_o)

    elif task == 7:
        #Task 7
        n = int(input("Input int: "))
        factorial = 1

        for i in range(1, n + 1):
            factorial *= i

        print("Factorial of", n, "is", factorial)
        
    else:
        print("Invalid task number. Please enter a number between 1 and 7.")
