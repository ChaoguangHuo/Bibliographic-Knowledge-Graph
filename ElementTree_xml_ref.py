import sys
reload(sys) 
sys.setdefaultencoding('utf8')
import numpy as np
import csv
import xml.etree.cElementTree as ET
csvfile=open('C:\Python27\PMC_data\Cpmc_2016_8.csv','wb')######################修改csv名字
tree=ET.parse("C:\Python27\PMC_data\pmc_2016_8.xml")############################修改xml名字
writer=csv.writer(csvfile)
writer.writerow(['pmid','pmc','cpmid','cpmc','cdoi'])
root=tree.getroot()
for article in root.iter('article'):
    pmid=0
    pmc=0
    if any(article.iter('back')):
        for front in article.iter('front'):  
            for ameta in front.iter('article-meta'):
                for aid in ameta.iter('article-id'):
                    if aid.get('pub-id-type')=='pmid':
                        pmid=aid.text
                    if aid.get('pub-id-type')=='pmc':
                        pmc=aid.text
        for back in article.iter('back'):
            for rlist in back.iter('ref-list'):
                for ref in rlist.iter('ref'):
                    cpmid=0
                    cpmc=0
                    cdoi=0
                    for e in ref.iter('element-citation'):
                        for pid in e.iter('pub-id'):
                            if pid.get('pub-id-type')=='pmid':
                                cpmid=pid.text
                            if pid.get('pub-id-type')=='pmc':
                                cpmc=pid.text
                            if pid.get('pub-id-type')=='doi':
                                cdoi=pid.text
                    for m in ref.iter('mixed-citation'):
                        for pid in m.iter('pub-id'):
                            if pid.get('pub-id-type')=='pmid':
                                cpmid=pid.text
                            if pid.get('pub-id-type')=='pmc':
                                cpmc=pid.text
                            if pid.get('pub-id-type')=='doi':
                                cdoi=pid.text
                    for c in ref.iter('citation'):
                        for pid in c.iter('pub-id'):
                            if pid.get('pub-id-type')=='pmid':
                                cpmid=pid.text
                            if pid.get('pub-id-type')=='pmc':
                                cpmc=pid.text
                            if pid.get('pub-id-type')=='doi':
                                cdoi=pid.text
                    writer.writerow([pmid,pmc,cpmid,cpmc,cdoi])
                
            
