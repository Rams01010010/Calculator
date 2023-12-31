#!/usr/bin/python3
from nodes import *
from tokens import TokenType

class Parser:

    def __init__(self,tokens):
        self.tokens = iter(tokens)
        self.advance()
    
    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None
    
    def parse(self):
        if self.current_token == None:
            return None
        
        result = self.expr()

        if self.current_token != None:
            raise Exception("Invalid Syntax")

        return result
    
    def expr(self):
        result = self.term()
        while self.current_token != None and self.current_token.type in (TokenType.PLUS , TokenType.MINUS):
            if self.current_token.type == TokenType.PLUS:
                self.advance()
                result = AddNode(result, self.term())
            elif self.current_token.type == TokenType.MINUS:
                self.advance()
                result = SubNode(result,self.term())
        
        return result


    def term(self):
        result = self.factor()
        while self.current_token != None and self.current_token.type in (TokenType.MULTIPLY , TokenType.DIVIDE):
            if self.current_token.type == TokenType.MULTIPLY:
                self.advance()
                result = MultiplyNode(result, self.factor())
            elif self.current_token.type == TokenType.DIVIDE:
                self.advance()
                result = DivideNode(result,self.factor())
        
        return result

    def factor(self):
        token = self.current_token
        self.advance()

        if token.type == TokenType.LPAREN:
            result = self.expr()
            if self.current_token.type != TokenType.RPAREN:
                raise Exception("Invalid Syntax")
            self.advance()
            return result
        elif token.type == TokenType.NUMBER:
            return NumberNode(token.value)
        elif token.type == TokenType.PLUS:
            return PlusNode(self.factor())
        elif token.type == TokenType.MINUS:
            return MinusNode(self.factor())
        

