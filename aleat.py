import webapp
import random


class aleatorio(webapp.webApp):
  def process(self, parsedRequest):
    aleatorio = str(random.randrange(100000000))
    return ("200 OK","<html>" +
                         "<body><h1>Pagina para pedir una nueva pagina aleatoria</h1>" +
                         "<p>Hola, <a href='" + aleatorio + "'>Dame otra</a></p>" +                        
                         "</body></html>" +
                         "\r\n")

if __name__ == "__main__": 
  serv = aleatorio("localhost", 1234) 
