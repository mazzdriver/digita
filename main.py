from modules import *


# Угадайка цифр. Тыкаем кнопку "Старт" и пытаемся отгадать число, загаданное компом.

def main():# start
	if ready_to_play():
		print(text.letsgo)
	else:
		print(text.bye)
		exit()
	# title
	while True:
		print(text.rules)
		solving = int(random.randrange(1, 10))
		guessed = False
		while not guessed:
			number = get_number()
			if number > solving:
				print(text.too_big)
				continue
			elif number < solving:
				print(text.too_small)
				continue
			else:
				print(text.bingo)
				break
		print(text.retry)
		if ready_to_play():
			pass
		else:
			print(text.goodbye)
			exit()
			
def ready_to_play():
	print(text.wanna_play)
	ready_proof = input()
	if ready_proof.lower() in 'yes':
		return True
	else:
		return False

def foolproof(number):
	"""Функция для "защиты от дурака". Принимает данные, если это цифры - возвращает True, в остальных случаях False
	"""
	if number.isdigit():
		return True
	else:
		return False
		
def get_number():
	attempt = (input(text.attempt))
	while not foolproof(attempt):
		print(text.bad_try)
		attempt = (input(text.attempt))
	return int(attempt)
		
if __name__== "__main__":
    main()
