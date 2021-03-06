# s2 commands
PRINT_TIM      =  0b00000001
HALT           =  0b00000010
PRINT_NUM      =  0b01000011  # command 3
SAVE           =  0b10000100
PRINT_REGISTER =  0b01000101
ADD            =  0b10000110  # command 6


# ADD

# Rules of our game
## we store everything in memory
## we move our PC to step through memory, and execute commands

# s1 memory holds numbers, example of loading programs in memory
memory = [
    PRINT_TIM,  
    PRINT_TIM,
    PRINT_NUM,
    99,
    SAVE, 
    42,  # number to save
    2,   # register to save into
    SAVE,
    42,  # number to save
    3,   # into R3
    ADD, # registers[2] = registers[2] + registers[3]  # <--- PC
    2,   # Register index
    3,   # also index
    PRINT_REGISTER,
    2,
    HALT,      
          ]

# s3
running = True
# create pointer | program counter
pc = 0 # 1 | 2

# Memory bus
## a bunch of wires that the CPU uses to send an address to RAM
## also a data bus: CPU sends data to RAM, RAM sends data to CPU
##     CPU
##  ||||||||
##  ||||||||
##  ||||||||
##     RAM

# 0b00000001
# 0b00000010
# 0b11111111


# save the number 42 into R2
# what arguments does SAVE require?

# registers (use as variables)
# R0-R7
registers = [None] * 8
# s4 while loop condition
while running:

    command = memory[pc]# memory[0] => command value is 1

    num_operands = command >> 6

    if command == PRINT_TIM:
        print("Tim!")

        # pc += 1
    
    if command == PRINT_NUM:
        number_to_print = memory[pc + 1]
        print(number_to_print)

        # pc += 2

    if command == SAVE:
        num = memory[pc + 1]
        index = memory[pc + 2]
        registers[index] = num

        # pc += 3

    if command == PRINT_REGISTER:
        reg_idx = memory[pc + 1]
        print(registers[reg_idx])

        # pc += 2

    if command == ADD:
        first_reg_idx = memory[pc + 1]
        second_reg_idx = memory[pc + 2]

        registers[first_reg_idx] += registers[second_reg_idx]

    if command == HALT:
        running = False

    # what if we set the pc directly?
    pc += num_operands + 1