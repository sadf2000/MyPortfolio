def get_questions():
    return [['Какого цвета дневное небо в ясный день?','голубого'],
            ['Что является ответом на вопрос о жизни, Вселенной и всем остальном?','42'],
            ['Какое слово состоит из трех букв обозначает мышеловку?','кот'],
            ['Какой звук издает по-настоящему продвинутая машина?','пинг']]

def check_questions(ga):
    question = ga[0]
    ans = ga[1]
    UserAns = input(question)
    if UserAns.lower() == ans:
        print('Правильно!')
        return True
    else:
        print('Не правильно! Ответ:',ans)
        return False

def start_test(questions):
    if len(questions) == 0:
        print('Ошибка')
        return
    index = 0
    right = 0
    while index < len(questions):
        if check_questions(questions[index]):
            right += 1
        index += 1
    print('Вы получили', right*100/len(questions),'% правильно из', len(questions))
    input()

start_test(get_questions())
