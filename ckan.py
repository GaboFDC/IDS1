#!/usr/bin/env python

# Importamos la API para conexiones con ckan
from ckanapi import RemoteCKAN


# Creamos la conexión con datahub 
datahub = RemoteCKAN('https://datahub.io')

# Creamos la conexión con publicdata  
publicdata = RemoteCKAN('http://publicdata.eu')

# Usamos la api para buscar todos los datasets con formato sparql
raw_result = datahub.action.package_search(fq='res_format:api/sparql')

# Imprimimos los resultados en bruto
print(raw_result)

# Imprimimos el titulo de cada uno de los resultados
for res in raw_result['results']:
    print res['title']
