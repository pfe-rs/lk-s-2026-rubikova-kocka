from face import FaceCube
from cubie import CubieCube
import solver  # Assuming you are using the original search.py for solving



def replaceUp(solution):
    exit = False
    while(exit == False):
        exit = True
        for i in range(len(solution)):
            if(solution[i] == 'U'):
                exit = False
                break
        if i != len(solution)-1:
            string1 = solution[0:i]
            string2 = solution[i+2:]
            replacement = "R1 L1 F2 B2 R3 L3 D" + solution[i + 1] + " R1 L1 F2 B2 R3 L3"
            solution = string1 + replacement + string2
    return solution

def is_valid(cube_string: str) -> bool:
    print("Ulaz u funkciju")
    if not isinstance(cube_string, str) or len(cube_string) != 54:
        print("Duzina niza za kreiranje kocke ne odgovara", isinstance(cube_string, str), len(cube_string))
        print(cube_string)
        return False
        
    valid_chars = set('URFDLB')
    if not set(cube_string).issubset(valid_chars):
        print("nevalidni karakteri")
        return False

    try:
        fc = FaceCube()
        fc.from_string(cube_string)
        cc = fc.to_cubie_cube()
        # verify() returns 0 for a valid cube
        print(cc.verify())
        return cc.verify() == True
    except Exception as e:
        print(f"Validation error: {e}")
        return False


def ColourToId(c):
    match c:
        case 'U':
            return 0
        case 'D':
            return 1
        case 'F':
            return 2
        case 'B':
            return 3
        case 'R':
            return 4
        case 'L':
            return 5
    return -1
        
def IdToColour(I):
    match I:
        case 0:
            return 'U'
        case 1:
            return 'D'
        case 2:
            return 'F'
        case 3:
            return 'B'
        case 4:
            return 'R'
        case 5:
            return 'L'
    return ''
    

def SolveFromPartial(cube_string):
    if(cube_string.count(' ') != 2 or len(cube_string) != 54):
        print("lose formatiran unosni string", cube_string.count(' '), len(cube_string) != 54)
        return
    colourAmounts = [9, 9, 9, 9, 9, 9]
    #UDFBRL
    index1 = -1
    index2 = -1

    for i in range(len(cube_string)):
        
        if ColourToId(cube_string[i]) != -1:
                colourAmounts[ColourToId(cube_string[i])] -= 1
        
        if(cube_string == ' '):
            if(index1 == -1):
                    index1 = i
            elif(index2 == -1):
                    index2 = i
    
    print(colourAmounts)
        
    
    fill1 = ' '
    fill2 = ' '
    for i in range(6):
        if(colourAmounts[i] == 1):
            if(fill1 == ' '):
                fill1 = IdToColour(i)
            elif(fill2 == ' '):
                fill2 = IdToColour(i)
    
    print(fill1, fill2)
    list1 = list(cube_string)
    list2 = list(cube_string)


    helper = True
    for i in range(54):
        if(cube_string[i] == ' ' and helper == False):
            print("drugi")
            list1[i] = fill2
            list2[i] = fill1
        if(cube_string[i] == ' ' and helper == True):
            print("prvi")
            list1[i] = fill1
            list2[i] = fill2
            helper = False
        

    print(cube_string)
    
    string1 = "".join(list1)
    string2 = "".join(list2)

    print(string1)
    print(string2)

    my_cube_string = ""
    if is_valid(string1):
       my_cube_string = string1
    elif is_valid(string2):
        my_cube_string = string2

    print(f"Is string 1 valid? {is_valid(string1)}")
    print(f"Is string 2 valid? {is_valid(string2)}")

    if my_cube_string:
        print("Calculating solution...")
        solution = solver.solve(my_cube_string, 20) 

        print("\n--- SOLUTION ---")
        print(solution)
        print("\n--- SOLUTION 5 sides ---")
        print(replaceUp(solution))
    else:
        print("No valid cube string found.")



my_cube_string = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLL  BBBBBBBB"
SolveFromPartial(my_cube_string)
