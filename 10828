import sys
tm=int(sys.stdin.readline())
stack=[]


def order(ordertext):
  num=0
  if ' ' in ordertext:
    name,num=ordertext.split()
  else:
    name=ordertext
  if name=='push':
    stack.append(num)
  elif name=='pop':
    if len(stack)==0:
      print(-1)
    else:
       print(stack.pop(-1))
  elif name=='size':
    print(len(stack))
  elif name=='empty':
    if len(stack)>0:
      print('0')
    else:
      print('1')
  else: #왜 여기로 빠질까
    if len(stack)==0:
      print(-1)
    else: 
      print(stack[-1])

for i in range(tm):
  a=sys.stdin.readline()
  order(a)
