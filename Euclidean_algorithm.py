class EuclideanAlgorithm():
    
    def get_euclidean_gcd(x,y):
    
        # If x is 0 then the gcd between x and y is y
        if x == 0:
            return y
        # If y is 0 then the gcd between x and y is x
        if y== 0:
            return x
        
        # Use the while loop to keep on getting the remainder of division between x and y until x becomes 0. Division between x and y as follows:
        ##  while x is not 0, get remainder of dividing y over x, replace x by this remainder and y by x.
        while x > 0:
            temp = y%x
            y = x
            x = temp
            
        return y
def main():
    try:
        euclidean= EuclideanAlgorithm
        # take the numbers as input
        number1 = input("Please Type your first number: ")
        # convert to integer
        integer1=int(number1)
        
        # make sure inputs are valid (positive), keep taking input until its valid
        while integer1<0:
            number1=input("The number should be positive, please re-enter it: ")
            integer1=int(number1)
        number2 = input("Please Type your second number: ")
        integer2=int(number2)
        while integer2<0:
            number2=input("The number should be positive, please re-enter it: ")
            integer2=int(number1)
        
        
        
        gcd = euclidean.get_euclidean_gcd(integer1, integer2)
        print("The GCD between both numbers is",gcd)
    except ValueError:
        print("The number(s) you entered are invalid")

if __name__ == "__main__":
     
    main()