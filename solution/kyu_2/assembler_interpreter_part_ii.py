"""
Assembler interpreter (part II)
https://www.codewars.com/kata/assembler-interpreter-part-ii/
"""
"""
This is the second part of this kata series. First part is here.

We want to create an interpreter of assembler which will support the following instructions:

    mov x, y - copy y (either an integer or the value of a register) into register x.
    inc x - increase the content of register x by one.
    dec x - decrease the content of register x by one.
    add x, y - add the content of the register x with y (either an integer or the value of a register) and stores the result in x (i.e. register[x] += y).
    sub x, y - subtract y (either an integer or the value of a register) from the register x and stores the result in x (i.e. register[x] -= y).
    mul x, y - same with multiply (i.e. register[x] *= y).
    div x, y - same with integer division (i.e. register[x] /= y).
    label: - define a label position (label = identifier + ":", an identifier being a string that does not match any other command). Jump commands and call are aimed to these labels positions in the program.
    jmp lbl - jumps to the label lbl.
    cmp x, y - compares x (either an integer or the value of a register) and y (either an integer or the value of a register). The result is used in the conditional jumps (jne, je, jge, jg, jle and jl)
    jne lbl - jump to the label lbl if the values of the previous cmp command were not equal.
    je lbl - jump to the label lbl if the values of the previous cmp command were equal.
    jge lbl - jump to the label lbl if x was greater or equal than y in the previous cmp command.
    jg lbl - jump to the label lbl if x was greater than y in the previous cmp command.
    jle lbl - jump to the label lbl if x was less or equal than y in the previous cmp command.
    jl lbl - jump to the label lbl if x was less than y in the previous cmp command.
    call lbl - call to the subroutine identified by lbl. When a ret is found in a subroutine, the instruction pointer should return to the instruction next to this call command.
    ret - when a ret is found in a subroutine, the instruction pointer should return to the instruction that called the current function.
    msg 'Register: ', x - this instruction stores the output of the program. It may contain text strings (delimited by single quotes) and registers. The number of arguments isn't limited and will vary, depending on the program.
    end - this instruction indicates that the program ends correctly, so the stored output is returned (if the program terminates without this instruction it should return the default output: see below).
    ; comment - comments should not be taken in consideration during the execution of the program.


Output format:

The normal output format is a string (returned with the end command). For Scala and Rust programming languages it should be incapsulated into Option.

If the program does finish itself without using an end instruction, the default return value is:

-1 (as an integer)


Input format:

The function/method will take as input a multiline string of instructions, delimited with EOL characters. Please, note that the instructions may also have indentation for readability purposes.

For example:

program = 
; My first program
mov  a, 5
inc  a
call function
msg  '(5+1)/2 = ', a    ; output message
end

function:
    div  a, 2
    ret

assembler_interpreter(program)

The above code would set register a to 5, increase its value by 1, calls the subroutine function, divide its value by 2, returns to the first call instruction, prepares the output of the program and then returns it with the end instruction. In this case, the output would be (5+1)/2 = 3.
"""

import re


class AsmInterpreter:
    def __init__(self, program: str):
        self.regs = {}
        self.labels = {}
        self.code = self.pre_parse(program)
        self.ptr = 0
        self.compare_result = None
        self.calls_stack = []
        self.stdout = []
        self.result = -1

    def pre_parse(self, program: str) -> list[str | int]:
        # tokenize
        code_parsed = []
        for line in program.splitlines():
            line = line.strip()  # clear leading and trailing spaces
            line_parsed = []
            mode = 'plain'  # plain mode - look for any delimiter
            element_start = 0
            for i, ch in enumerate(line):
                if ch not in " ,';":  # NOT any kind of delimiter (space, comma, single quote, semicolon)
                    continue  # ordinary character, go to next one
                # delimiter encountered, save current element and
                if mode == 'plain':
                    line_parsed.append(line[element_start:i])  # save current element
                    if ch in ", ":  # plain mode delimiters (space, comma)
                        element_start = i + 1  # set new element start after current character
                    elif ch == "'":  # start of the string element
                        mode = 'string'  # string mode - look for closing "'"
                        element_start = i + 1  # set new element start at next character to omit "'"
                    elif ch == ";":  # start of the comment element
                        element_start = i  # set new element start at current character to include ";"
                        break  # no other elements are allowed after comment, so we can omit further characters parsing
                elif mode == 'string' and ch == "'":  # end of the string
                    line_parsed.append(line[element_start:i])  # save current element omitting closing "'"
                    element_start = i + 1  # set new element start after current character
                    mode = 'plain'
            line_parsed.append(line[element_start:])  # save the last element of the current line
            line_parsed = [el for el in line_parsed if el and not el.startswith(';')]  # discard empty elements and comments
            if line_parsed:
                code_parsed.append(line_parsed)  # collect non-empty lines
        # parse tokens for labels and integers
        for i_line, line in enumerate(code_parsed):
            for i_element, element in enumerate(line):
                if i_element == 0 and element.endswith(':'):  # label
                    self.labels[element] = i_line  # store label and it's line number
                elif i_element > 0:  # first element is always command or label. Other elements can be numbers
                    try:  # try to...
                        code_parsed[i_line][i_element] = int(code_parsed[i_line][i_element])  # ... convert element to integer...
                    except ValueError:  # ... or leave as is, if converting is not possible
                        pass
        return code_parsed

    def eval_argument(self, val: str | int):
        # if it's register name - return register's value. otherwise return the value (int or str) itself
        return self.regs[val] if val in self.regs else val

    @property
    def current_command(self):
        return self.code[self.ptr][0]

    @property
    def current_operands(self):
        return self.code[self.ptr][1:]

    def mov(self):  # mov x, y - copy y (either an integer or the value of a register) into register x.
        self.regs[self.current_operands[0]] = self.eval_argument(self.current_operands[1])

    def inc(self):  # inc x - increase the content of register x by one.
        self.regs[self.current_operands[0]] += 1

    def dec(self):  # dec x - decrease the content of register x by one.
        self.regs[self.current_operands[0]] -= 1

    def add(self):  # add x, y - add the content of the register x with y (either an integer or the value of a register) and stores the result in x (i.e. register[x] += y).
        self.regs[self.current_operands[0]] += self.eval_argument(self.current_operands[1])

    def sub(self):  # sub x, y - subtract y (either an integer or the value of a register) from the register x and stores the result in x (i.e. register[x] -= y).
        self.regs[self.current_operands[0]] -= self.eval_argument(self.current_operands[1])

    def mul(self):  # mul x, y - same with multiply (i.e. register[x] *= y).
        self.regs[self.current_operands[0]] *= self.eval_argument(self.current_operands[1])

    def div(self):  # div x, y - same with integer division (i.e. register[x] /= y).
        self.regs[self.current_operands[0]] //= self.eval_argument(self.current_operands[1])

    def jmp(self):  # jmp lbl - jumps to the label lbl.
        self.ptr = self.labels[f'{self.current_operands[0]}:']  # add ':' to match label name

    def cmp(self):  # cmp x, y - compares x (either an integer or the value of a register) and y (either an integer or the value of a register). The result is used in the conditional jumps (jne, je, jge, jg, jle and jl)
        x, y = self.eval_argument(self.current_operands[0]), self.eval_argument(self.current_operands[1])
        if x > y:
            self.compare_result = 1  # greater
        elif x < y:
            self.compare_result = -1  # less
        else:
            self.compare_result = 0  # equal

    def jne(self):  # jne lbl - jump to the label lbl if the values of the previous cmp command were not equal.
        if self.compare_result != 0: self.jmp()

    def je(self):  # je lbl - jump to the label lbl if the values of the previous cmp command were equal.
        if self.compare_result == 0: self.jmp()

    def jge(self):  # jge lbl - jump to the label lbl if x was greater or equal than y in the previous cmp command.
        if self.compare_result != -1: self.jmp()

    def jg(self):  # jg lbl - jump to the label lbl if x was greater than y in the previous cmp command.
        if self.compare_result == 1: self.jmp()

    def jle(self):  # jle lbl - jump to the label lbl if x was less or equal than y in the previous cmp command.
        if self.compare_result != 1: self.jmp()

    def jl(self):  # jl lbl - jump to the label lbl if x was less than y in the previous cmp command.
        if self.compare_result == -1: self.jmp()

    def call(self):  # call lbl - call to the subroutine identified by lbl. When a ret is found in a subroutine, the instruction pointer should return to the instruction next to this call command.
        self.calls_stack.append(self.ptr)  # store current pointer for the "return" command of the function called
        self.jmp()

    def ret(self):  # ret - when a ret is found in a subroutine, the instruction pointer should return to the instruction that called the current function.
        self.ptr = self.calls_stack.pop(-1)

    def msg(self):  # msg 'Register: ', x - this instruction stores the output of the program. It may contain text strings (delimited by single quotes) and registers. The number of arguments isn't limited and will vary, depending on the program.
        self.stdout.append(''.join([str(self.eval_argument(val)) for val in self.current_operands]))

    def end(self):  # end - this instruction indicates that the program ends correctly, so the stored output is returned (if the program terminates without this instruction it should return the default output: -1).
        self.result = '\n'.join(self.stdout)  # format program result
        self.ptr = len(self.code)  # skip all subsequent commands (if any)

    def run(self):
        while self.ptr < len(self.code):  # are there lines left?
            if not self.current_command.endswith(':'):  # current line is not label?
                getattr(self, self.current_command)()  # execute method with the name of current command
            self.ptr += 1
        return self.result


def assembler_interpreter(program: str) -> str | int:
    return AsmInterpreter(program).run()
