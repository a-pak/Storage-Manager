#Storage manager for warehouses

Scalable storage manager that works in a browser. It can be connected to a remote PLC using MQTT broker. 
Frontend works with React.js
Backend is created with Python using Flask for API calls, while database handling is done with with SQLite.
When you send a HTTP request from browser (i.e. add or order a product from/to docking area) it first sends the request to the server, that then publishes MQTT message to a wanted topic. 
