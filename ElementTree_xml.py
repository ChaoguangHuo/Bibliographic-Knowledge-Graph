import sys
reload(sys) 
sys.setdefaultencoding('utf8')

import numpy as np
import csv
import xml.etree.cElementTree as ET

papercsvfile=open('C:/Python27/PMC_data/paper_pmc2000.csv','wb')
paperw=csv.writer(papercsvfile)
paperw.writerow(['pmc','pmid','nlm_jr_id','pubmed_jr_id','nlmta_jr_id','iso_abbrev_jr_id','journal_title','ppub','epub','article_category','article_title','epub_year','ppub_month','keyword','abstract'])

authorcsvfile=open('C:/Python27/PMC_data/author_pmc2000.csv','wb')
authorw=csv.writer(authorcsvfile)
authorw.writerow(['pmc','pmid','author_name','author_aff'])

refcsvfile=open('C:/Python27/PMC_data/ref_pmc2000.csv','wb')
refw=csv.writer(refcsvfile)
refw.writerow(['pmc','pmid','ref_pmid','ref_pmc'])



tree=ET.parse("C:\Python27\PMC_data\pmc2000.xml")
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
    article_title=0
    article_category=0
    epub_year=0
    ppu_year=0
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
            for titlegroup in articlemeta.iterfind('title-group'):
                for articletitle in titlegroup.iterfind('article-title'):##########article title
                    article_title=articletitle.text
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
                for sec in abs.iter('sec'):
                    for p in sec.iter('p'):
                        abstract.append(p.text)
            for keygroup in articlemeta.iterfind('kwd-group'):##########article keyword
                if keygroup.get('kwd-group-type')=='author':
                    for kwd in keygroup.iter('kwd'):
                        keyword.append(kwd.text)
        for articlemeta in front.iterfind('article-meta'):
            for articleid in articlemeta.iter('article-id'):########article ID
                if articleid.get('pub-id-type')=='pmid':
                    pmid=int(articleid.text)
                if articleid.get('pub-id-type')=='pmc':
                    pmc=int(articleid.text)           
            for aff in articlemeta.iter('aff'):
                name=aff.text
                for af in aff.iterfind('label'):
                    afnumber=int(af.text)
                    if afnumber!=0:
                        afname=update({afnumber:name})
            if afnumber!=0:
                for contribgroup in articlemeta.iterfind('contrib-group'):
                    for contrib in contribgroup.iter('contrib'):
                        for name in contrib.iterfind('name'):
                            surname=0
                            givenname=0
                            for sur in name.iterfind('surname'):
                                surname=sur.text.lower()
                            for given in name.iterfind('given-names'):
                                givenname=given.text.lower()
                            author_name=str(str(givenname)+'/'+str(surname))
                        for xref in contrib.iter('xref'):
                            xnumber=int(xref.text)
                            author_aff.append(afname.get(xnumber))
                        authorw.writerow([pmc,pmid,author_name,author_aff])  #######写出作者                                     
            if afnumber==0:
                for contribgroup in articlemeta.iterfind('contrib-group'):
                    afname=0
                    for affcontrib in contribgroup.iterfind('aff'):
                        afname=affcontrib.text
                    for contrib in contribgroup.iter('contrib'):
                        for name in contrib.iterfind('name'):
                            surname=0
                            givenname=0
                            for sur in name.iterfind('surname'):
                                surname=sur.text.lower()
                            for given in name.iterfind('given-names'):
                                givenname=given.text.lower()
                            author_name=str(str(givenname)+'/'+str(surname))
                        authorw.writerow([pmc,pmid,author_name,afname])#########写出作者
    for back in article.iterfind('back'):
        for reflist in front.iterfind('ref-list'):
            for ref in reflist.iter('ref'):
                for mixcitation in ref.iter('mixed-citation'):
                    for pubid in mixcitation.iter('pub-id'):
                        ref_pmid=0
                        ref_pmc=0
                        if pubid.get('pub-id-type')=='pmid':
                            ref_pmid=int(pubid.text)
                        if pubid.get('pub-id-type')=='pmc':
                            ref_pmc=int(pubid.text)
                        refw.writerow([pmc,pmid,ref_pmid,ref_pmc])########写出参考文献                                                                                  

    paperw.writerow([pmc,pmid,nlm_jr_id,pubmed_jr_id,nlmta_jr_id,iso_abbrev_jr_id,journal_title,ppub,epub,article_category,article_title,epub_year,ppub_year,str(keyword).replace("'","").replace("[","").replace("]","").replace(", ",","),str(abstract).replace("[","").replace("]","")])





























