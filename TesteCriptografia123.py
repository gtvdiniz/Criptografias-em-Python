class Arquivo_Criptografia:

    def criptografia(self):

        op = int(input("[1] - Inversão da Mensagem\n[2] - Deslocamento de Letras\n[3] - Substituição aleatória\nDigite a opção: "))
        with open("criptografando.txt", "w") as arquivo:
            arquivo.write(input("Conteúdo do arquivo: "))
        match op:

            case 1:

                with open("criptografando.txt", "r") as arquivo:
                    conteudo = arquivo.read()

                conteudo_contrario = "".join(reversed(conteudo))

                with open("criptografando.txt", "w") as arquivor:
                    arquivor.write(conteudo_contrario)

            case 2:
             #Passo 2 - Utilização da Cifra de César
                numeros = "1234567890"
                letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
                letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

                valor_deslocamento = int(input("Digite o valor de deslocamento das palavras: "))

                letrasmini_cifrados = letras_minusculas[valor_deslocamento:] + letras_minusculas[:valor_deslocamento]
                numeros_cifrados = numeros[valor_deslocamento:] + numeros[:valor_deslocamento]
                letrasmega_cifrados = letras_maiusculas[valor_deslocamento:] + letras_maiusculas[:valor_deslocamento]

                tabela_ciframento = str.maketrans(letras_minusculas + numeros + letras_maiusculas,
                                              letrasmini_cifrados + numeros_cifrados + letrasmega_cifrados)
            #-----------------------------------------------------------------------------------------------------
                with open("criptografando.txt", "r") as arquivo:
                    novamsg = arquivo.read()


                mensagem_cifrada = novamsg.translate(tabela_ciframento)

                with open("criptografando.txt", "w") as arquivo:
                    arquivo.write(mensagem_cifrada)

        #------------------------------------------------------------------------------------------------------
            case 3:
                #Passo 3 - Utilização de Cifragem Aleatória
                cifragem_aleatoria = {
                    "A": "X", "B": "M", "C": "Q", "D": "J", "E": "O", "F": "Z", "G": "P", "H": "T", "I": "L",
                    "J": "Y", "K": "S", "L": "N", "M": "B", "N": "C", "O": "D", "P": "R", "Q": "V", "R": "F",
                    "S": "K", "T": "E", "U": "G", "V": "W", "W": "A", "X": "U", "Y": "H", "Z": "I",


                    "a": "x", "b": "m", "c": "q", "d": "j", "e": "o", "f": "z", "g": "p", "h": "t", "i": "l",
                    "j": "y", "k": "s", "l": "n", "m": "b", "n": "c", "o": "d", "p": "r", "q": "v", "r": "f",
                    "s": "k", "t": "e", "u": "g", "v": "w", "w": "a", "x": "u", "y": "h", "z": "i"
                }
                if op == 3:
                 with open("criptografando.txt", "r") as arquivo:
                    novamsg2 = arquivo.read()
                arquivo.close()



                ultima_mensagem = novamsg2.translate(str.maketrans(cifragem_aleatoria))

                with open("criptografando.txt", "w") as arquivo2:
                    arquivo2.write(ultima_mensagem)
                arquivo2.close()


crip = Arquivo_Criptografia()
crip.criptografia()
