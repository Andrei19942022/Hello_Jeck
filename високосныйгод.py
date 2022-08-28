year = int(input('введите год:'))

if year % 4 !=0:
    print('год обычный!')

elif year % 100  == 0:
    if year % 400 == 0:
        print('год високосный!')

    else:
       print('год обычный!')
else:
  print('год високосный!')
