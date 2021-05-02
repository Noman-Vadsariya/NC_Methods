class Forward_Backward:
    
    def __init__(self,x_data,y_data,h):
        self.x_data = x_data
        self.y_data = y_data
        self.diff_data = []
        self.h = h
        

    def Forward(self,index):
        a = self.y_data[index+1]-self.y_data[index]
        return (1/self.h) * a
    
    def Backward(self,index):
        a = self.y_data[index-1]-self.y_data[index]
        return (1/-self.h) * a

    def Differentiate(self):

        for i in range(len(self.x_data)):

            if (i+1 < len(self.x_data)):
                self.diff_data.append(self.Forward(i))
            else:
                self.diff_data.append(self.Backward(i))
        
    def get_Diff_data(self):
        return self.diff_data

    def print_table(self):

        print("\nX\t\tF(y)\t\tF'(y)\n")
        for i in range(len(self.x_data)):
            print(f"{round(self.x_data[i],2)}\t\t{round(self.y_data[i],7)}\t\t{round(self.diff_data[i],7)}")


#Validation Required
#Atleast 2 points required

x = [1,1.2,1.4]
y = [1,1.2625,1.6595]

fb = Forward_Backward(x, y, 0.2)
fb.Differentiate()
fb.print_table()