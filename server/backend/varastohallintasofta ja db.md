#Toteutus

Varastonhallintaohjelma toteutaan Pythonilla ja database SQLitellä. 
Tiedonsiirto selaimen kanssa tapahtuu HTTP protokollaa käyttäen, hyödyntäen Flask kirjastoa.
Tiedonsiirto PLC:n kanssa tapahtuu MQTT protokollaa käyttäen, hyödyntäen Mosquitto ja Paho.MQTT kirjastoja.

__init__.py 
tiedosto alustaa ohjelman ja luo tarvittavat riippuvaisuudet middlewareihin. 
CORs mahdollistaa ohjelman toimimisen eri porttien välillä. "create_table()" alustaa databasen taulun, mikäli sellaista ei vielä ole tehty. client pyynnöt avaavat yhteyden mosquitto brokerin kanssa. 

app.py
Pääohjelma josta ohjelmaa ajetaan. 
blueprintin avulla reititys ohjataan router.py tiedostoon ohjelman siistimiseksi. 
Viimeiset komennot looppaavat http ja mqtt "kuuntelijat", jotka toimivat eri säikeissä. 

Router.py
tiedostosta reititetään selaimelta tulevat http pyynnöt eteenpäin databaseen ja PLC:lle.

SQlite_controller ja mqtt_controller vastaa etuliitteidensä toiminnoista metodeidensa avulla routerilta tulevien käskyjen mukaan.

httpRequest kansiosta löytyy http yhteyden testialustoja. 