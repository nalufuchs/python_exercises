from time import sleep
import emoji
print('\033[36m=-\033[m'*15)
print('\033[36mOs fogos de artifício irão começar em...\033[m')
print('\033[36m=-\033[m'*15)

for f in range (10, -1, -1):
    print(f)
    sleep(0.5)
print(emoji.emojize('\033[035mFIREWOOOOORK!!\033[m  :sparkler:' ,  language='en'))
