import string

numb = int(input(''))

if numb in range(0,10000):
    unid    = numb%10
    dez     = (numb //10 )%10
    cente   = (numb //100) %10
    milhar  = (numb //1000)
    print('Unidade {}\nDezenas {}\nCentenas {}\nMilhar {}\n'.format(unid,dez,cente,milhar))







