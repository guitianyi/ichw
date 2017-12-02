def exchange(currency_from,currency_to,amount_from):
    from urllib.request import urlopen
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from={}&to={}&amt={:f}'.\
                  format(currency_from,currency_to,amount_from))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    just=jstr.replace(' ','')
    a=just.replace('"',' ')
    b=a.split()
    c=b[7]
    d=''
    for x in c:
        if x in ('1','2','3','4','5','6','7','8','9','0','.'):
            d=d+x
    d=float(d)
    return d

