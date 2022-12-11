-- A query to retrieve words and their types from Joukahainen XML based Word List
WITH data AS
( 
	SELECT
      xml_sanat::xml as query_column 
   FROM xml_testi1
) 
SELECT 
   xml.form AS sana, 
   xml.wclass AS tyyppi
FROM data, 
     XMLTABLE 
     (
         '/wordlist/word/forms' PASSING query_column 
         COLUMNS 
              form text PATH 'form',
		      wclass text PATH '../classes/wclass'            
      ) xml  