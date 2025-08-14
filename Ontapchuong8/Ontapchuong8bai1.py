list_food=['pho','pizza','com','banhmi','buncha']
# print('Mon an yeu thich cua toi la: ')
# for i in range(len(list_food)):
#     print(f'{i+1}. Toi thich an {list_food[i]}')
    
# for i, food in enumerate(list_food):
#     print(f'{i+1}: Toi thich an {food}')

biendem = 0
for i in list_food:
    print(f'{biendem+1}: Toi thich an {i}')
    biendem+=1