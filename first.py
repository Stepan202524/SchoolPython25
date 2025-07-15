# Декораторы
def answer(question):
    return 'Dumay!'

def dialog():
    def answer(question):
        if question.lower().startswith('kogda'):
            return 'nikogda'
        else:
            return 'Upppss'
    question = input()
    while question != '':
        print(answer(question))
        question = input()

dialog()