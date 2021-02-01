--Print
    print('A soma vale ',s) //apresentação padrão
    print('A soma vale {}'.format(s)) //apresentação nova
--IF
x = int(input("Entre com um inteiro: "))
if x < 0:
    x = 0
    print('Negativo se torna 0');
elif x == 0:
    print('Zero')
elif x == 1:
    print('Um')
else
    print('Vários')

--For
words = ['gato','janela']
for w in words:
    print(w,len(w))

for i in range(5):
    print(i)

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n, ' = ', x,' * ',n//x)
            break
    else:
        print(n,'numero primario')

--While
    while True:
        pass

--Funções
    def fib(n):
        result = []
        a, b = 0, 1
        while a < n :
            result.append(a) //chama um método do objeto lista result, este método informa que um determinado valor pertence ao objeto que chama o método
            a, b = b, a+b
        return result

    def ask_ok(prompt, retries = 4, remider = 'Please try again'):
        while True:
            ok = input(prompt)
            if ok in ('y','ye','yes'):
                return True
            if ok in ('n','no','nop','nope'):
                return False
            retries = retries - 1
            if retries < 0:
                raise ValueError('Invalid user responsw')
            print(remider)