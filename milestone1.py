# class with multiple attributes python
class polygon:

    def __init__(self, layer, datatype, xy_num,x,y):
        self.layer = layer
        self.datatype = datatype
        self.xy_num = xy_num
        self.xy=self.vertex(x,y)

    class vertex:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    def printPolygon(self):
        print("boundary", file=f)
        #f.write("layer %s", self.layer)
        print("layer {}".format(self.layer), file=f)
        #f.write()
        #f.write("datatype", self.datatype)
        print("datatype {}".format(self.datatype), file=f)
        print("xy", file=f, end=" ")
        #f.write("xy", self.xy_num, end="")
        #print(self.xy)

        num=int(self.xy_num)

        for i in range (0, num):
            #f.write(self.xy.x[i], end=" ")
            print("{}".format(self.xy.x[i]), file=f, end=" ")
            #f.write(self.xy.y[i], end=" ")
            print("{}".format(self.xy.y[i]), file=f, end=" ")

        #print("{}".format(self.xy.x[i]), file=f)
        #f.write("", file=f)
        print("endel", file=f)
    pass


polygon_num=0
polygons=[]
header=[]
footer=[]

with open(r"C:\Users\radhi\OneDrive\Desktop\Milestone_Input\Milestone_Input\Milestone 1\Format_Source.txt") as file:
    hflag=0
    lines=file.readlines()
    for x in lines:
        parts = x.strip().split()

        if (len(parts) == 0):
            header.append(x)
            continue

        if (parts[0] == "boundary"):
            polygon_num = polygon_num + 1
            
            hflag=1
        elif (parts[0] == "layer"):
            layer = parts[1]
        
        elif (parts[0] == "datatype"):
            datatype = parts[1]

        elif (parts[0] == "xy"):
            xy_num = parts[1]
            num = int(xy_num)
            vx=[]
            vy=[]
            j=2
            for i in range (num):
                vx.append(parts[j])
                vy.append(parts[j+1])      
                print(vx[i], vy[i])          
                j=j+2

            p=polygon(layer, datatype, xy_num, vx, vy)
            #v=p.vertex(vx, vy)
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
        f.write("%s" % i)
    for i in range(2):
        polygons[i].printPolygon()
    for i in footer:
        f.write("%s" % i)
    f.close()

print(header)
    




    



    

