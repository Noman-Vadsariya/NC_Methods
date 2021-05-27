class Lagrange:

    def __init__(self,x_data,y_data):
        self.x_data = x_data
        self.y_data = y_data

    def interpolate(self,x):
        
        y = 0 #interpolated value

        for i in range(len(self.x_data)):
            prev = 1            
            for j in range(len(self.x_data)):
                if i != j:
                    prev = prev * (x - self.x_data[j])/(self.x_data[i] - self.x_data[j])
            
            y = y + prev * self.y_data[i]
            print(f"Value After 1st Iteration: {round(prev * self.y_data[i],5)}") 

        return y
    

if __name__ == "__main__":

    print("Enter No Interpolating Points: ",end="")
    no_points = int(input())

    x_data = []
    y_data = []
    # x = [0,0.2,0.4,0.6,0.8]
    # y = [1,1.22140,1.49182,1.82212,2.22554]
    
    print("\nEnter Interpolating Points: ")
    for i in range(0,no_points):
        print(f"x{i} : ",end="")
        x = float(input())
        x_data.append(x)
        print(f"y{i} : ",end="")
        y = float(input())
        y_data.append(y)
        print()
    
    print("Enter Value to be Interpolated: ",end="")
    # x=0.65
    x = float(input())
    l = Lagrange(x_data,y_data)
    print(f'\nFinal Interpolated Value : {round(l.interpolate(x),5)}')