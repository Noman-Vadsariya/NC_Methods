from lib.processor import Processor

p = Processor()

class Backward_Difference:
    
    def __init__(self,x_data,y_data):

        self.x_data = x_data
        self.y_data = y_data
    
    #returns factorial of any number
    def factorial(self,n):
        if n == 1:
            return 1

        return n*self.factorial(n-1)
    
    def get_S(self,S,n):
        t = S
        
        for i in range(1, n):
            t = t * (S + i)

        return t

    def Construct_Backward_Difference_Table(self):

        for i in range(1, len(self.x_data)):
            for j in range(len(self.x_data)-1,i-1,-1):
                self.y_data[j][i] = self.y_data[j][i - 1] - self.y_data[j - 1][i - 1]

    # Displaying the forward difference table
    def print_table(self):
        
        for i in range(len(self.x_data)):
            print(self.x_data[i], end = "\t")

            for j in range(0,i+1):
                print(round(self.y_data[i][j],7), end = "\t")
            
            print("")
    
    def interpolate(self,x):

        sum = self.y_data[len(self.x_data)-1][0]  #since forward difference that's why yn

        S = (x - self.x_data[len(self.x_data)-1]) / (self.x_data[1] - self.x_data[0])

        p.clearResults()
        p.addResult({
            "iterative interpolated value": sum
        })

        for i in range(1,len(self.x_data)):
            sum = sum + (self.get_S(S, i) * self.y_data[len(self.x_data)-1][i]) / self.factorial(i)
            p.addResult({
                "iterative interpolated value": sum
            })

        p.printResults(("iterative interpolated value", ))

        p.clearResults()
        p.addResult({
            "final interpolated value": sum
        })

        p.printResults(("final interpolated value",))

        return sum

if __name__ == "__main__":

    print("Enter No Interpolating Points: ",end="")
    no_points = int(input())

    x_data = []
    y_data = [[0 for i in range(no_points)] for i in range(no_points)]
    j=0
    print("\nEnter Interpolating Points: ")
    for i in range(0,no_points):
        print(f"x{i} : ",end="")
        x = float(input())
        x_data.append(x)
        print(f"y{i} : ",end="")
        y = float(input())
        y_data[i][j] = y
        print()

    print("Enter Value to be Interpolated: ",end="")
    # x=0.05
    x = float(input())

    bd = Backward_Difference(x_data, y_data)
    bd.Construct_Backward_Difference_Table()
    print("\n-----------Backward Difference Table-------------\n")
    bd.print_table()
    print()
    print(f'Final Interpolated Value: {round(bd.interpolate(x),5)}')

# n = 5
# x = [ 1891, 1901, 1911,  1921, 1931 ]            
# y = [[0 for i in range(n)]
#         for j in range(n)]

# y[0][0] = 46
# y[1][0] = 66
# y[2][0] = 81
# y[3][0] = 93
# y[4][0] = 101

# fd = Backward_Difference(x, y)
# fd.Construct_Backward_Difference_Table()
# fd.print_table()
# print()
# print(f'Interpolated Value: {round(fd.interpolate(1925),5)}')
