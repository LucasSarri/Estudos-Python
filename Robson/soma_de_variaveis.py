#É necessário converter explicitamente o valor recebido do Input poque ele é inicialmente considerado uma string#
n1 = int(input('Digite n1:')) 
n2 = int(input('Digite n2:'))
s = n1+n2
print('A soma entre',n1,'e',n2,'vale',s) #apresentação convencional
print('A soma entre {} e {} vale: {}'.format(n1,n2,s))
