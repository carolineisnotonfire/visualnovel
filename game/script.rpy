# Personagens
define e = Character("Eric")
define c = Character("[player_name]")




# The game starts here.

label start:
    stop music fadeout 1.0

    scene busbackground

    play music "audio/millionmilesaway.mp3" volume 0.25
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
    #""

    #show eric

    return
