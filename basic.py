#Tokenizer
cint="INT"
cfloat="FLOAT"
cplus="PLUS"
cminus="MINUS"
cmul="MUL"
cdiv="DIV"
clparen="LPAREN"
crparen="RPAREN"
class token:
    def __init__(self,type_,value):
        self.type=type_
        self.value=value
    def __repr__(self):
        if self.value:
            return f'{self.type}:{self.value}'
        return f'{self.type}'
#lEXER
class lexer:
    def __init__(self,text):
        self.text=text
        