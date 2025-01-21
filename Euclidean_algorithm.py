class EuclideanAlgorithm:
    
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
    euclidean= EuclideanAlgorithm
    number1 = 15
    number2 = 30
    gcd = euclidean.get_euclidean_gcd(number1, number2)
    print("The GCD between 15 and 30 is",gcd)
    number1 = 120
    number2 = 68
    gcd = euclidean.get_euclidean_gcd(number1, number2)
    print("The GCD between 120 and 68 is",gcd)
if __name__ == "__main__":
     
    main()