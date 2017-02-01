import pygame


def print_letter(window, letter, position, thickness, size, color):

	letters = {"A":[(position[0]+(size/8),position[1]+size),(position[0] + size/2,position[1]+0),(position[0] + (7*size/8),position[1]+size),(position[0] + (5*size/8),position[1]+(size/2)),( position[0]+(3*size/8), position[1]+size/2)],
		"B":[(position[0]+(size/8), position[1]+size), (position[0]+(size/8),position[1]),(position[0]+(size/8)+(5*size/8),position[1]),(position[0]+(size/8)+(7*size/8),position[1]+(1*size/8)),(position[0]+(size/8)+(7*size/8),position[1]+(2*size/8)),(position[0]+(size/8)+(5*size/8),position[1]+(3*size/8)),(position[0]+(size/8)+(7*size/8),position[1]+(4*size/8)),(position[0]+(size),position[1]+(7*size/8)),(position[0]+(7*size/8),position[1]+(size)),(position[0]+(size/8),position[1]+(size)) ],
		"C":[(position[0]+(7*size/8), position[1]+(2*size/8)),(position[0]+(6*size/8), position[1]),(position[0]+(3*size/8), position[1]),(position[0]+(1*size/8), position[1]+(3*size/8)),(position[0]+(size/8), position[1]+(5*size/8)),(position[0]+(3*size/8), position[1]+(size)),(position[0]+(6*size/8), position[1]+(size)),(position[0]+(7*size/8), position[1]+(6*size/8)), ],
		"D":[(position[0]+(size/8), position[1]+size), (position[0]+(size/8),position[1]), (position[0]+(5*size/8),position[1]), (position[0]+(7*size/8),position[1]+(2*size/8)), (position[0]+(7*size/8),position[1]+(6*size/8)), (position[0]+(5*size/8),position[1]+(size)),(position[0]+(size/8), position[1]+size) ],
		"E":[(position[0]+(7*size/8), position[1]), (position[0]+(size/8),position[1]), (position[0]+(size/8),position[1]+(4*size/8)), (position[0]+(6*size/8),position[1]+(4*size/8)), (position[0]+(size/8),position[1]+(4*size/8)), (position[0]+(size/8),position[1]+(size)), (position[0]+(7*size/8),position[1]+(size)) ],
		"F":[(position[0]+(7*size/8), position[1]), (position[0]+(size/8),position[1]), (position[0]+(size/8),position[1]+(4*size/8)), (position[0]+(6*size/8),position[1]+(4*size/8)), (position[0]+(size/8),position[1]+(4*size/8)), (position[0]+(size/8),position[1]+(size)) ],
		"G":[(position[0]+(7*size/8), position[1]+(2*size/8)),(position[0]+(6*size/8), position[1]),(position[0]+(3*size/8), position[1]),(position[0]+(1*size/8), position[1]+(3*size/8)),(position[0]+(size/8), position[1]+(5*size/8)),(position[0]+(3*size/8), position[1]+(size)),(position[0]+(6*size/8), position[1]+(size)),(position[0]+(7*size/8), position[1]+(6*size/8)),(position[0]+(7*size/8), position[1]+(5*size/8)),(position[0]+(5*size/8), position[1]+(5*size/8)) ],
		"O":[(position[0]+(7*size/8), position[1]+(2*size/8)),(position[0]+(6*size/8), position[1]),(position[0]+(2*size/8), position[1]),(position[0]+(1*size/8), position[1]+(2*size/8)),(position[0]+(size/8), position[1]+(6*size/8)),(position[0]+(2*size/8), position[1]+(size)),(position[0]+(6*size/8), position[1]+(size)),(position[0]+(7*size/8), position[1]+(6*size/8)), (position[0]+(7*size/8), position[1]+(2*size/8))],
		
	}
	pygame.draw.lines(window,color, False, letters[letter], thickness)

def print_text(window, text, position, thickness, size, color):
	space = size/8
	for idx, letter in enumerate(text):
		print_letter(window, letter, (position[0]+idx*(size+space),position[1]),thickness,size, color)
	