#Possible moves:
# L,  R,  U,  D,  F,  B  -> L1, R1, U1, D1, F1, B1
# L', R', U', D', F', B' -> L3, R3, U3, D3, F3, B3
# M,  E,  S  -> R1 + L3 + X', U1 + D3 + Y , F3 + B1 + Z
# M', E', S' -> L1 + R3 + X , D1 + U3 + Y', B3 + F1 + Z'
# X(L,  R,  U,  D,  F,  B)  -> L1, R1, F1, B1, D1, U1
# X(L', R', U', D', F', B') -> L3, R3, F3, B3, D3, U3
# Y(L,  R,  U,  D,  F,  B)  -> B1, F1, U1, D1, L1, R1
# Y(L', R', U', D', F', B') -> B3, F3, U3, D3, L3, R3
# Z(L,  R,  U,  D,  F,  B)  -> D1, U1, L1, R1, F1, B1
# Z(L', R', U', D', F', B') -> D3, U3, L3, R3, F3, B3
# X'(L, R, U, D, F, B) -> X(X(X(L))) etc.
# Y'(L, R, U, D, F, B) -> Y(Y(Y(L))) etc.
# Z'(L, R, U, D, F, B) -> Z(Z(Z(L))) etc.

TIMESTOCLEAN = 6 #average in testing, can cut ~100 moves

def applyX(move):
    if move == "U":
        return "F"
    elif move == "D":
        return "B"
    elif move == "F":
        return "D"
    elif move == "B":
        return "U"
    else:
        return move

def applyY(move):
    if move == "L":
        return "B"
    elif move == "R":
        return "F"
    elif move == "F":
        return "L"
    elif move == "B":
        return "R"
    else:
        return move

def applyZ(move):
    if move == "L":
        return "D"
    elif move == "R":
        return "U"
    elif move == "U":
        return "L"
    elif move == "D":
        return "R"
    else:
        return move

def processOrientation(orientations, move):
    for orien in orientations:
        if orien == "X":
            move = applyX(move)
        elif orien == "Y":
            move = applyY(move)
        elif orien == "Z":
            move = applyZ(move)
    return move

def cleanInput(solverMoves):
    i = 0
    while i < len(solverMoves):
        try: #remove moves that have their inverses right afterward
            if solverMoves[i]+'i' == solverMoves[i+1] or solverMoves[i] == solverMoves[i+1]+'i':
                del solverMoves[i]
                del solverMoves[i]
                i -= 1
        except IndexError:
            pass
        
        try: #remove 4-in-a-row moves (they just keep cube the same)
            if solverMoves[i] == solverMoves[i+1]:
                if solverMoves[i+1] == solverMoves[i+2]:
                    if solverMoves[i+2] == solverMoves[i+3]:
                        del solverMoves[i]
                        del solverMoves[i]
                        del solverMoves[i]
                        del solverMoves[i]
                        i -= 1
        except IndexError:
            pass  

        i += 1
    return solverMoves


def convert(solverMoves): #take solverMoves, convert in terms of 6 moves
    #Convert M,E,S,M',E',S' to respective, insert them
    # M,  E,  S  -> R1 + L3 + X', U1 + D3 + Y , F3 + B1 + Z
    # M', E', S' -> L1 + R3 + X , D1 + U3 + Y', B3 + F1 + Z'
    i = 0
    while i < len(solverMoves):
        if solverMoves[i] == 'M':
            solverMoves[i] = "X'"
            solverMoves.insert(i, "L'")
            solverMoves.insert(i, 'R')
        elif solverMoves[i] == 'E':
            solverMoves[i] = "Y"
            solverMoves.insert(i, "D'")
            solverMoves.insert(i, 'U')
        elif solverMoves[i] == 'S':
            solverMoves[i] = "Z"
            solverMoves.insert(i, "B")
            solverMoves.insert(i, "F'")
        elif solverMoves[i] == "Mi":
            solverMoves[i] = "X"
            solverMoves.insert(i, "R'")
            solverMoves.insert(i, 'L')
        elif solverMoves[i] == "Ei":
            solverMoves[i] = "Y'"
            solverMoves.insert(i, "U'")
            solverMoves.insert(i, 'D')
        elif solverMoves[i] == "Si":
            solverMoves[i] = "Z'"
            solverMoves.insert(i, "F")
            solverMoves.insert(i, "B'")
        i += 1
    #Convert inverses to 3x respective, insert them
    i = 0
    while i < len(solverMoves):
        if len(solverMoves[i]) == 2: #inverse
            solverMoves[i] = solverMoves[i][0]
            for j in range(2):
                solverMoves.insert(i, solverMoves[i])
        i += 1
    #Clean out input (remove 4x and C + C')
    for i in range(TIMESTOCLEAN):
        solverMoves = cleanInput(solverMoves)
    #if move is orientation, add it to orientation list
    #else, convert move through every orientation, then account for inverses
    #1. for every move, convert using orientation calculations to correct motor movement
    #2. process motor movement
    #3. update orientation if needed
    orientations = []
    processedMoves = []
    moveNum = 0
    while moveNum < len(solverMoves):
        if solverMoves[moveNum] == "X":
            orientations.append("X")
        elif solverMoves[moveNum] == "Y":
            orientations.append("Y")
        elif solverMoves[moveNum] == "Z":
            orientations.append("Z")
        else:
            move = processOrientation(orientations, solverMoves[moveNum])
            processedMoves.append(move)
        moveNum += 1

    return processedMoves