print("Program Hitung Total Keuntungan")

x = int(input("Uang Modal Awal: "))

a = 0*x
b = 0*x
c = 0.01*x
d = 0.01*x
e = 0.05*x
f = 0.05*x
g = 0.05*x
h = 0.02*x
y=[a,b,c,d,e,f,g,]

for i in range(len(y)):
    print("laba bulan ke",i+1 ,"sebesar: ",y[i])
z=(a+b+c+d+e+f+g+h)
print("Jumlah laba selama 8 bulan: ",z)