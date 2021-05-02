class ThreePoint:
    
    def __init__(self,x_data,y_data,h):
        self.x_data = x_data
        self.y_data = y_data
        self.diff_data = []
        self.h = h

    def ThreePoint_Midpoint(self,index):
        a = self.y_data[index+1]-self.y_data[index-1]
        return (1/(2*self.h)) * a        

    def Forward_ThreePoint_Endpoint(self,index):
        a = -3*self.y_data[index]+4*self.y_data[index+1]-self.y_data[index+2]
        return (1/(2*self.h)) * a
    
    def Backward_ThreePoint_Endpoint(self,index):
        a = -3*self.y_data[index]+4*self.y_data[index-1]-self.y_data[index-2]
        return (1/(2*-self.h)) * a

    def Differentiate(self):

        for i in range(len(self.x_data)):

            if(i-1 >= 0 and i+1 < len(self.x_data)):
                self.diff_data.append(self.ThreePoint_Midpoint(i))
            elif (i+2 < len(self.x_data)):
                self.diff_data.append(self.Forward_ThreePoint_Endpoint(i))
            else:
                self.diff_data.append(self.Backward_ThreePoint_Endpoint(i))
        
    def get_Diff_data(self):
        return self.diff_data

    def print_table(self):

        print("\nX\t\tF(y)\t\tF'(y)\n")
        for i in range(len(self.x_data)):
            print(f"{round(self.x_data[i],2)}\t\t{round(self.y_data[i],7)}\t{round(self.diff_data[i],7)}")


#Validation Required
#Atleast 3 points required

x = [2,2.1,2.2,2.3]
y = [3.6887983,3.6905701,3.6688192,3.6245909]

t = ThreePoint(x, y, 0.1)
t.Differentiate()
t.print_table()