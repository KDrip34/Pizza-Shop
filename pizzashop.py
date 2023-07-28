rompt = "\nPlease tell me how you like your pizza dont worry pineapples are welcome no judgement here:"
prompt += "\n(Enter 'that will be all' when you are finished picking out your toppings.)"
while True:
	pizzatop = input(prompt)
	if pizzatop == 'that will be all':
		break
	else:
			print("The pizza topping I would like to add would be " + pizzatop.title() + "!")
