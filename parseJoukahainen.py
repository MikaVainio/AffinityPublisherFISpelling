import xmltodict
import xml.etree.ElementTree as ET

joukahainen = '''<?xml version="1.0" encoding="UTF-8" ?>
<wordlist xml:lang="fi">
<word id="w499539">
	<forms>
		<form>Aaretti</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>risti-av1</infclass>
	</inflection>
</word>
<word id="w499540">
	<forms>
		<form>Agonist</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kalsium</infclass>
	</inflection>
</word>
<word id="w499541">
	<forms>
		<form>Airam</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kalsium</infclass>
	</inflection>
</word>
<word id="w499542">
	<forms>
		<form>Akademi</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>risti</infclass>
	</inflection>
</word>
<word id="w499543">
	<forms>
		<form>Akava</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>asema</infclass>
	</inflection>
</word>
<word id="w499544">
	<forms>
		<form>Akira</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kala</infclass>
		<infclass type="historical">karahka</infclass>
	</inflection>
</word>
<word id="w499545">
	<forms>
		<form>Al</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>loppu</infclass>
	</inflection>
</word>
<word id="w499546">
	<forms>
		<form>Alesis</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>vastaus</infclass>
	</inflection>
</word>
<word id="w499547">
	<forms>
		<form>Alko</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>valo</infclass>
	</inflection>
</word>
<word id="w499548">
	<forms>
		<form>Allah</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>edam</infclass>
	</inflection>
</word>
<word id="w499549">
	<forms>
		<form>Alta=vista</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kala</infclass>
	</inflection>
	<usage>
		<flag>it</flag>
	</usage>
	<info>
		<description>Yritys, Internetin hakupalvelu ym.</description>
	</info>
</word>
<word id="w499550">
	<forms>
		<form>Animalia</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kulkija</infclass>
	</inflection>
</word>
<word id="w499551">
	<forms>
		<form>Annessa</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kala</infclass>
	</inflection>
	<style>
		<flag>foreign</flag>
	</style>
</word>
<word id="w499552">
	<forms>
		<form>Apollon</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kalsium</infclass>
	</inflection>
</word>
<word id="w499553">
	<forms>
		<form>Aquarius</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>vastaus</infclass>
	</inflection>
</word>
<word id="w499554">
	<forms>
		<form>Aristoteles</form>
	</forms>
	<classes>
		<wclass>pnoun_firstname</wclass>
	</classes>
	<inflection>
		<infclass>vieras</infclass>
	</inflection>
</word>
<word id="w499555">
	<forms>
		<form>Aspirin</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kalsium</infclass>
	</inflection>
</word>
<word id="w499556">
	<forms>
		<form>Atamon</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kalsium</infclass>
	</inflection>
</word>
<word id="w499557">
	<forms>
		<form>Ateneum</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kalsium</infclass>
	</inflection>
</word>
<word id="w499558">
	<forms>
		<form>Athene</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>nalle</infclass>
	</inflection>
</word>
<word id="w499559">
	<forms>
		<form>Atorox</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kalsium</infclass>
	</inflection>
</word>
<word id="w499560">
	<forms>
		<form>Audi</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>risti</infclass>
	</inflection>
</word>
<word id="w499561">
	<forms>
		<form>Bamix</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kalsium</infclass>
	</inflection>
</word>
<word id="w499562">
	<forms>
		<form>Barabbas</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>vastaus</infclass>
	</inflection>
</word>
<word id="w499563">
	<forms>
		<form>Basic</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kalsium</infclass>
	</inflection>
</word>
<word id="w499564">
	<forms>
		<form>Benecol</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kalsium</infclass>
	</inflection>
</word>
<word id="w499565">
	<forms>
		<form>Bernese</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>nalle</infclass>
	</inflection>
</word>
<word id="w499566">
	<forms>
		<form>Blarnia</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kulkija</infclass>
	</inflection>
	<style>
		<flag>foreign</flag>
	</style>
</word>
<word id="w499567">
	<forms>
		<form>Borealis</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>vastaus</infclass>
	</inflection>
</word>
<word id="w499568">
	<forms>
		<form>Botnia</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kulkija</infclass>
		<infclass type="historical">karahka</infclass>
	</inflection>
</word>
<word id="w499569">
	<forms>
		<form>Burana</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>karahka</infclass>
		<infclass type="historical">pasuuna</infclass>
	</inflection>
</word>
<word id="w499570">
	<forms>
		<form>Centro</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>valo</infclass>
	</inflection>
</word>
<word id="w499571">
	<forms>
		<form>Centrum</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kalsium</infclass>
	</inflection>
</word>
<word id="w499572">
	<forms>
		<form>Cialis</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>vastaus</infclass>
	</inflection>
	<application>
		<flag>not_voikko</flag>
	</application>
</word>
<word id="w499573">
	<forms>
		<form>Coca-Cola</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>koira</infclass>
	</inflection>
</word>
<word id="w499574">
	<forms>
		<form>Colt</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kalsium</infclass>
	</inflection>
</word>
<word id="w499575">
	<forms>
		<form>Core</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>nalle</infclass>
	</inflection>
</word>
<word id="w499576">
	<forms>
		<form>Crash</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kalsium</infclass>
	</inflection>
</word>
<word id="w499577">
	<forms>
		<form>Crichton-Vulcan</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>edam</infclass>
	</inflection>
</word>
<word id="w499578">
	<forms>
		<form>Cujo</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>valo</infclass>
	</inflection>
</word>
<word id="w499579">
	<forms>
		<form>Cygni</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>risti</infclass>
	</inflection>
</word>
<word id="w499580">
	<forms>
		<form>Damokles</form>
	</forms>
	<classes>
		<wclass>pnoun_firstname</wclass>
	</classes>
	<inflection>
		<infclass>vieras</infclass>
	</inflection>
</word>
<word id="w499581">
	<forms>
		<form>Decamerone</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>nalle</infclass>
	</inflection>
</word>
<word id="w499582">
	<forms>
		<form>Dei</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>pii</infclass>
	</inflection>
</word>
<word id="w499583">
	<forms>
		<form>Disc=world</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kalsium</infclass>
	</inflection>
	<style>
		<flag>foreign</flag>
	</style>
</word>
<word id="w499584">
	<forms>
		<form>Edita</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kala</infclass>
	</inflection>
</word>
<word id="w499585">
	<forms>
		<form>Elka</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kala</infclass>
	</inflection>
	<application>
		<flag>not_voikko</flag>
	</application>
</word>
<word id="w499586">
	<forms>
		<form>Eres</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>vastaus</infclass>
	</inflection>
</word>
<word id="w499587">
	<forms>
		<form>Erikeeper</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>edam</infclass>
	</inflection>
</word>
<word id="w499588">
	<forms>
		<form>Esso</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>valo</infclass>
	</inflection>
</word>
<word id="w499589">
	<forms>
		<form>Estonia</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kulkija</infclass>
		<infclass type="historical">karahka</infclass>
	</inflection>
</word>
<word id="w499590">
	<forms>
		<form>Euref</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kalsium</infclass>
	</inflection>
</word>
<word id="w499591">
	<forms>
		<form>Facta</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kala</infclass>
	</inflection>
	<info>
		<description>tietosanakirja tai tietopalvelu</description>
	</info>
</word>
<word id="w499592">
	<forms>
		<form>Fedora</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kulkija</infclass>
	</inflection>
	<usage>
		<flag>it</flag>
	</usage>
</word>
<word id="w499593">
	<forms>
		<form>Finax</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kalsium</infclass>
	</inflection>
</word>
<word id="w499594">
	<forms>
		<form>Finncon</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kalsium</infclass>
	</inflection>
	<application>
		<flag>not_voikko</flag>
	</application>
</word>
<word id="w499595">
	<forms>
		<form>Finn=air</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kalsium</infclass>
	</inflection>
</word>
<word id="w499596">
	<forms>
		<form>Finnref</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kalsium</infclass>
	</inflection>
	<application>
		<flag>not_voikko</flag>
	</application>
</word>
<word id="w499597">
	<forms>
		<form>Finnvaate</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>hame-av2</infclass>
	</inflection>
	<application>
		<flag>not_voikko</flag>
	</application>
</word>
<word id="w499598">
	<forms>
		<form>Finnzine</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>nalle</infclass>
	</inflection>
	<application>
		<flag>not_voikko</flag>
	</application>
</word>
<word id="w499599">
	<forms>
		<form>Finvaate</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>hame-av2</infclass>
	</inflection>
	<application>
		<flag>not_voikko</flag>
	</application>
</word>
<word id="w499600">
	<forms>
		<form>Folkvisa</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kala</infclass>
	</inflection>
</word>
<word id="w499601">
	<forms>
		<form>Ford</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kalsium</infclass>
	</inflection>
</word>
<word id="w499602">
	<forms>
		<form>Fotozuumi</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>risti</infclass>
	</inflection>
</word>
<word id="w499603">
	<forms>
		<form>Freija</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kala</infclass>
	</inflection>
</word>
<word id="w499604">
	<forms>
		<form>Gaudeamus</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>vastaus</infclass>
	</inflection>
</word>
<word id="w499605">
	<forms>
		<form>Genos</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>vastaus</infclass>
	</inflection>
</word>
<word id="w499606">
	<forms>
		<form>Granini</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>paperi</infclass>
		<infclass type="historical">banaali</infclass>
	</inflection>
</word>
<word id="w499607">
	<forms>
		<form>Halloween</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kalsium</infclass>
	</inflection>
</word>
<word id="w499608">
	<forms>
		<form>Hamlet</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>kalsium</infclass>
	</inflection>
</word>
<word id="w499609">
	<forms>
		<form>Hari</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>risti</infclass>
	</inflection>
</word>
<word id="w499610">
	<forms>
		<form>Helios</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>vastaus</infclass>
	</inflection>
</word>
<word id="w499611">
	<forms>
		<form>Hesari</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>paperi</infclass>
	</inflection>
</word>
<word id="w499612">
	<forms>
		<form>Homeros</form>
	</forms>
	<classes>
		<wclass>pnoun_misc</wclass>
	</classes>
	<inflection>
		<infclass>vastaus</infclass>
	</inflection>
</word>
</wordlist>
'''
#dictionry = xmltodict.parse(joukahainen)
# print(dictionry)

xmlTree = ET.parse('testxml.xml')
root = xmlTree.getroot()
rootName = root.tag
print(rootName)
words = []
for node in root.findall('./word/forms/form'):
    words.append(node.text)
print(words)
print(len(words))   
