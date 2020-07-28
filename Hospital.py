n = input("¿Cúal es su nombre?: ")
e = int(input("¿Cúal es su edad?: "))
x = input("¿Cúal es su sexo?: ")
m = int(input("¿Cúal es su matrícula?: "))
a = input("¿Cúal es su afiliación?: ")
s = input("¿Que sintoma presenta?: ")
if s == "obesidad":
	a = input("Tiene algún otro sintoma: ")
	if a == "si":
		b = input("¿Que sintoma es?: ")
	elif b == "vomito":
		print("Puede pasar")
	elif b == "obesidad":
		print("Puede pasar")
	elif b == "infarto":
		print("Puede pasar")
	elif a == "no":
		print("Puede pasar")
elif s == "infarto":
	print("Por favor vaya a casa") 
elif s == "fiebre":
	t = float(input("¿Cual es su temperatura?: "))
	if t <=37.5:
		print("Puede pasar")  
	elif t >=37.6: 
		print("Espere un momento")
		p = input("Tiene algún otro sintoma: ")
		if p == "si":
			c = input("¿Que sintoma es?: ")
			if c == "vomito":
				print("Por favor vaya a casa")
			elif c == "obesidad":
				print("Puede pasar")
			elif c == "infarto":
				print("Por favor vaya a casa")
		elif p == "no":
			print("Puede pasar")
elif s == "vomito":
	d = input("Tiene algún otro sintoma: ")
	if d == "si":
		v = input("¿Que sintoma es?: ")
		if v == "fiebre":
			print("¿Cúal es su temperatura?")
			i = float(input("Tiene temperatura normal"))
			if i <=37.5:
				print("Puede pasar")  
			elif i >=38: 
				print("Por favor vaya a casa")
		elif v == "obesidad":
			print("Puede pasar")
		elif v == "infarto":
			print("Puede pasar")
elif s == "ninguna":
	print("Puede pasar")
print('Registro exitoso')
print("Gracias, eso es todo por el momento")
print('------------------------')
print( n, e, x, m, a, s)


	
