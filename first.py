print('Ходы:\n\tL-left\n\tR- Right\n\tF-Forward\n\tQ - exit')

while True:
    ch = input('Yor choise')
    match ch:
        case 'L' | 'l' | 'л' | 'Л':
            print('Turn left')
        case 'R':
            print('Turn right')
        case 'F':
            print('Turn forward')
        case ' ':
            print('No choice')
        case 'Q':
            print('Bay')
            break
        case _:  # default
            print('Choice ne ponyatno')