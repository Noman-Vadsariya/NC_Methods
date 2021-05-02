class FivePoint:
    
    def __init__(self,x_data,y_data,h):
        self.x_data = x_data
        self.y_data = y_data
        self.diff_data = []
        self.h = h

    def FivePoint_Midpoint(self,index):
        a = self.y_data[index-2]-8*self.y_data[index-1]+8*self.y_data[index+1]-self.y_data[index+2]
        return (1/(12*self.h)) * a        

    def Forward_FivePoint_Endpoint(self,index):
        a = -25*self.y_data[index]+48*self.y_data[index+1]-36*self.y_data[index+2]+16*self.y_data[index+3]-3*self.y_data[index+4]
        return (1/(12*self.h)) * a
    
    def Backward_FivePoint_Endpoint(self,index):
        a = -25*self.y_data[index]+48*self.y_data[index-1]-36*self.y_data[index-2]+16*self.y_data[index-3]-3*self.y_data[index-4]
        return (1/(12*-self.h)) * a

    def Differentiate(self):

        for i in range(len(self.x_data)):

            if(i-2 >= 0 and i+2 < len(self.x_data)):
                self.diff_data.append(self.FivePoint_Midpoint(i))
            elif (i+4 < len(self.x_data)):
                self.diff_data.append(self.Forward_FivePoint_Endpoint(i))
            else:
                self.diff_data.append(self.Backward_FivePoint_Endpoint(i))
        
    def get_Diff_data(self):
        return self.diff_data

    def print_table(self):

        print("\nX\t\tF(y)\t\tF'(y)\n")
        for i in range(len(self.x_data)):
            print(f"{round(self.x_data[i],2)}\t\t{round(self.y_data[i],7)}\t{round(self.diff_data[i],7)}")


#Validation Required
#Atleast 5 points required

x = [-3,-2.8,-2.6,-2.4,-2.2,-2]
y = [9.367879,8.233241,7.180351,6.209329,5.320305,4.513417]

f = FivePoint(x, y, 0.2)
f.Differentiate()
f.print_table()