str = 'I am workinging on a projecting'

from enum import Enum

class State(Enum):
    nothing = 1
    saw_i = 2
    saw_in = 3
    saw_ing = 4
    
def rec_ing(str):
    cnt = 0
    state = State.nothing
    for i in range(len(str)):
        if state == State.nothing:
            if str[i] == 'i':
                state = State.saw_i
            else:
                state = State.nothing
        elif state == State.saw_i:
            if str[i] == 'n':
                state = State.saw_in
            else:
                state = State.nothing
        elif state == State.saw_in:
            if str[i] == 'g':
                state = State.saw_ing
                cnt = cnt + 1
            
            state = State.nothing
    return cnt
    

print(rec_ing(str))
