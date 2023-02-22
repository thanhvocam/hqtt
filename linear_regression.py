def avg_x(lis):
   for i in range(len(lis)):
     tbc_x = sum(lis)/len(lis)
     return tbc_x
 
def avg_y(lis):
   for i in range(len(lis)):
     tbc_y = sum(lis)/len(lis)
     return tbc_y
def delta_x(lis):
  list_x = []
  for i in lis:
    delta_x = i - avg_y(lis)
    list_x.append(delta_x)
  return list_x

def delta_y(lis):
  list_y = []
  for i in lis:
    delta_y = i - avg_y(lis)
    list_y.append(delta_y)
  return list_y
def multi_xy(list_x,list_y):
  list_multi = []
  for a,b in zip(list_x,list_y):
    multi = a*b
    list_multi.append(multi)
  return list_multi

def square(list_x):
  square_list_x = []
  for i in list_x:
    square = i**2
    square_list_x.append(square)
  return square_list_x
def tinh_hqtt(x,y):
  tbc_x = avg_x(x)
  tbc_y = avg_y(y)
  deltax = delta_x(x)
  deltay = delta_y(y)
  multi = multi_xy(deltax,deltay)
  binhphuong = square(deltax)
  beta = sum(multi)/sum(binhphuong)
  alpha = tbc_y - beta*tbc_x
  return beta, alpha

print(tinh_hqtt([1,2,3],[4,5,6]))
