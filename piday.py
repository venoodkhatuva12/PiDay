#!/bin/python

#viete series
import time
start_time = time.time()

def pi():
  pi = 0 #Using initial pi series will start from 0
  n = 4 #Using n represents the numerator of the fraction
  d = 1 # Using d is denominator
  for i in range(1, 100000):
    a = 2*(i % 2) - 1
    pi +=a*n/d
    d +=2
  print(pi)

pi()

end_time = time.time()
print(end_time - start_time)

#wallis series
import time
start_time = time.time()
def wallis(n):
    pi = 0.0   
    for i in range(1, n):
        x = 4 * (i ** 2)
        y = x - 1
        z = float(x) / float(y)
        if (i == 1):
            pi = z
        else:
            pi *= z
    pi *= 2
    return pi

print(wallis(100000))
end_time = time.time()
print(end_time - start_time)


#leibniz series
import time
start_time = time.time()
def myPi(n):
    denominator = 1
    addto = 1

    for i in range(n):
        denominator = denominator + 2
        addto = addto - (1/denominator)
        denominator = denominator + 2
        addto = addto + (1/denominator)

    pi = addto * 4

    return(pi)

print(myPi(1000000))
end_time = time.time()
print(end_time - start_time)


#nikantha's series
import time
start_time = time.time()

def nilakantha(reps):
        result = round(3.0)
        op = 1
        n = 2
        for n in range(2, 2*reps+1, 2):
                result += 4/round(n*(n+1)*(n+2)*op)
                op *= -1

        return result

iterations = int(100000)
print(nilakantha(iterations))
end_time = time.time()
print(end_time - start_time)