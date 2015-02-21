import webapp
import random


class Aleatorio(webapp.webApp):

	def process(self, parsedRequest):
		aleatorio = str(random.randrange(100000000))
		return ("HTTP/1.1 200 OK\r\n\r\n" +
                         "<html>" +
                         "<body><h1>Pagina para pedir una nueva pagina aleatoria</h1>" +
                         "<p>Hola, <a href='" + aleatorio + "'>Dame otra</a></p>" +                        
                         "</body></html>" +
                         "\r\n")

if __name__ == "__main__": 
	serv = Aleatorio("localhost", 1234) 
