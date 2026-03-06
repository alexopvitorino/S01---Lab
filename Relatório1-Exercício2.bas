DIM senha AS INTEGER
DIM tentativa AS INTEGER

senha = 7788
tentativa = 0

WHILE tentativa <> senha
    INPUT "Digite a senha: ", tentativa
    
    IF tentativa <> senha THEN
        PRINT "Senha incorreta. Tente novamente."
    END IF
WEND

PRINT "Acesso liberado!"
