keyA=9
keyB=4
plaintext = ""
ciphertext = "nbela bove w okt fc tbok nar tbeleyz yz r m e jek f ewwortk ac fo jarwtcetyar ieyk w okt rabiez yz odyktobe fok nynzyatposcok jacb woze e z eloryb ho tbaclo tbok nyor sco lack emov wafo zok okjewok ieyk lack ecbyov jc wpaykyb fo zok kcjjbyiob ac fo wafob kcb lyrgt kojt webewtobok jeb odoijzo xozywytetyark or tact wek iobwy jacb wo noec jbagbeiio narro wartyrcetyar ot narrok lewerwok"

di = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
      'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23,
      'y': 24, 'z': 25, ' ': ' ', 'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
      'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21,
      'W': 22, 'X': 23, 'Y': 24, 'Z': 25, 'é': 4}

dy = {'0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e', '5': 'f', '6': 'g', '7': 'h', '8': 'i', '9': 'j', '10': 'k',
      '11': 'l', '12': 'm', '13': 'n', '14': 'o', '15': 'p', '16': 'q', '17': 'r', '18': 's', '19': 't', '20': 'u',
      '21': 'v', '22': 'w', '23': 'x', '24': 'y', '25': 'z', ' ': ' '}

def mod26(x):
    return x%26

def cipher(plaintext):
    chain = plaintext
    len(chain)
    index = 0
    List=[]
    for index in range(len(chain)):
        if chain[index] in di:
            List.append(di[chain[index]])
    ListAffine=[]
    q=0
    for q in range(len(chain)):
        if List[q]==' ':
            ListAffine.append(List[q])
        else:
            ListAffine.append(List[q] * keyA + keyB)
            q = q + 1
    ListMod=[]
    w=0
    for w in range(len(chain)):
        if ListAffine[w]==' ':
            ListMod.append(List[w])
        else:
            ListMod.append(mod26(ListAffine[w]))
            w = w + 1
    p=0
    for k in range(len(chain)):
        if p==0:
            p=dy[str(ListMod[k])]
            pass
        else:
            p = str(p) + dy[str(ListMod[k])]
    return p

# print("I am delighted to introduce you your ciphered message : " + cipher(plaintext)) #english way
# print("J'ai l'honneur de vous présenter votre message crypté : " + cipher(plaintext)) #french touch

def decipher(ciphertext):
    chain = ciphertext
    len(chain)
    index = 0
    List=[]
    while index < len(chain):
        if chain[index] in di:
            List.append(di[chain[index]])
            index = index + 1
    ListBright = []
    q = 0
    for q in range(len(chain)):
        if List[q]==' ':
            ListBright.append(List[q])
        else:
            t = 0
            while mod26(keyA * t + keyB) != List[q]:
                t = t + 1
            ListBright.append(dy[str(t)])
            q = q + 1
    p=0
    for i in range(len(chain)):
        if p==0:
            p=ListBright[i]
            pass
        else:
            p = p + ListBright[i]
    return p

# print("I am delighted to introduce you your deciphered message : " + decipher(ciphertext)) #english way
print("J'ai l'honneur de vous présenter votre message décrypté : " + decipher(ciphertext)) #french touch

# written by Réza Machraoui in 2020
# with PyCharm