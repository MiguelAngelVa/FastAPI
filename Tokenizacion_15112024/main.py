# Practica NLTK Analisis de Frecuencia de Palabras

import nltk
from nltk.corpus import stopwords #Eliminar los conectores
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from collections import Counter #Caulcula la frecuencia

#Freqndis: Estructura de datos de NLTK que muestra cuantas veces aparece una palabra en un texto.

texto = """Devonian reefs of north-western Gondwana represent the southernmost record of shallow-water coral reefs in the Palaeozoic. However, few studies have attempted to date palaeoecological reconstructions of these high-latitude reefal buildups. This study provides the first detailed palaeoecological analysis of Aferdou el Mrakib, an isolated, Givetian coral-stromatoporoid reef, which developed in a semirestricted basin in the south-eastern part of the Rheic Ocean. The study documents spatial facies variability and succession of faunal replacements accompanying progressive reef accretion towards the sea surface. The investigations included both autochthonous communities found at the base of the reef and, partially, within the reef core, and allochthonous deposits of reef-derived skeletal debris that accumulated in the fore-reef setting. Contrary to some previous suggestions, the study shows that the Aferdou reef shared many characteristics of classical Middle Devonian coral-stromatoporoid buildups, including the ecological succession, limited role of calcareous algae, and development within the range of the euphotic zone, but likely below the zone of regular water agitation. Critical factors in the facies development and temporal changes in the character of reef building were the palaeobathymetry, dominant sedimentary and circulation regimes, level of wave energy, and, possibly, light availability. Distinctive features of the palaeoecology of Aferdou el Mrakib are the dominance of massive colonies of heliolitid tabulates and a subordinate role of massive stromatoporoids, both explained here primarily as a result of increased water turbidity in the high-latitude sedimentary basin. The growth of the high-latitude coral-stromatoporoid reefs in the south-eastern Rheic Ocean was favoured by a combination of the exceptionally warm climate and plate tectonic configuration typifying the Devonian. Of critical importance appears the palaeogeographic position of the Rheic, which resulted in the seawater circulation in the ocean being dominated by tropical water masses, with restricted inflow of cold water from the circumpolar oceanic circulation."""

#Tokenizamos el texto
palabras = word_tokenize(texto, language='spanish')
print(palabras)

# Stopwords:Elimina los conectores

stop_words = set(stopwords.words('spanish'))

#Filtramos las palaras que estan en la lista de stopwords
palabras_filtradas = [palabra for palabra in palabras if 
                      palabra.lower() not in stop_words and palabra.isalpha()]

print(palabras_filtradas)   #Lista de palabras filtradas

frecuencia_palabras = FreqDist(palabras_filtradas)

print(frecuencia_palabras.most_common(3))