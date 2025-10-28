str = 'I am workinging on a projecting aaaa'

from enum import Enum

class State(Enum):
    begin = 1
    saw_a = 2
    saw_aa = 3

    
def rec_aa(str):
    cnt = 0
    state = State.begin
    for i in range(len(str)):
        if state == State.begin:
            if str[i] == 'a':
                state = State.saw_a
            else:
                state = State.begin
        elif state == State.saw_a:
            if str[i] == 'a':
                state = State.saw_aa
                cnt = cnt + 1

            state = State.begin

    return cnt
    

print(rec_aa(str))
