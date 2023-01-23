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
        print("{}".format(self.xy_num), file=f, end=" ")
        #f.write("xy", self.xy_num, end="")
        #print(self.xy)

        num=int(self.xy_num)

        for i in range (0, num):
            #f.write(self.xy.x[i], end=" ")
            print("{}".format(self.xy.x[i]), file=f, end=" ")
            #f.write(self.xy.y[i], end=" ")
            print("{}".format(self.xy.y[i]), file=f, end=" ")

        #print("{}".format(self.xy.x[i]), file=f)
        print("", file=f)
        print("endel", file=f)
    pass


def read_polygon(file, header, footer, polygons):
    hflag=0
    lines=file.readlines()
    for x in lines:
        parts = x.strip().split()

        if (len(parts) == 0):
            header.append(x)
            continue

        if (parts[0] == "boundary"):
            #polygon_num = polygon_num + 1
            
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
                #print(vx[i], vy[i])          
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

    return header, footer, polygons

def polygonArea(X, Y, n):
    area = 0.0
    # Calculate value of shoelace formula
    j = n - 1
    for i in range(0,n):
        area += (X[j] + X[i]) * (Y[j] - Y[i])
        j = i   # j is previous vertex to i
    # Return absolute value
    return int(abs(area / 2.0))

with open (r"milestone2/POI.txt") as f:
    rheader=[]
    rfooter=[]
    rpolygons=[]
    rheader, rfooter, rpolygons = read_polygon(f, rheader, rfooter, rpolygons)

f.close()

with open(r"milestone2/Source.txt") as f:
    spolygons=[]
    sheader=[]
    sfooter=[]
    sheader, sfooter, spolygons = read_polygon(f, sheader, sfooter, spolygons)

f.close()

rpolx=[]
rpoly=[]

for i in range(7):
    rpolx.append(int(rpolygons[0].xy.x[i]))
    rpoly.append(int(rpolygons[0].xy.y[i]))

ref_area=polygonArea(rpolx, rpoly, 7)
print(ref_area)

#print(rpolygons[0].xy.x)
#print(rpoly)

spol_area=[]

for i in range (len(spolygons)):
    spolx=[]
    spoly=[]
    for j in range (len(spolygons[i].xy.x)):
        spolx.append(int(spolygons[i].xy.x[j]))
        spoly.append(int(spolygons[i].xy.y[j]))
    spol_area.append(polygonArea(spolx, spoly, len(spolx)))

#print(spol_area)

with open(r"milestone2_output.txt", "w") as f:

    k=0
    for i in sheader:
        f.write("%s" % i)

    for i in range(len(spolygons)):
       if (spol_area[i] == ref_area):
            spolygons[i].printPolygon()
            k=k+1

    for i in sfooter:
        f.write("%s" % i)

    #print(spolygons[0].xy.x)
    print(k)
f.close()