from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import urllib
# Create your views here.

def main(request):
    #plantilla_main = '<html>\
    #                    <body>\
    #	                    <h1>Esta aplicacion extrae los titulos de barrapunto.com</h1>\
    #                        <a href="titles">Obtener los titulos de barrapunto</a>\
    #                    </body>\
    #                  </html>'#Esto tendria que ir en main.html y usar el codigo comentado
    #return HttpResponse(plantilla_main)
    template = get_template('main.html')
    return HttpResponse(template.render())

def titles(request):
    pagecode = urllib.urlopen('http://softlibre.barrapunto.com/')
    htmlcode = pagecode.read()
    articulos = htmlcode.split('<div class="title">\n		<h3 >\n			')#Tomo los articulos por separado
    titulos = []
    enlaces = []
    for articulo in articulos[1:-1]:
        titulos.append(articulo.split('\n			\n		</h3>')[0])
        enlaces.append(articulo.split('<li class="more">\n		<a href="')[1].split('"')[0])#De cada articulo tomo su titulo y su enlace
    for i in range(len(titulos)):
        if titulos[i].find('<a href="') != -1:
            titulos[i] = titulos[i].split('</a>: ')[1]#A veces los titulos vienen con enlaces a otros sitios. Me quedo solo con el titulo
    respuesta = '<h1>Lista de titulares de barrapunto:</h1>'
    for i in range(len(titulos)):
        respuesta += '<p><a href="' + enlaces[i] + '">' + titulos[i] + '</a></p>'
    return HttpResponse(respuesta)
