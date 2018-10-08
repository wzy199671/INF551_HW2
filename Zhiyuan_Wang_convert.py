from lxml import etree
import json
import sys

fileobject=open(sys.argv[1])
payload=fileobject.read()
data = json.loads(payload)
num=len(data['prizes'])
root=etree.Element('prizes')
for i in range(0,num):
    category=etree.SubElement(root, data['prizes'][i]['category'])
    for j in range(0,len(data['prizes'][i]['laureates'])):
        laureates=etree.SubElement(category, 'laurate')
        laureates.set("id", data['prizes'][i]['laureates'][j]['id'])
        laureates.set("year", data['prizes'][i]['year'])
        firstname=etree.SubElement(laureates,'firstname')
        firstname.text=data['prizes'][i]['laureates'][j]['firstname']
        surname=etree.SubElement(laureates,'surname')
        surname.text=data['prizes'][i]['laureates'][j]['surname']
        motivation=etree.SubElement(laureates,'motivation')
        if 'motivation' in data['prizes'][i]['laureates'][j]:
            motivation.text=data['prizes'][i]['laureates'][j]['motivation'][1:-1]
        share=etree.SubElement(laureates,'share')
        share.text=data['prizes'][i]['laureates'][j]['share']
tree =etree.ElementTree(root)
tree.write(sys.argv[2],pretty_print=True, encoding='utf-8')

