


def pwd_validity(data):

    count = 0
    for i in data:
        count += 1
    if count == 0:
        return 'empty string'
    elif type(data)!= str:
        return 'invalid data'
    elif not count==4 or count==6:
        return 'data must have length of 4 or 6'

    else:
        out = 'valid pwd'

        for i in data:

            if i not in ['1','3','5','7','9']:

                out = 'invalid pwd'
        return out

result = pwd_validity('137 ')

print(result)