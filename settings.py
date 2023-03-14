# Plataformas do mapa ou estrutura
# Mapas
level_map = [
'                                                                              ',
'                                                                              ',
'               X  X             X        X           X        X               ',
'XX X     XXXXXXXXXXXXXXXXX    XXXXXXX  XX X     XXXXXXXXXXXXXXXXX    XXXXXXX  ',
'XX P X X X                   X XX X X XXX   X X X                   X XX X X X',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',]

tile_size = 64 #largura do ladrilho

#configurações da tela
screen_height = 432
screen_width = 800#len(level_map) * tile_size # a largura do mapa e aumentada de acordo com o mapa

#bordas da camera
camera_borders = {
    'left': 400,
    'right': 400,
	'top':200,
	'bottom': 200
}

fps = 60 #60 fps cravado