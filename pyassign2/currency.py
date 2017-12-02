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
    if d=='':
        d='Exchange currency code is invalid'
    else:
        d=float(d)
    return d
def test_exchange():
    assert(exchange('USD','CNY',100)==652.615)
    assert(exchange('BHD','MTL',100)=='Exchange currency code is invalid')
    assert(exchange('BHD','MUR',100)==8721.8615407464)

def test_ALL():
    test_exchange()
    print('test passed')
