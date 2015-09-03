import os
diraddress = "htlall/"
files = os.listdir(diraddress) 
a = []
fmin = 0
fmax = 0
for i in a:
    dic = {}
    s=str(i)+"-"+str(i+100000000)+".txt"
    print s
    f=file(s,"w+")
    for filename in files:
        k=0
        file_object = open(diraddress+filename)
        for line in file_object:
            k+=1
            if k%10000000==0:
                print k
            l = line.rstrip('').split("\x01")
            #print l[0]
            if int(l[0]) > fmax:
                fmax = l[0]
            if int(l[0]) < fmin:
                fmin = l[0]
            if int(l[0]) >= i and int(l[0]) <(i+100000000):
                if l[0] not in dic:
                    dic[l[0]] = 0
                    f.writelines(line)
                else:
                    continue
            else:
                continue
        file_object.close()
        print len(dic)

    f.close()
print fmin
print fmax