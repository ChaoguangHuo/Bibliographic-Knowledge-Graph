#--*-- coding:utf-8 --*--
import sys
reload(sys) 
sys.setdefaultencoding('utf8')
import numpy as np
import csv
import xml.etree.cElementTree as ET

#######################################################
tree=ET.parse("C:/Python27/PMC_data/example/pmc_2000.xml")
csvfile=open('C:/Python27/PMC_data/example/pmc_2000.csv','wb')



writer=csv.writer(csvfile)
writer.writerow(['x','pmc','pmid','author_name','author_aff'])

root=tree.getroot()
for article in root.iter('article'):
    pmid=0
    pmc=0
    x=0
    af_name={}
    afname=[]
    author_name=0
    author_aff=[]
    for front in article.iterfind('front'):
        for a_meta in front.iterfind('article-meta'):
            for a_id in a_meta.iter('article-id'):############paper ID
                if a_id.get('pub-id-type')=='pmid':
                    pmid=int(a_id.text)
                if a_id.get('pub-id-type')=='pmc':
                    pmc=int(a_id.text)
            for a_ff in a_meta.iter('aff'):##############Z找机构
                for af in a_ff.iter('label'):
                    x=int(af.text)

            if x!=0:##########################第一种情况
                for a_ff in a_meta.iter('aff'):##############Z找机构
                    for af in a_ff.iterfind('label'):
                        x=int(af.text)
                        afname.append(af.tail)
                        for s in af.iter('sup'):
                            afname.append(s.tail)
                        for b in af.iter('bold'):
                            afname.append(b.tail)
                        for i in af.iter('italic'):
                            afname.append(i.tail)
                        for sub in af.iter('sub'):
                            afname.append(sub.tail)
                        af_name.update({x:afname})
                for c_group in a_meta.iterfind('contrib-group'):####################多机构
                    for contrib in c_group.iter('contrib'):
                        surname=0
                        givenname=0
                        author_aff=[]
                        for name in contrib.iterfind('name'):
                            surname=name.find('surname').text
                            givenname=name.find('given-names').text
                            author_name=str(str(givenname)+'/'+str(surname))
                        for xref in contrib.iter('xref'):
                            if xref.get('ref-type')=='aff':
                                x=int(xref.text)
                                author_aff.append([af_name.get(x)])
                        writer.writerow([x,pmc,pmid,author_name,author_aff])  #######写出作者 
            if x==0:##########################第二种情况
                author_aff=[]
                for a_ff in a_meta.iter('aff'):
                    author_aff.append(a_ff.text)
                    for s in a_ff.iter('sup'):
                        author_aff.append(s.tail)
                    for b in a_ff.iter('bold'):
                        author_aff.append(b.tail)
                    for i in a_ff.iter('italic'):
                        author_aff.append(i.tail)
                    for sub in a_ff.iter('sub'):
                        author_aff.append(sub.tail)
                if author_aff!=[]:
                    for c_group in a_meta.iterfind('contrib-group'):
                        for contrib in c_group.iter('contrib'):
                            for name in contrib.iter('name'):
                                surname=name.find('surname').text
                                givenname=name.find('given-names').text
                                author_name=str(str(givenname)+'/'+str(surname))
                                writer.writerow([x,pmc,pmid,author_name,author_aff])#########写出作者
            if x==0:##########################第三种情况
                for c_group in a_meta.iterfind('contrib-group'):
                    author_aff=[]
                    for a_ff in c_group.iter('aff'):
                        author_aff.append([a_ff.text])
                        for s in a_ff.iter('sup'):
                            author_aff.append(s.tail)
                        for b in a_ff.iter('bold'):
                            author_aff.append(b.tail)
                        for i in a_ff.iter('italic'):
                            author_aff.append(i.tail)
                        for sub in a_ff.iter('sub'):
                            author_aff.append(sub.tail)
                    if author_aff!=[]:
                        for contrib in c_group.iter('contrib'):
                            for name in contrib.iter('name'):
                                surname=name.find('surname').text
                                givenname=name.find('given-names').text
                                author_name=str(str(givenname)+'/'+str(surname))
                                writer.writerow([x,pmc,pmid,author_name,author_aff])#########写出作者
            if x==0:##########################第四种情况
                for c_group in a_meta.iterfind('contrib-group'):
                        for contrib in c_group.iter('contrib'):
                            author_aff=[]
                            for a_ff in contrib.iter('aff'):
                                author_aff.append(a_ff.text)
                                for s in a_ff.iter('sup'):
                                    author_aff.append(s.tail)
                                for b in a_ff.iter('bold'):
                                    author_aff.append(b.tail)
                                for i in a_ff.iter('italic'):
                                    author_aff.append(i.tail)
                                for sub in a_ff.iter('sub'):
                                    author_aff.append(sub.tail)
                            if author_aff!=[]:
                                for name in contrib.iter('name'):
                                    surname=name.find('surname').text
                                    givenname=name.find('given-names').text
                                    author_name=str(str(givenname)+'/'+str(surname))
                                    writer.writerow([x,pmc,pmid,author_name,author_aff])#########写出作者
                    

"""

            for a_ff in a_meta.iter('aff'):##############Z找机构
                for af in a_ff.iterfind('label'):
                    x=int(af.text)
                    afname.append(af.tail)
                    for s in af.iter('sup'):
                        afname.append(s.tail)
                    for b in af.iter('bold'):
                        afname.append(b.tail)
                    for i in af.iter('italic'):
                        afname.append(i.tail)
                    for sub in af.iter('sub'):
                        afname.append(sub.tail)
                    af_name.update({x:afname})


get('rid')).replace("A","").replace("B","").replace("I","").replace("C","").replace("D","").replace("E","").replace("F","").replace("G","").replace("H","").replace("J",""))
"""
"""
            for a_ff in a_meta.iter('aff'):##############Z找机构
                x=int(str(a_ff.get('id')).replace("A",""))
                for af in a_ff.iterfind('label'):
                    afname.append(af.tail)
                    for s in af.iter('sup'):
                        afname.append(s.tail)
                    for b in af.iter('bold'):
                        afname.append(b.tail)
                    for i in af.iter('italic'):
                        afname.append(i.tail)
                    for sub in af.iter('sub'):
                        afname.append(sub.tail)
                    af_name.update({x:afname})
"""
