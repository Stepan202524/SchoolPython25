# Декораторы
def upper_case_print(old_func):
    def new_func(*args, **kwargs):
        case = kwargs.pop('case', None)
        if case == 'U':
            args = [str(arg).upper() for arg in args]
        elif case == 'L':
            args = [str(arg).lower() for arg in args]
        return old_func(*args, **kwargs)
    return new_func

new_print = upper_case_print(print)
new_print('Privet, Poka')
new_print('PRIVet, pOKA', case='L')

# def answer(question):
#     return 'Dumay!'
#
# def dialog():
#     def answer(question):
#         if question.lower().startswith('kogda'):
#             return 'nikogda'
#         else:
#             return 'Upppss'
#     question = input()
#     while question != '':
#         print(answer(question))
#         question = input()
#
# dialog()