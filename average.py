#!/usr/bin/env python3
N=10
average=0.0
sum=0.0
count=0
print("please input 10 integers:")
while count<N:
    number=float(input())
    sum=sum+number
    count=count+1
average=sum//N
print("N={},sum={}".format(N,sum))
print("average={:.2f}".format(average))

