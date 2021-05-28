from lib.processor import Processor

p = Processor()
p.setVariable("x")

class Lagrange:

    def __init__(self,x_data,y_data):
        self.x_data = x_data
        self.y_data = y_data

    def interpolate(self,x):
        
        y = 0 #interpolated value
        p.clearResults()

        for i in range(len(self.x_data)):
            prev = 1            
            for j in range(len(self.x_data)):
                if i != j:
                    prev = prev * (x - self.x_data[j])/(self.x_data[i] - self.x_data[j])
            
            y = y + prev * self.y_data[i]
            p.addResult({
                "iterative interpolated value": (prev * self.y_data[i]),
            })

        p.printResults(("iterative interpolated value", ))

        p.clearResults()

        p.addResult({
            "final interpolated value": y
        })

        p.printResults(("final interpolated value", ))

        return y
    
