import h5py
import matplotlib.pyplot as plt
import numpy as np
import math


f = h5py.File("Tuce-Hamstring-10.h5")["20:15:12:22:84:48"]["raw"]["channel_1"][:, 0]
t = len(f)

print "Kac veri var:", (t)
# sampling_rate_1000Hz_time_calculation_second
time = np.array([i for i in range(0, t, 1)])

# for i in f:
#   print i

# plt.plot(f)
# plt.show()

#x = np.absolute(f)


y = 0.0

for i in f:
    long(y)

    a = (i / 1024) - 0.5
    b = a * 3.3
    c = b / 1009
    n = c * 1000

    y = y + (i)

print "Hepsini topladim:", (y)

z = (1.0/t)*abs(y)
print "Ortalama deger", (z)

k = 0.0
for i in f:
    long(k)

    a = (i / 1024) - 0.5
    b = a * 3.3
    c = b / 1009
    n = c * 1000
    k = k + abs(i - z)

print "mutlak degerleri topladim", k
mad = (1.0/t) * k

print "MAD: ", (mad)

#a = z / 1024 - 0.5
#b = a * 3.3
#c = b / 1009
#n = c * 1000

#print "ortalama degerin mV cevrimi", n


#fig = plt.figure()
#plt.plot(time,f)
#plt.show()
