import sys
reload(sys) 
sys.setdefaultencoding('utf8')

import numpy as np
import csv
import xml.etree.cElementTree as ET

csvfile=open('C:\Python27\PMC_data\p_pmc_2016_1.csv','wb')######################修改csv名字
tree=ET.parse("C:\Python27\PMC_data\pmc_2016_1.xml")############################修改xml名字


writer=csv.writer(csvfile)
writer.writerow(['pmc','pmid','nlm_jr_id','pubmed_jr_id','nlmta_jr_id','iso_abbrev_jr_id','journal_title','ppub','epub','articletype','article_category','article_title','epub_year','ppub_month','keyword','abstract'])

root=tree.getroot()

for article in root.iter('article'):
    articletype=article.get('article-type')
    nlm_jr_id=0
    pubmed_jr_id=0
    nlmta_jr_id=0
    iso_abbrev_jr_id=0
    journal_title=0
    ppub=0
    epub=0
    pmid=0
    pmc=0
    a_title=[]
    article_category=0
    epub_year=0
    ppub_year=0
    abstract=[]
    keyword=[]
    afname={}
    author_name=0
    author_aff=[]    
    for front in article.iterfind('front'):
        for journalmeta in front.iterfind('journal-meta'):
            for x in journalmeta.iterfind('journal-id'):###########journal ID
                if x.get('journal-id-type')=="nlm-journal-id":
                    nlm_jr_id=x.text
                if x.get('journal-id-type')=='pubmed-jr-id':
                    pubmed_jr_id=x.text
                if x.get('journal-id-type')=='nlm-ta':
                    nlmta_jr_id=x.text
                if x.get('journal-id-type')=='iso-abbrev':
                    iso_abbrev_jr_id=x.text       
            for x in journalmeta.iterfind('journal-title-group'):#########journal title
                for y in x.iterfind('journal-title'):
                    journal_title=y.text
            for x in journalmeta.iter('issn'):
                if x.get('pub-type')=='ppub':
                    ppub=x.text
                if x.get('pub-type')=='epub':
                    epub=x.text
        for articlemeta in front.iterfind('article-meta'):
            for articleid in articlemeta.iter('article-id'):########article ID
                if articleid.get('pub-id-type')=='pmid':
                    pmid=int(articleid.text)
                if articleid.get('pub-id-type')=='pmc':
                    pmc=int(articleid.text)
            for articlecategory in articlemeta.iterfind('article-categories'):########article 类别
                for subtype in articlecategory.iterfind('subj-group'):
                    for subject in subtype.iterfind('subject'):
                        article_category=str(subject.text).lower()
            for tgroup in articlemeta.iterfind('title-group'):
                for atitle in tgroup.iterfind('article-title'):##########article title
                    a_title.append(atitle.text)
                    for i in atitle.iter('italic'):
                        a_title.append(i.text)
                        a_title.append(i.tail)
                    for b in atitle.iter('bold'):
                        a_title.append(b.text)
                        a_title.append(b.tail)
                    for s in atitle.iter('sup'):
                        a_title.append(s.tail)
                    for sub in atitle.iter('sub'):
                        a_title.append(sub.tail)                       
            for pubdate in articlemeta.iterfind('pub-date'):
                if pubdate.get('pub-type')=='epub':##########article publish date
                    for yea in pubdate.iterfind('year'):
                        epub_year=int(yea.text)
                if pubdate.get('pub-type')=='ppub':##########article publish date
                    for yea in pubdate.iterfind('year'):
                        ppub_year=int(yea.text)                        
            for abs in articlemeta.iterfind('abstract'):##########article abstract
                for p in abs.iter('p'):
                    abstract.append(p.text)
                    for bold in p.iter('bold'):
                        abstract.append(bold.tail)       
                    for i in p.iter('italic'):
                        abstract.append(i.tail)
                    for s in p.iter('sup'):
                        abstract.append(s.tail)
                for sec in abs.iter('sec'):
                    for p in sec.iter('p'):
                        abstract.append(p.text)
            for keygroup in articlemeta.iterfind('kwd-group'):##########article keyword
                    for kwd in keygroup.iter('kwd'):
                        keyword.append(kwd.text)
                        for i in kwd.iter('italic'):
                            keyword.append(i.text)
                            keyword.append(i.tail)
                        for b in kwd.iter('bold'):
                            keyword.append(b.text)
                            keyword.append(b.tail)
                        for s in kwd.iter('sup'):
                            keyword.append(s.text)
                            keyword.append(s.tail)
                        for sec in kwd.iter('sec'):
                            keyword.append(sec.text)
                            keyword.append(sec.tail)
    writer.writerow([pmc,pmid,nlm_jr_id,pubmed_jr_id,nlmta_jr_id,iso_abbrev_jr_id,journal_title,ppub,epub,articletype,article_category,str(a_title).replace("u'","").replace("', '","").replace("']","").replace("['","").replace("\n","").replace("[","").replace("]","").replace("   "," ").replace("  "," "),epub_year,ppub_year,str(keyword).replace("None,","").replace(",None","").replace("/",",").replace('\n',"").replace("  ","").replace(";",",").replace("‖",",").replace("|","").replace("'","").replace("[","").replace("]","").replace(", ",",").replace("  ","").replace("\n","").replace(",,",""),str(abstract).replace("'\n'","").replace("[","").replace("]"," ").replace("u'"," ").replace(".'"," ").replace('u"',' ').replace("None,","").replace("   "," ").replace("  "," ").replace("  "," ").replace(",,",",")])






















