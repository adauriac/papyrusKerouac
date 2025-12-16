L'image vient de:
https://www.vogue.fr/culture/a-voir/diaporama/on-the-road-le-manuscrit-original-de-kerouac-en-rsidence-paris/9034

makeFilm.py : on utilise wand pour créer les images et ffmpeg pour les monter.

utiliser wand.py l'api python de imagemagick qui crée les fichiers ordonnés des images
utiliser ffmpeg avec un fichier qui contient une ligne file'nom' suivie d'une ligne duration x

Pour faire l'intro ouvrir une image avec gimp y ajouter un calque blanc(donc bonne dim) et avec text entrer le texte avec la police manuscripte

Pour avoir des dimensions paires: magick input.jpg -resize 798x430! output.jpg (initialement 799x430)
