from lib.processor import Processor

p = Processor()

class Forward_Difference:
    
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
            t = t * (S - i)

        return t

    def Construct_Forward_Difference_Table(self):
        for i in range(1, len(self.x_data)):
            for j in range(len(self.x_data) - i):
                self.y_data[j][i] = self.y_data[j + 1][i - 1] - self.y_data[j][i - 1]

    # Displaying the forward difference table
    def print_table(self):
        
        for i in range(len(self.x_data)):
            print(self.x_data[i], end = "\t")

            for j in range(len(self.x_data) - i):
                print('{:<10}'.format(round(self.y_data[i][j],7)), end = "\t")
            
            print("")
    
    def interpolate(self,x):

        sum = self.y_data[0][0]  #since forward difference that's why y0

        S = (x - self.x_data[0]) / (self.x_data[1] - self.x_data[0])

        p.clearResults()
        p.addResult({
            "iterative interpolated value": sum
        })

        for i in range(1,len(self.x_data)):
            sum = sum + (self.get_S(S, i) * self.y_data[0][i]) / self.factorial(i)
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

# n = 5
# x = [0,0.2,0.4,0.6,0.8]
# y = [[0 for i in range(n)]
#         for j in range(n)]

# y[0][0] = 1
# y[1][0] = 1.22140
# y[2][0] = 1.49182
# y[3][0] = 1.82212
# y[4][0] = 2.22554

# fd = Forward_Difference(x, y)
# fd.Construct_Forward_Difference_Table()
# fd.print_table()
# print()
# print(f'Interpolated Value: {round(fd.interpolate(0.05),5)}')
