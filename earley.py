#Constantes
T_ID = 116
T_FLOAT =101
T_INTEGER =102
T_OTHERS = 500
T_IF =103
T_THEN =104
T_BEGIN =105
T_END =106
T_PROCEDURE =107
T_FUNCTION =108
T_WHILE= 109
T_DO =110
T_BOPERATOR =111
T_LPARENT =112
T_RPARENT =113
T_ENDINSTRUCTION = 114	
T_RESULT =115
T_NREC =117
T_ATRIB =118
T_COMP =119
T_TYDESIG =120
T_OR =121
T_AND =122
T_TYPE =123
T_VAR = 124

#le o arquivo que possui os valores para a fita
arquivo = open('fita.in','r') 

#constroi a fita
fita = arquivo.readlines()

#Conjunto D
d = []

#Gramatica definida para o reconhecimento da linguagem
producoes = [
	["P","S"],#0

	["S","DEC","S"],#1
	["S","ATRIB","S"],#2
	["S","PROC","S"],#3
	["S","IF","S"],#4
	["S","WHILE","S"],#5
	["S","FUNC","S"],#6
	["S","DEC"],#7
	["S","ATRIB"],#8
	["S","PROC"],#9
	["S","IF"],#10
	["S","WHILE"],#11
	["S","FUNC"],#12


	["DEC",T_ID , T_TYDESIG , T_TYPE , T_ENDINSTRUCTION , "DEC"],#13
	["DEC",T_ID , T_TYDESIG , T_TYPE , T_ENDINSTRUCTION ],#14

	["DECPF",T_ID , T_TYDESIG , T_TYPE , "DECPF"],#15
	["DECPF",T_ENDINSTRUCTION,"DECPF"],#16
	["DECPF",T_ID , T_TYDESIG , T_TYPE ],#17
	["DECPF",T_ENDINSTRUCTION],#18

	["ATRIB",T_ID,T_ATRIB,"VALORES",T_ENDINSTRUCTION,"ATRIB"],#19
	["ATRIB",T_ID,T_ATRIB,"VALORES",T_ENDINSTRUCTION],#20

	["VALORES",T_ID],#21
	["VALORES",T_INTEGER],#22
	["VALORES",T_FLOAT],#23
	["VALORES","OPERACAO"],#24
	["VALORES","PARENT"],#25

	["OPERACAO","VALORES",T_BOPERATOR,"VALORES"],#26

	["PARENT",T_LPARENT,"VALORES",T_RPARENT],#27

	["COND","VALORES",T_COMP,"VALORES","LOGICA"],#28
	["COND","VALORES",T_COMP,"VALORES"],#29
	["COND","VALORES","LOGICA"],#30
	["COND","VALORES"],#31
	["COND","VALORES",T_COMP,"VALORES"],#32
	["COND","VALORES"],#33

	["L",T_AND],#34
	["L",T_OR],#35

	["LOGICA","L","COND"],#36

	["BEGEND",T_BEGIN,"S", T_END, T_ENDINSTRUCTION],#37
	["BEGENDRES", T_BEGIN, "S", T_RESULT, T_ATRIB ,"VALORES", T_ENDINSTRUCTION, T_END,T_ENDINSTRUCTION],#38
	["BEGEND",T_BEGIN, T_END, T_ENDINSTRUCTION],#39
	["BEGENDRES", T_BEGIN, T_RESULT, T_ATRIB ,"VALORES", T_ENDINSTRUCTION, T_END,T_ENDINSTRUCTION],#40

	["VAR",T_VAR,"DEC"],#41
	["VAR",T_VAR],#42

	["IF", T_IF, "COND", T_THEN, "BEGEND"],#43
	
	["WHILE", T_WHILE, "COND", T_DO, "BEGEND"],#44

	["PROC", T_PROCEDURE, T_ID, T_LPARENT, "DECPF", T_RPARENT,T_ENDINSTRUCTION,"VAR","BEGEND"],#45
	["PROC", T_PROCEDURE, T_ID, T_LPARENT, "DECPF", T_RPARENT,T_ENDINSTRUCTION,"BEGEND"],#46
	["PROC", T_PROCEDURE, T_ID, T_LPARENT, T_RPARENT,T_ENDINSTRUCTION,"VAR","BEGEND"],#47
	["PROC", T_PROCEDURE, T_ID, T_LPARENT, T_RPARENT,T_ENDINSTRUCTION,"BEGEND"],#48

	["FUNC",T_FUNCTION,T_ID,T_LPARENT,"DECPF",T_RPARENT,T_TYDESIG,T_TYPE,T_ENDINSTRUCTION,"BEGENDRES"],#49
	["FUNC",T_FUNCTION,T_ID,T_LPARENT,T_RPARENT,T_TYDESIG,T_TYPE,T_ENDINSTRUCTION,"BEGENDRES"]#50
]


#Cosntrução de D0
d.append(list())
for i in producoes:
	if i[0]=="P":
		d[0].append(list(i))
		d[0][len(d[0])-1].insert(1,".")
		d[0][len(d[0])-1].append("/0")
qtdAnt = len(d[0])


while True:
	for i in d[0]:
		for j in producoes:
			if j[0] == i[2]:
				copy = list(j)
				copy.insert(1,".")
				copy.append("/0")
				if copy not in d[0]:
					d[0].append(copy)

	if qtdAnt == len(d[0]):
		break;
	else:
		qtdAnt = len(d[0])
#Finaliza construção de D0

w = len(fita)-1#Tamanho da palavra a ser reconhecida

#Construção dos demais conjuntos D
for r in range(1,w+1):
	d.append(list())
	ar = fita.pop(0)
	for i in d[r-1]:
		iPonto = i.index(".")
		if i[iPonto+1] == int(ar):
			copy = list(i)
			copy.insert((iPonto+2),".")
			copy.pop(iPonto)
			if copy not in d[r]:
				d[r].append(copy)
	qtdAnt = len(d[len(d)-1])

	while True:
		for i in d[r]:
			iPonto = i.index(".")
			for j in producoes:
				if i[iPonto+1] == j[0]:
					copy = list(j)
					copy.insert(1,".")
					copy.append("/"+str(r))
					if copy not in d[r]:
						d[r].append(copy)
		for i in d[r]:
			iPonto = i.index(".")
			afterPonto = str(i[iPonto+1])
			if afterPonto[0] == "/":
				A = i[0]
				s = int(afterPonto[1:])
				for j in d[s]:
					iPontoo = j.index(".")
					afterPontoo = j[iPontoo+1]
					if afterPontoo == A:
						copy = list(j)
						copy.insert((iPontoo+2),".")
						copy.pop(iPontoo)
						if copy	not in d[r]:
							d[r].append(copy)
		
		if qtdAnt == len(d[r]):
			break;
		else:
			qtdAnt = len(d[r])	
#Finaliza construção do conjunto D

#Imprime cada Conjunto E D	
index = 0
for i in d:
	print("D"+str(index)+":")
	for j in i:
		print(j)
	index+=1
#Finaliza a impressão

#Verifica se a palavra é aceita
for i in d[w]:
	iPonto = i.index(".")
	if(i[iPonto+1] == "/0" and i[0] == "P"):
		print("Palavra aceita!")
		break
#fim da verificação