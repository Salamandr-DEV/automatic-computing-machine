from logpy import *
from logpy.core import lall

people = var()

rul = lall(
	(eq, (var(), var(), var(), var(), var()), people),
	(membero, ('Англичанин', var(), var(), var(), 'красный'), people),
	(membero, ('Швед', var(), var(), 'собака', var()), people),
	(membero, ('Датчанин', var(), 'чай', var(), var()), people),

	(membero, (var(), var(), 'кофе', var(), 'зеленый'), people),
	(membero, (var(), 'Pall Mall', var(), 'птицы', var()), people),
	(membero, (var(), 'Dunhill', var(), var(), 'желтый'), people),
	(eq, (var(), var(), (var(), var(), 'молоко', var(), var()), var(), var()), people),
	(eq, (('Норвежец', var(), var(), var(), var()), var(), var(), var(), var()), people),

	(membero, (var(), 'Winfield', 'пиво', var(), var()), people),
	(membero, ('Немец', 'Rothmans', var(), var(), var()), people),

	(membero, (var(), var(), var(), 'рыбки', var()))
)

solution = run(0, people, rul)

for item in solution[0]:
	print(item)


