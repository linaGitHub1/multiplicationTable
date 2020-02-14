for i in range(9):#从0循环到8
  i += 1
  for j in range(i):#从j循环到i
    j += 1
    print(j,'*',i,'=',i*j,end = ' ',sep='')#打印j*i='值'
  print()#回车

print('hello world')
