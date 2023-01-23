# class with multiple attributes python
class polygon:

    def __init__(self, layer, datatype, xy_num, xy ):
        self.xy=xy
        self.layer = layer
        self.datatype = datatype
        self.xy_num = xy_num

    def printPolygon(self):
        print("boundary", file=f)
        print("layer", self.layer, file=f)
        print ("datatype", self.datatype, file=f)
        print("xy", self.xy_num, end="", file=f)
        #print(self.xy)

        for i in range (0,self.xy_num,2):
            print(self.xy[i], self.xy[i+1], end=" ", file=f)
    
        print("", file=f)
        print("endel", file=f)
    pass


polygon_num=0
polygons=[]
header=[]
footer=[]


with open(r"C:\Users\radhi\OneDrive\Desktop\Milestone_Input\Milestone_Input\Milestone 1\Format_Source.txt") as file:
    hflag=0
    
    for x in file.readlines():
        parts = x.strip().split()
        


        if (len(parts) == 0):
            continue

        if (parts[0] == "boundary"):
            polygon_num = polygon_num + 1
            xy=[]
            hflag=1
        elif (parts[0] == "layer"):
            layer = int(parts[1])
        
        elif (parts[0] == "datatype"):
            datatype = int(parts[1])

        elif (parts[0] == "xy"):
            xy_num = int(parts[1])
            
            for i in range (xy_num):
                j=2
                xy.append(parts[j])
                xy.append(parts[j+1])
                j=j+2

        elif (parts[0] == "endel"):
            p=polygon(layer, datatype, xy_num, xy)
            polygons.append(p)
            #p.printPolygon()

        if (hflag==0):
            header.append(x)
            #continue
        if (parts[0] == "endstr" or parts[0] == "endlib"):
            footer.append(x)

#print(footer)

with open(r"milestone1_output.txt", "w") as f:
    for i in header:
        f.write(i)
    for i in range(2):
        polygons[i].printPolygon()
    for i in footer:
        f.write(i)


    



    

