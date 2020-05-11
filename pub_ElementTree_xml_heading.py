#--*-- coding:utf-8 --*--
import sys
reload(sys) 
sys.setdefaultencoding('utf8')
import numpy as np
import csv
import xml.etree.cElementTree as ET

tree=ET.parse("C:/Python27/PUB_data/pub_2009.xml")

csvfile=open('C:/Python27/PUB_data/Hpub_2009.csv','wb')
writer=csv.writer(csvfile)
writer.writerow(['pmid','DescriptorName','QualifierName','DescriptorName_UI','D_MajorTopicYN','Q_MajorTopicYN'])

root=tree.getroot()
for particle in root.iter('PubmedArticle'):
    pmid=0
    for mc in particle.iter('MedlineCitation'):
        for pid in mc.iter('PMID'):
            pmid=pid.text
            v=pid.get('Version')
        for mhl in mc.iter('MeshHeadingList'):
            for mh in mhl.iter('MeshHeading'):
                dname=[]
                qname=[]
                dui=[]
                dty=[]
                qui=[]
                qty=[]
                for d in mh.iter('DescriptorName'):
                    dname.append(d.text)
                    dui.append(d.get('UI'))
                    dty.append(d.get('MajorTopicYN'))
                for q in mh.iter('QualifierName'):
                    qname.append(q.text)
                    qui.append(q.get('UI'))
                    qty.append(q.get('MajorTopicYN'))
                writer.writerow([pmid,str(dname).replace("[]","").replace("', '","/").replace("['","").replace("']",""),str(qname).replace("[]","").replace("', '","/").replace("['","").replace("']",""),str(dui).replace("[]","").replace("', '","/").replace("['","").replace("']",""),str(dty).replace("[]","").replace("', '","/").replace("['","").replace("']",""),str(qui).replace("[]","").replace("', '","/").replace("['","").replace("']",""),str(qty).replace("[]","").replace("', '","/").replace("['","").replace("']","")])
