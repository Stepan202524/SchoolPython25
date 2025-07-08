# Библиотека pymorphy
# pip install pymorphy3
#pip install -U pymorphy3-dicts-ru
import pymorphy3

morph = pymorphy3.MorphAnalyzer()
print(morph.parse('Алексей'))

from pymorphy3 import MorphAnalyzer
form = MorphAnalyzer().parse('бутылка')[0]
for btl in reversed(range(11)):
    print(f'V Holodilnike {btl + 1} {form.make_agree_with_number(btl + 1).word}')
    print('Voz`mi sebe odnu! ')
    if btl % 10 == 1 and btl != 11:
        remain = 'Ostalas`'
    else:
        remain = 'Ostalos`'
    print(f'{remain} {btl} {form.make_agree_with_number(btl + 1).word}')


