L'image vient du réseau.
Pour dessiner j'ai essayer GIMP sans  succès. 
	Il y a des _scripts_-- et des _plugins_ en différents langages, dont python.
	Les scripts sont censés être plus simples.
Avec image-magick c'est beaucoup plus simple: deux méthodes:
1. utiliser des commandes construites en python: magick in.jpg -stroke red -strokewidth 5 -fill none -draw "rectangle 100,100 500,400" out.jpg voir go.py
2. utiliser l'api python de imagemagick qui est wand voir gowand.py

