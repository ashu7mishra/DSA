def solve(A, B):
    hash_1 = {97:'a', 98:'b',99:'c',100:'d',101:'e',102:'f',103:'g',104:'h',105:'i',106:'j',
    107:'k',108:'l',109:'m',110:'n',111:'o',112:'p',113:'q',114:'r',115:'s',116:'t',117:'u',118:'v',
    119:'w',120:'x',121:'y',122:'z'}

    find = ''
    if B in hash_1:
        find = hash_1[B]
    print(find)
    for i in range(len(A)):
        if A[i] == find:
            return i
    return -1

A = "bvymzikytswvgniflzbyyrkcojuxedcviygnxuckqxmiqtzsqvrvppsnmaoghsxoierzuuecjlxwievsxcesfqsaeg"
B = 99
print(solve(A, B))