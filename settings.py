# Plataformas do mapa ou estrutura
# Mapas
level_map = [
'      X                                ',
'     X                                 ',
'    X                                  ',
'XX X     XXXXXXXXXXXXXXXXX    XXXXXXX  ',
'XX   X X X                   X XX X X X',
'XXX                   X    X     X X X ',
'XXXP         X  X     XX        X X X ',
'XXXX       X     X       XXXXXXX       ',
'XXXX XXXX        X      X  XXXXX       ',
'XXXX     XXXX    X     X   XXXXX       ',
'XXXX           X X    X    XXXXX       ',
'XXXX         X   X   X     XXXXX       ',
'XXXX      X      X  X      XXXXX       ',
'XXXXXXXXXXXXXXXXXXXX                   ',]

tile_size = 64 #largura do ladrilho

#configurações da tela
screen_height = 720
screen_width = len(level_map) * tile_size # a largura do mapa e aumentada de acordo com o mapa

#bordas da camera
CAMERA_BORDERS = {
    'left': 400,
    'right': 400,
	'top':400,
	'bottom': 400
}