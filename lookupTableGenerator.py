# pocetak implementacije algoritma od nule
corners = [[0, 0],
           [1, 0],
           [2, 0],
           [3, 0],
           [4, 0],
           [5, 0],
           [6, 0],
           [7, 0],]

edges =   [[0, 0],
           [1, 0],
           [2, 0],
           [3, 0],
           [4, 0],
           [5, 0],
           [6, 0],
           [7, 0],
           [8, 0],
           [9, 0],
           [10, 0],
           [11, 0],]

def pisiKocku():
    print("coskovi:")
    for c in corners:
        print(c)
    print("ivice:")
    for e in edges:
        print(e)

def L(turning_amount):
    
    if turning_amount == 0:
        turning_amount = 3
    for i in range(turning_amount):
        #promena rotacionih brojeva
        corners[2][1]+=1
        corners[3][1]+=2
        corners[7][1]+=1
        corners[6][1]+=2
        
        #promena pozicija coskova
        temp = corners[6]
        corners[6] = corners[7]
        corners[7] = corners[3]
        corners[3] = corners[2]
        corners[2] = temp
        

        #promena pozicija ivica
        temp = edges[3]
        edges[3] = edges[6]
        edges[6] = edges[11]
        edges[11] = edges[7]
        edges[7] = temp
    for c in corners:
        c[1] = c[1]%3

def R(turning_amount):
    if turning_amount == 0:
        turning_amount = 3
    for i in range(turning_amount):
        #promena rotacionih brojeva
        corners[0][1]+=1
        corners[1][1]+=2
        corners[5][1]+=1
        corners[4][1]+=2
        #promena pozicija coskova
        temp = corners[0]
        corners[0] = corners[4]
        corners[4] = corners[5]
        corners[5] = corners[1]
        corners[1] = temp
        #promena pozicija ivica
        temp = edges[1]
        edges[1] = edges[4]
        edges[4] = edges[9]
        edges[9] = edges[5]
        edges[5] = temp
    for c in corners:
        c[1] = c[1]%3


def B(turning_amount):
    if turning_amount == 0:
        turning_amount = 3
    for i in range(turning_amount):
        #promena rotacionih brojeva
        corners[1][1]+=1
        corners[2][1]+=2
        corners[6][1]+=1
        corners[5][1]+=2
        #promena pozicija coskova
        temp = corners[1]
        corners[1] = corners[5]
        corners[5] = corners[6]
        corners[6] = corners[2]
        corners[2] = temp
        #promena rotacionih brojeva ivica
        edges[2][1]+=1
        edges[5][1]+=1
        edges[6][1]+=1
        edges[10][1]+=1

        #promena pozijica ivica
        temp = edges[5]
        edges[5] = edges[10]
        edges[10] = edges[6]
        edges[6] = edges[2]
        edges[2] = temp
    for c in corners:
        c[1] = c[1]%3
    for e in edges:
        e[1] = e[1]%2

def F(turning_amount):
    if turning_amount == 0:
        turning_amount = 3
    for i in range(turning_amount):
        #promena rotacionih brojeva
        corners[3][1]+=1
        corners[0][1]+=2
        corners[4][1]+=1
        corners[7][1]+=2
        #promena pozicija coskova
        temp = corners[3]
        corners[3] = corners[7]
        corners[7] = corners[4]
        corners[4] = corners[0]
        corners[0] = temp
        #promena rotacionih brojeva ivica
        edges[0][1]+=1
        edges[7][1]+=1
        edges[8][1]+=1
        edges[4][1]+=1

        #promena pozijica ivica
        temp = edges[0]
        edges[0] = edges[7]
        edges[7] = edges[8]
        edges[8] = edges[4]
        edges[4] = temp
    for c in corners:
        c[1] = c[1]%3
    for e in edges:
        e[1] = e[1]%2

def D(turning_amount):
    if turning_amount == 0:
        turning_amount = 3
    for i in range(turning_amount):
        #promena pozicija coskova
        temp = corners[5]
        corners[5] = corners[4]
        corners[4] = corners[7]
        corners[7] = corners[6]
        corners[6] = temp
        #promena pozijica ivica
        temp = edges[8]
        edges[8] = edges[11]
        edges[11] = edges[10]
        edges[10] = edges[9]
        edges[9] = temp

def U(turning_amount):
    if turning_amount == 0:
        turning_amount = 3
    for i in range(turning_amount):
        #promena pozicija coskova
        temp = corners[0]
        corners[0] = corners[1]
        corners[1] = corners[2]
        corners[2] = corners[3]
        corners[3] = temp
        #promena pozijica ivica
        temp = edges[2]
        edges[2] = edges[3]
        edges[3] = edges[0]
        edges[0] = edges[1]
        edges[1] = temp

def fU(turning_amount):
    
        

    R(1)
    L(1)
    F(2)
    B(2)
    R(0)
    L(0)
    D(turning_amount)
    R(1)
    L(1)
    F(2)
    B(2)
    R(0)
    L(0)

#iz stanja u koordinatu
#State to Coordinates
def CornerOrientationStC():
    coordinate = 0
    for i in range(7):
        coordinate = coordinate+( corners[i][1] * 3**(6-i))
        
        print("vrednost za dodavanje: ", corners[i][1] * 3**(6-i))


    return coordinate

def CornerOrientationCtS(coordinate):
    for i in range(7):
        corners[6-i][1] = coordinate%3
    corners[7][1] = 0


    

    