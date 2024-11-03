cint = "INT"
cfloat = "FLOAT"
cplus = "PLUS"
cminus = "MINUS"
cmul = "MUL"
cdiv = "DIV"
clparen = "LPAREN"
crparen = "RPAREN"

class token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value
    
    def __repr__(self):
        if self.value:
            return f'{self.type}:{self.value}'
        return f'{self.type}'

class lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.adv()
    
    def adv(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def tokenizer(self):
        tokens = []
        while self.current_char is not None:
            if self.current_char in ' \t':
                self.adv()
            elif self.current_char.isdigit():
                tokens.append(self.number())
            elif self.current_char == '+':
                tokens.append(token(cplus))
                self.adv()
            elif self.current_char == '-':
                tokens.append(token(cminus))
                self.adv()
            elif self.current_char == '*':
                tokens.append(token(cmul))
                self.adv()
            elif self.current_char == '/':
                tokens.append(token(cdiv))
                self.adv()
            elif self.current_char == '(':
                tokens.append(token(clparen))
                self.adv()
            elif self.current_char == ')':
                tokens.append(token(crparen))
                self.adv()
            else:
                raise Exception(f"Illegal character  found and will be deported to mexico hopefuly.Suspect is : '{self.current_char}'")
        
        return tokens

    def number(self):
        num_str = ''
        dot_count = 0
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
            if self.current_char == '.':
                if dot_count == 1:
                    break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.adv()
        
        if dot_count == 0:
            return token(cint, int(num_str))
        return token(cfloat, float(num_str))
