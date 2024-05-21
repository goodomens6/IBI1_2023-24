import xml.dom.minidom
import time
import xml.sax
import matplotlib.pyplot as plt

start_time1=time.time()

DOMTree=xml.dom.minidom.parse("go_obo.xml")
collection=DOMTree.documentElement
terms=collection.getElementsByTagName("term")
molecular_function=0
biological_process=0
cellular_component=0

for term in terms:
    if term.getElementsByTagName("namespace")[0].firstChild.nodeValue=="molecular_function":
        molecular_function+=1
    if term.getElementsByTagName("namespace")[0].firstChild.nodeValue=="biological_process":
        biological_process+=1
    if term.getElementsByTagName("namespace")[0].firstChild.nodeValue=="cellular_component":
        cellular_component+=1

print("The number of molecular function is",molecular_function)
print("The number of biological process is",biological_process)
print("The number of cellular component is",cellular_component)

plt.figure(1)
plt.bar(["moleculare function","biological process","cellular component"],[molecular_function,biological_process,cellular_component])
plt.title("The number of different terms with three ontology(DOM)")
plt.xlabel("ontology")
plt.ylabel("the number of terms")

end_time1=time.time()
time_taken1=end_time1-start_time1
print("The time DOM used is",str(time_taken1)+"s")

class TermsHandler (xml.sax.ContentHandler):
    def __init__(self):
        self.molecular_function=0
        self.biological_process=0
        self.cellular_component=0
    def characters(self, content):
        if content=="molecular_function":
            self.molecular_function+=1
        elif content=="biological_process":
            self.biological_process+=1
        elif content=="cellular_component":
            self.cellular_component+=1
    def endDocument(self):
        print("The number of molecular function is",self.molecular_function)
        print("The number of biological process is",self.biological_process)
        print("The number of cellular component is",self.cellular_component)
        plt.figure(2)
        plt.bar(["molecular function","biological process","cellular compnent"],[self.molecular_function,self.biological_process,self.cellular_component])
        plt.title("The number of different terms with three ontology(SAX APIs)")
        plt.xlabel("ontology")
        plt.ylabel("the number of terms")

start_time2=time.time()
parser=xml.sax.make_parser()
parser.setContentHandler(TermsHandler())
parser.parse("go_obo.xml")
end_time2=time.time()
time_taken2=end_time2-start_time2
print("The time SAX APIs used is",str(time_taken2)+"s")

plt.show()
plt.clf
