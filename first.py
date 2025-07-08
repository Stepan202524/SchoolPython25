# Практикум (обучаемый словарь)
import pickle
from fnmatch import translate

# минимальная версия, если файл dict.dat отсутствует

voc = {
    'стол': 'table',
    'стул': 'chair',
    'дверь': 'door'
}
# функция распечатки словаря
def print_voc():
    print('Soderjanie slovarya: ')
    for k, v in voc.items():
        print(k, '-', v)
# Загружаем словарь из файла
try:
    with open('dict.dat', 'rb') as dump_in:
        voc = pickle.load(dump_in)
except FileNotFoundError:
    with open('dict.dat', 'wb') as dump_out:
        pickle.dump(voc, dump_out)
    print('Sozdan minimal slovar')
    print_voc()

while True:
    temp = input('\nVvedite slovo dlya perevoda or "#" dlya konca: ')
    word = temp.strip().lower()
    if word == '#' or word == '№':
        break
    if word in voc.keys():
        translate = voc[word]
        print(f'Slovo "{word}" perevod: {translate}.\n')
    else:
        print(f'Slovo "{word}" net v slovare.')
        newkey = f'Kakoy perevod slova "{word}"? \n'
        newkey += 'Esli net vvoda, Press ENTER '
        newkey += 'ili vvedite ego tut: '
        new_word = input(newkey)

        if new_word != '' or len(new_word) > 2:
            voc[word] = new_word
            print(f'Slovo {word} s perevodom {new_word} vneseno v slovar')
        else:
            print('Nichego ne vvedeno')
            continue
# СОхранить словарь
with open('dict.dat', 'wb') as dump_out:
    pickle.dump(voc, dump_out)
print('Bay Bay')