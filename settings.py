# Plataformas do mapa ou estrutura
# Mapas
level_map = [
'      X                                                                       ',
'     X                                                                        ',
'    X                                                                         ',
'XX X     XXXXXXXXXXXXXXXXX    XXXXXXX  XX X     XXXXXXXXXXXXXXXXX    XXXXXXX  ',
'XX   X X X                   X XX X X XXX   X X X                   X XX X X X',
'XXX                   X    X     X X X XXX                   X    X     X X X ',
'XXXP         X  X     XX        X X X XXX          X  X     XX        X X X   ',
'XXXX       X     X       XXXXXXX       XXXX       X     X       XXXXXXX       ',
'XXXX XXXX        X      X  XXXXX       XXXX XXXX        X      X  XXXXX       ',
'XXXX     XXXX    X     X   XXXXX       XXXX     XXXX    X     X   XXXXX       ',
'XXXX           X X    X    XXXXX       XXXX           X X    X    XXXXX       ',
'XXXX         X   X   X     XXXXX       XXXX         X   X   X     XXXXX       ',
'XXXX      X      X  X      XXXXX       XXXX      X      X  X      XXXXX       ',
'XXXXXXXXXXXXXXXXXXXX                   XXXXXXXXXXXXXXXXXXXX                   ',]

tile_size = 64 #largura do ladrilho

#configurações da tela
screen_height = 720
screen_width = 1000#len(level_map) * tile_size # a largura do mapa e aumentada de acordo com o mapa

#bordas da camera
camera_borders = {
    'left': 400,
    'right': 400,
	'top':200,
	'bottom': 200
}