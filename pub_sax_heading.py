import xml.sax
import csv
import numpy as n

csvfile=open('C:\PUB_data\H_pubmed_1992_1993.csv','wb')
writer=csv.writer(csvfile)
writer.writerow(['pmid','Version','DescriptorName','QualifierName','DescriptorName_UI','QualifierName_UI'])


class PubmedHandler(xml.sax.ContentHandler):
        def __init__(self):
                self.CurrentData = ""
                self.pmid = ""
                self.pmc = ""
                self.dname=""
                self.qname=""
                self.v=""
                self.pmid=""   
        def startElement(self,tag,attributes):
                self.CurrentData=tag
                if tag=="PMID":
                        self.pmid=""
                        self.v=attributes["Version"]
                elif tag=="MeshHeading":
                        self.dname=""
                        self.qname=""
                        self.qui=""
                        self.dui=""
                elif tag=="DescriptorName":
                        self.dui+=(attributes["UI"]+'/')
                elif tag=="QualifierName":
                        self.qui+=(attributes["UI"]+'/')

        def characters(self,content):
                if self.CurrentData=="PMID":
                        self.pmid+=content
                elif self.CurrentData=="DescriptorName":
                        self.dname+=(content+'/')
                elif self.CurrentData=="QualifierName":
                        self.qname+=(content+'/')
  
        def endElement(self,name):
                if name=="MeshHeading":
                        writer.writerow([self.pmid.replace('\n','').replace("    ","").replace("  ","").replace("  ",""),self.v,self.dname.replace('\n','').replace("      "," ").replace("   "," ").replace("  "," ").replace("// /","/"),self.qname.replace('\n','').replace("/ "," ").replace(" /"," ").replace("      "," ").replace("   "," ").replace("  "," ").replace("/ ","/"),self.dui,self.qui])
                       
if ( __name__ == "__main__"):
        parser = xml.sax.make_parser()# create XMLReader
        Handler=PubmedHandler()# rewrite ContextHandler
        parser.setContentHandler( Handler )
        parser.parse("C:\PUB_data\pubmed_1992_1993.xml")
