# Personagens
define e = Character("Eric")
define c = Character("[player_name]")
define m = Character("Motorista")

label start:
    stop music fadeout 1.0

    play music "audio/inlovewithaghost.mp3" volume 0.25

    scene busbackground with fade
    play sound "audio/somdeonibus.mp3" volume 0.05

    "Três coisas que eu consigo ver quando acordo."
    "uma mala no bagageiro acima da cabeça de outra pessoa que também estava no ônibus..."
    "essa mesma pessoa roncando incessantemente, o que talvez tenha sido o motivo de eu acordar..."
    "e o motorista pelo seu retrovisor quase dormindo, isso não pode ser saudável."
    "Bom, vamos começar pelo básico, então."

    python:
        player_name = renpy.input("Qual é o seu nome? Se não conseguir decidir, escolhemos um pra você,"
        " apenas aperte Enter sem digitar nada!", length=10)

        # O .strip() tira quaisquer espaços para que apenas o nome seja visível.
        player_name = player_name.strip()

        # Se o jogador não quer escolher um nome,
        # escolheremos um que seja apropriado (eu acho):
        if player_name == "":
            player_name="Ari"

    c "Meu nome é [player_name]!"

    python:
            player_age = renpy.input("Quantos anos você tem? (Escolhemos isso também caso esteja"
            " indeciso!)", allow="0123456789")

            if player_age == "":
                player_age="19"

    c "Tenho [player_age] anos e vou começar a estudar em uma faculdade na cidade de Itajubá"
    c "A cidade é conhecida por sua forte cultura de educação. Embora pequena, Itajubá tem diversos"
    c " centros de educação e não é muito difícil trombar com uma universidade lá."
    c "Agora... Eu preciso encontrar o Eric, ele é filho de uma amiga da minha mãe... ou algo assim, sei lá."
    c "Para onde devo ir?"

menu:

    "Pedir ajuda ao motorista":
        jump motorista

    "Meh, whatever happens, happens":
        jump endingFudida

stop sound fadeout 1.0
stop music fadeout 1.0

label motorista:
    scene busanime with dissolve
    
    "Você se aproxima do motorista depois de descer do ônibus, ele parece ocupado folheando algumas páginas."
    show busdriver
    c "*Limpa a garganta* Ei, com licença, você pode me dizer como eu saio daqui?"
    m "Ora! Veja só você! Deve ser uma pessoa nova por aqui, hoho!"
    "Você olha desconfortavelmente pros lados pra ver se alguém notou esse velho safado falando assim com você, aparentemente não"
    m "Bem, bem! Não precisa choramingar, estou aqui por você! Pegue a primeira à esquerda depois daquele bebedouro."

    menu:
        "Agradecer o motorista":
            jump motoristaEducado

        "Se fodase ele":
            jump motoristaGrosso

label endingFudida:
    "Bad ending 1/10 :("

    #show eric

return
