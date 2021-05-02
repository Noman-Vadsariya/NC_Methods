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

        return y
    


x = [0,0.2,0.4,0.6,0.8]
y = [1,1.22140,1.49182,1.82212,2.22554]

l = Lagrange(x,y)
print(f'Interpolated Value : {round(l.interpolate(0.65),5)}')
