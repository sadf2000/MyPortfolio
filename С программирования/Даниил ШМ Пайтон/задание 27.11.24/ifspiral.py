ans = input('Хотите спираль?')
if ans == 'да':
    print('Работаем.')
    import turtle as t
    tP = t.Pen()
    tP.width(2)
    for x in range(100):
        tP.forward(2*x)
        tP.left(89)
        print('100/'+str(x))
    print('Законченно!')
