import os

def create_pos_n_neg():
  for img in os.listdir('neg'):
    with open('bg.txt', 'a') as f:
      f.write(img + '\n')

  for img in os.listdir('pos'):
    with open('info.dat', 'a') as f:
      f.write(img + ' 1 0 0 128 128 \n')

create_pos_n_neg()