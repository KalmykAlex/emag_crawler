[![Generic badge](https://img.shields.io/badge/python_version-3.7-blue.svg)](https://shields.io/)

# E-commerce website crawler

Online Retail store website crawler for price monitoring

### Project structure

 - crawler.py - script that sends http requests, filters responses using BeautifulSoup and then saves the data in csv format
 - echipamente - directory that contains folders with csv data from grouped equipment cathegories
 
### Usage

 __Heads up!__ This project is taylored to work with emag.ro site. All the links and the data mining procedure are specific for that site. If you want to use this for another site you will need to change the code accordingly.
 
 If you want to monitor the prices on emag.ro you will have to do the following:
 - Hardcode the links of the product cathegory you want to monitor in the *links* variable from *crawler.py* (ex. 'https://www.emag.ro/*product type*/c' )
 - Then you will need to automate the *crawler.py* script to gather data periodically
 - Finally you can use the tools inside *data_visualisation.py* to visualise your gathered data
 
### Script Automation

 To gather price data automatically you will need to either:
 - __Linux__ - set a crontab for crawler.py
 - __Windows__ - use Task Sheduler to create a task
 
### Further development
 
 - creating more complex data visualisation tools

