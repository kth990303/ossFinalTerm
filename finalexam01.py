def calpi(num):
    ans=0;
    for i in range(1,num+1):
        ans+=((-1)**(i+1))*(1/(float)(2*i-1))
    return ans*4

print(" i              m(i)")
for k in range(1,1001, 100):
    print("%3d            %.4f"%(k,calpi(k)))
