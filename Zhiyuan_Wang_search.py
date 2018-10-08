from lxml import etree
import sys

string=sys.argv[2].split()
index=etree.parse(sys.argv[1])
root=index.getroot()
list=[]
for stt in string:
    for element in root.iter('entry'):
        if stt == element.find('keyword').text:
            for x in element.find('ids').findall('id'):
                if x.text not in list:
                    list.append(x.text)

print(list)
