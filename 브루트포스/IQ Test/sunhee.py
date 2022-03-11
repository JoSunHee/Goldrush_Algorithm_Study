#1. 주어진 리스트를 통해 뒤 숫자가 나올 수 있는지 확인(A,B or 숫자)
#2. 숫자가 나올 수 있는 리스트라면 a,b 구하기
#3. (앞 수 * a + b)=뒷 수 => nlist[1]=nlist[0]*a+b
import sys
n=int(sys.stdin.readline())
nlist=list(map(int,sys.stdin.readline().split()))

if n==1:    #1개면 뒤에 숫자 예측 불가 -> 무조건 A
    print('A')
elif n==2:
    if nlist[0]==nlist[1]:
        print(nlist[0])
    else:   #서로 다른 2개면 뒤에 숫자 예측 불가 -> 무조건 A
        print('A')
else:   #a,b 구하기
    if nlist[1]==nlist[0]:  #1,2번째가 같은 수일 때 뒤 숫자들은 모두 이 숫자들과 같아야 됨. 
        for i in range(2,len(nlist)):
            if (nlist[i]-nlist[i-1])!=0:    #하나라도 다르면 규칙X
                print('B')
                exit()
        else:
            print(nlist[-1])
    else:
        # a=nlist[1]-nlist[0]
        # b=nlist[1]-a*nlist[0]
        a=(nlist[2]-nlist[1])/(nlist[1]-nlist[0])
        if a!=int(a):   #a는 정수여야 함
            print('B')
            exit()
        b=nlist[1]-nlist[0]*a
        for i in range(2,len(nlist)):
            if nlist[i]!=(nlist[i-1]*a+b):
                print('B')
                break
        else:
            print(int(nlist[-1]*a+b))
