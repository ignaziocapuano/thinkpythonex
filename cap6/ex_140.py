#Postal Codes

dictionary={"A":"Newfoundland","B":"Nova Scotia","C":"Prince Edward Island","E":"New Brunswick","G":"Quebec.","H":"Quebec","J":"Quebec","K":"Ontario","L":"Ontario",\
            "M":"Ontario","N":"Ontario","P":"Ontario","R":"Manitoba","S":"Saskatchewan","T":"Alberta","V":"British Columbia","X":"Nunavut","X":"Northwest territories","Y":"Yukon"}

postal_code=input("Inserisci codice postale canadese X0X XXX:")
postal_code=postal_code.upper()
if postal_code[0] not in dictionary.values() or not postal_code[1].isnumeric() or len(postal_code)!=6:
    print("Codice non valido")
    quit()
key=postal_code[0]
if postal_code[1]==0:
    zona="Rurale"
else:
    zona="Urbana"
print("Il codice è di",dictionary[key],", zona",zona)
