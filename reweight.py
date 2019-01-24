
def reweight(input_tuple, outfilename, minv1, maxv1,  minv2, maxv2, i1, i2, temp):
    _minv1 = minv1
    _maxv1 = maxv1
    _minv2 = minv2
    _maxv2 = maxv2
    _i1 = i1
    _i2 = i2
    _temp = temp

    ofile = open(outfilename, 'w')    # open file for writing
    i1 = int(_i1)
    i2 = int(_i2)
    minv1 = float(_minv1)
    maxv1 = float(_maxv1)
    minv2 = float(_minv2)
    maxv2 = float(_maxv2)
    V = np.zeros((i1, i2))
    DG = np.zeros((i1, i2))
    I1 = maxv1 - minv1
    I2 = maxv2 - minv2
    kB = 3.2976268E-24
    An = 6.02214179E23
    T = float(_temp)

    for x_value, y_value in input_tuple:
        v1 = x_value
        for x in range(i1):
            if v1 <= minv1 + (x + 1) * I1 / i1 and v1 > minv1 + x * I1 / i1:
                v2 = y_value
    for y in range(i2):
        if v2 <= minv2 + (y + 1) * I2 / i2 and v2 > minv2 + y * I2 / i2:
            V[x][y] = V[x][y] + 1

    P = list()
    for x in range(i1):
        for y in range(i2):
            P.append(V[x][y])
    Pmax = max(P)

    LnPmax = math.log(Pmax)

    for x in range(i1):
        
        for y in range(i2):
            
            if V[x][y] == 0:
                DG[x][y] = 10
                
            else:
                DG[x][y] = -0.001 * An * kB * T * (math.log(V[x][y])-LnPmax)
                
    for x in range(i1):
        for y in range(i2):
            ofile.write(str((2 * minv1 + (2 * x + 1) * I1 / i1) / 2) + "\t" 
                        + str((2 * minv2 + (2 * y + 1) * I2 / i2) / 2) + "\t" + str(DG[x][y])
                        + "\n")
        ofile.write("\n")

