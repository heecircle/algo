tm=int(input())


def check():
  stack=[]
  arr=input()
  for i in arr:
    if i=='(':
      stack.append(1)
    else:
      if stack==[]:
        print('NO')
        stack=[]
        return
      else:
        stack.pop()
  if stack==[]:
    print('YES')
  else:
    print('NO')


for i in range(tm):
  check()
