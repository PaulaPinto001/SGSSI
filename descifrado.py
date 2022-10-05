import sys

#prueba
# Funcion que dada una lista de caracteres devuelve un diccionario con pares caracter-frecuencia
def frecuenciasDic(lista):
    frecuencias = [lista.count(c) for c in lista]
    return dict(list(zip(lista,frecuencias)))
    
    
#Funcion que ordena el diccionario en orden de frecuencia descendente
def ordenaDicDesc(dic):
    aux = [(dic[i], i) for i in dic]
    aux.sort()
    aux.reverse()
    return aux
    

#Funcion que devuelve el mensaje que se le pasa cambiando el caracter indicado por otro.
def cambiarLetra(mensaje,letraFalsa,letraNueva):
	mensajeNuevo=mensaje.replace(letraFalsa,letraNueva)
	return mensajeNuevo


# 1) Separar el mensaje por caracteres
mensajeO = 'RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE'
lista = []

for letra in mensajeO:
	if letra != ' ' and letra != '.' and letra != ',':
		lista.append(letra)



# 2) Obtener frecuencia de cada caracter
frecuencias=frecuenciasDic(lista)

# 3) Ordenar caracteres descendentemente por frecuencia
frecuenciasOrd=ordenaDicDesc(frecuencias)

print('##############################    Frecuencias   #################################')

print(str(frecuenciasOrd))

# 4) Reemplazar en el mensaje original las 3 letras de mayor frecuencia por la e, la a y la o
sospecha=input('\n Introduce la primera letra de la lista anterior (con mayor frecuencia)')
mensajeNuevo=cambiarLetra(mensajeO,sospecha,'e')

sospecha=input('\n Introduce la segunda letra de la lista anterior')
mensajeNuevo=cambiarLetra(mensajeNuevo,sospecha,'a')

sospecha=input('\n Introduce la tercera letra de la lista anterior')
mensajeNuevo=cambiarLetra(mensajeNuevo,sospecha,'o')
print(mensajeNuevo)

# 5) Seguir cambiando letras hasta que se descifre el mensaje completo
cont='Y'
while cont=='Y':
	print("\n ¿Seguir intercambiando letras?")
	cont=input('Escribe Y si quieres cambiar alguna letra o N si ya has acabado: ')
	if cont=='Y':
		letraFalsa=input('\n Introduce la letra que quieres cambiar: ')
		posibleLetra=input('\n Introduce la letra por la que quieres cambiar la ' + letraFalsa + ' (en minuscula): ')
		mensajeNuevo=cambiarLetra(mensajeNuevo,letraFalsa,posibleLetra)
		print(mensajeNuevo)
	elif cont=='N':
		sys.exit();
	else: cont=input('\n Escribe Y si quieres cambiar alguna letra o N si ya has acabado: ')



