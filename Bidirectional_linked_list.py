from collections import deque
q=deque([])
while True:
    try:
        s=input()
    except:
        break

    if s=="deleteFirst":
        q.popleft()
        continue
    elif s=="deleteLast":
        q.pop()
        continue
    
    try:
        s,n=s.split()
    except:
        break
    if s=='insert':
        q.appendleft(int(n))
    elif s=="delete":
        q.remove(int(n))
print(q)
    