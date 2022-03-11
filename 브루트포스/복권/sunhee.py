#한 개를 뽑으면 남은 것이 변하는 문제 -> 조합 문제 -> comb사용

import sys
from math import comb

n,m,k=map(int,sys.stdin.readline().split())
total=comb(n,m) #전체 확률= n개 중에서 m개를 뽑을 때
prob=0

for i in range(k,m+1):           #뽑은 m개 중에서 k개 겹칠 확률=mCk인데 k는 1씩 늘어나는 경우 모두 계산(왜? 적어도니까)
    prob+=comb(m,i)*comb(n-m,m-i) #당첨확률을 계산하기 위해서 남은 카드 중에 k개를 뽑지 못하는 확률을 계산

print(prob/total)   #(k개 뽑을 확률*k개 뽑지 못학 확률)/n개 중 m개 뽑을 확률
