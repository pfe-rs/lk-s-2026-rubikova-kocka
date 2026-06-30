#provera rada biblioteke i implementirano prebacivanje iz resenja sa 6 strana u resenje sa 5 strana
import twophase.solver  as sv


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
    if not isinstance(cube_string, str) or len(cube_string) != 54:
        return False
        
    valid_chars = set('URFDLB')
    if not set(cube_string).issubset(valid_chars):
        return False

    
    try:
        sv.solve(cube_string, patternstring=cube_string)
        return True
    except ValueError as e:
        print(f"Invalid cube: {e}")
        return False



my_cube_string1 = "BLRDURUFUFUDFRLDBDBDLDFUURFRFLDDRRULULRLLBFRFBFLBBUBBD"
my_cube_string2 = "BLRDURUFUFUDFRLDBDBDLDFUURFRFLDDRRULULRLLBFRFBFLBBUBBR"
my_cube_string = ""
if(is_valid(my_cube_string1)):
    my_cube_string = my_cube_string1
elif(is_valid(my_cube_string1)):
    my_cube_string = my_cube_string2

print(is_valid(my_cube_string1))
print(is_valid(my_cube_string2))



print("Calculating solution...")
solution = sv.solve(my_cube_string, 0, 5) 




print("\n--- SOLUTION ---")
print(solution)
print("\n--- SOLUTION 5 sides ---")
print(replaceUp(solution))



