#!/usr/bin/python3
from tokens import *

WHITESPACE = ' \n\t'
DIGITS = '0123456789'

class Lexer:
    def __init__(self,text):
        self.text = iter(text)
        self.advance()
    
    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None


    def generateTokens(self):
        while self.current_char != None:
            if self.current_char in WHITESPACE:
                self.advance()
            elif self.current_char in DIGITS or self.current_char == '.':
                yield self.generateNumber()
            elif self.current_char == '+':
                yield Token(TokenType.PLUS)
                self.advance()
            elif self.current_char == '-':
                yield Token(TokenType.MINUS)
                self.advance()
            elif self.current_char == '*':
                yield Token(TokenType.MULTIPLY)
                self.advance()
            elif self.current_char == '/':
                yield Token(TokenType.DIVIDE)
                self.advance()
            elif self.current_char == ')':
                yield Token(TokenType.RPAREN)
                self.advance()
            elif self.current_char == '(':
                yield Token(TokenType.LPAREN)
                self.advance()
            else:
                raise Exception(f"IllegalCharacter: '{self.current_char}'")


    
    def generateNumber(self):
        decimal_point_count = 0
        num_str = ''
        while self.current_char != None and (self.current_char == '.' or self.current_char in DIGITS):
            if self.current_char == '.':
                decimal_point_count += 1
                if decimal_point_count > 1:
                    break
            
            num_str += self.current_char
            self.advance()
        
        if num_str.startswith('.'):
            num_str = '0' + num_str
        if num_str.endswith('.'):
            num_str = num_str + '0'
        
        return Token(TokenType.NUMBER,float(num_str))
