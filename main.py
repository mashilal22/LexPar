from lexer import Lexer
from parsr import Parser
from evaluator import Evaluator

def main():
    filename = 'hilal.txt'
    file     = open(filename,'r')
    lexer    = Lexer(file)
    parsr    = Parser(lexer.tokens)

    lexer.tokenizer()
    print ("TOKENS:")
    print (lexer.tokens, "\n")

    parsr.build_AST()
    print ("AST:")
    print (parsr.AST, "\n")

    evaluator = Evaluator(parsr.AST)
    print ("OUTPUT:")
    evaluator.run(parsr.AST)

if __name__ == "__main__":
    main()
