#!/usr/bin/env python

from ckanapi import RemoteCKAN

datahub = RemoteCKAN('https://datahub.io')
publicdata = RemoteCKAN('http://publicdata.eu')

raw_result = datahub.action.package_search(fq='res_format:api/sparql')

print(raw_result)

print(len(raw_result['results']))
for res in raw_result['results']:
    print res['title']