def golf(n):
 while 1:
  n+=1;r=1
  for d in range(2,n):
   if not n%d:r=0;break
  if r and int(str(n)[::-1])==n:return n
