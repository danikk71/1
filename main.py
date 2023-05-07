# dict_1 = {
#     'Nick':{
#         'phone':'2342334324234',
#         'insta':'@fssd'
#     },
#     'Anna':{
#         'phone':'123125324513',
#         'insta':'@21321ls'
#     },
#     'Rick':{
#         'phone':'021843094032',
#         'insta':'@;s;doif'
#     }
# }
#
#
# user = input('Enter name: ')
# userin = input('Enter 2 : ')
#
# print(dict_1[user][userin])

dict_1 = {
    'Nick':{
        'phone':'2342334324234',
        'insta':'@fssd'
    },
    'Anna':{
        'phone':'123125324513',
        'insta':'@21321ls'
    },
    'Rick':{
        'phone':'021843094032',
        'insta':'@;s;doif'
    }
}

user = input('Enter name: ')

for x in dict_1:
    if x == user:
        print('True')