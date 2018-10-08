from lxml import etree
import sys
prize=etree.parse(sys.argv[1])

root=prize.getroot()

index=etree.Element('index')

di=dict()
for element in root.iter('laurate'):
    if(element.find('motivation').text):
        for stri in element.find('motivation').text.split():
            s=filter(str.isalnum,stri)
            if s:
                if di.__contains__(s):
                    if element.attrib['id'] not in di[s]:
                     di[s].append(element.attrib['id'])
                else:
                    di[s] = []
                    di[s].append(element.attrib['id'])
for stri in di:
    entry = etree.SubElement(index, 'entry')
    keyword = etree.SubElement(entry, 'keyword')
    keyword.text = filter(str.isalnum,stri).lower()
    ids = etree.SubElement(entry, 'ids')
    for snum in di[stri]:
        id=etree.SubElement(ids,'id')
        id.text=snum

tree =etree.ElementTree(index)
tree.write(sys.argv[2],pretty_print=True, encoding='utf-8')



