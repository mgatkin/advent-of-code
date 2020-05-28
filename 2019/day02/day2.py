'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

raw_data = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,5,19,23,2,6,23,27,1,27,5,31,2,9,31,35,1,5,35,39,2,6,39,43,2,6,43,47,1,5,47,51,2,9,51,55,1,5,55,59,1,10,59,63,1,63,6,67,1,9,67,71,1,71,6,75,1,75,13,79,2,79,13,83,2,9,83,87,1,87,5,91,1,9,91,95,2,10,95,99,1,5,99,103,1,103,9,107,1,13,107,111,2,111,10,115,1,115,5,119,2,13,119,123,1,9,123,127,1,5,127,131,2,131,6,135,1,135,5,139,1,139,6,143,1,143,6,147,1,2,147,151,1,151,5,0,99,2,14,0,0]

def intcode(noun, verb, raw_data):
    data = raw_data[:]
    data[1] = noun
    data[2] = verb
    for i in range(int(len(data) / 4)):
        opcode = data[i * 4]
        arg1_position = i * 4 + 1
        arg2_position = i * 4 + 2
        result_position = data[i * 4 + 3]
        arg1 = data[arg1_position]
        arg2 = data[arg2_position]
        data1 = data[arg1]
        data2 = data[arg2]
        if opcode == 1:
            data[result_position] = data1 + data2
        elif opcode == 2:
            data[result_position] = data1 * data2
        elif opcode == 99:
            break
        else:
            print('Invalid opcode')
            break
        
    return data

def solve():
    for noun in range(100):
        for verb in range(100):
            if intcode(noun, verb, raw_data)[0] == 19690720:
                return(noun, verb)

print(intcode(12, 2, raw_data)[0])

noun, verb = solve()
print(noun * 100 + verb)