# Bitcoin_pricing
This repository is for an API that i created for fetching bitcoin price in real time and show its list to you, list is in descending order of its timestamp so always latest price is shown to you. I have use python for fetching bitcoin price from
 
 This is my first Attempt at creating backend api using Python.
 ** Following are what i have achieved in this:-**
 - requesting real time pricing of bitcoins using biance.com API.
 - json module usage for converting recieved info from json fromat to python dictionary
 - tkinter for creating graphic user interface and that shows price list in latest to oldest fashion with* Timestamp and Paging (10 entries at each page)
 - SQlite3 module of python for creating light weight database file where prices fetched by the API is stored
 - the paging provided by me take into consideration the case of last page being incomplete and leaves space for the missing lined
 - Paging has "prev" and "next" buttons to move from one page to another.
 - Final API was not created but it is a working program which runs on local desktops and give the desired output as neede.

Code parts are explained using comments in the bitcoin_price.py file
