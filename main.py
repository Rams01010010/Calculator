#!/usr/bin/python3
from lexer import Lexer
from parser_ import Parser
from interpretor import Interpretor

while True:
    text = input("calc > ")
    if(text == 'q'):
        break
    try:
        lexer = Lexer(text)
        tokens = lexer.generateTokens()
        parser = Parser(tokens)
        tree = parser.parse()
        if not tree: continue
        interpretor = Interpretor()
        result = interpretor.visit(tree)
        print(result)
    except Exception as e:
        print(e)
    
