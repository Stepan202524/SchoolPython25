import pprint
import pickle
# dic= {
#     'стол': 'table',
#     'стул': 'chair',
#     'дверь': 'door'
# }
# # Сериализация
# with open('dict.dat', 'wb') as p:
#     pickle.dump(dic, p)
# Десериализация
with open('dict.dat', 'rb') as p:
    d = pickle.load(p)
pprint.pprint(d, width=11)

from path_lib import *
print(img_dir, '\n', font_dir)