abc = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'ñ', 'Ñ', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V',
        'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z']

num = range(0, 54)

abc_to_num = dict(zip(abc, num))
num_to_abc = dict(zip(num, abc))

# texts to encrypt in test mode
text_list = ['Hello World!',
             'Ironhack kids',
             'Convocatoria oficial en el Oportiño',
             'Too cool for school',
             'Tenemos los mejores teachers de Ironhack',
             'Alea jacta est',
             'Real programmers count from zero',
             'Everything is under crtl',
             'Help me please!',
             'Tengo el mismo código y a mí no me funciona',
             'In case of fire: git commit, git push and run!',
             'Drama de ramas'
             ]

# keys for vigenere function in test mode
cipher_key = [
            'git',
            'python',
            'loop',
            'for',
            'while',
            'tuple',
            'list',
            'dict',
            'api',
            'hey',
            'ironhack',
            'bootcamp',
            'data',
            'elif',
            'else',
            'html',
            'plot',
            'code',
            'return',
            'if'
            ]