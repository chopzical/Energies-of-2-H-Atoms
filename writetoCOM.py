def WriteToCom(n,y2):
    
    x1 = 0.0
    y1 = 0.0
    z1 = 0.0
    x2 = 0.0 
    #y2 = 10.0
    z2 = 0.0

    #for x in range(8):
        #n = n + 1
    with open("test_{0}.com".format(n), "w") as f:
            f.write("%nprocshared=1\n%mem=500MB\n%chk=test_{0}.chk\n# wb97xd/aug-cc-pvtz\n\nTwo Hydrogens\n\n0 1\n".format(n))
            f.write("H {0} {1} {2}\n".format(x2, y2, z2))
            f.write("H {0} {1} {2}\n".format(x1, y1, z1))
            f.write("\n")
            


