# ȭ���� �̸�Ƽ�� s, Ŭ�������� �̸�Ƽ�� c

# 1. ȭ�鿡 �ִ� �̸�Ƽ���� ��� �����ؼ� Ŭ�����忡 �����Ѵ�.
# ���� : (s,c) -> (s,s)
# 2. Ŭ�����忡 �ִ� ��� �̸�Ƽ���� ȭ�鿡 �ٿ��ֱ� �Ѵ�.
# �ٿ��ֱ� : (s,s) -> (s+c, c)
# 3. ȭ�鿡 �ִ� �̸�Ƽ�� �� �ϳ��� �����Ѵ�.
# (s,c) -> (s-1, c)

# => ��� ������ 1�ʰ� �ɸ��� ��� ����� ����ġ�� 1�̴�.
# ����, dist[s][c] + 1 �� ���� 1�� ������� �Ѵ�.

from collections import deque
n = int(input())
emoji = [[-1] * (n+1) for _ in range(n+1)]
emoji[1][0] = 0

def bfs(n):
    q = deque()
    q.append((1, 0))
    while q:
        s, c = q.popleft()
        if emoji[s][s] == -1:  # �ϳ��� ó�� �ȵ� ����
            emoji[s][s] = emoji[s][c] + 1  # �ϳ��� ó�� �ȵ� ���¸� 1�� ���� ����
            q.append((s, s))
        if s+c <= n and emoji[s+c][c] == -1:  # 1���� ����ǰ� 2���� ���� �ȵ� ������ ��
            q.append((s+c, c))
            emoji[s+c][c] = emoji[s][c] + 1  # 2�� ���� ����
        if s-1 >= 0 and emoji[s-1][c] == -1:  # 2���� ����ǰ� 3���� ���� �ȵ� ������ ��
            q.append((s-1, c))
            emoji[s-1][c] = emoji[s][c] + 1  # 3�� ���� ����


bfs(n)
answer = -1
for i in range(n+1):
    if emoji[n][i] != -1:
        if answer == -1 or answer > emoji[n][i]:
            answer = emoji[n][i]

print(answer)