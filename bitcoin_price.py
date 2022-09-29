import json   # used for unmarshelling jason data into python dictionary
import requests # used for sending request to servers
import datetime
import tkinter as tk
import sqlite3
from tkinter import *


out=tk.Tk() # Initialises Tkinter for graphic interface 
conn=sqlite3.connect('bit_price.db',detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) # initialises database
act=conn.cursor() # sets up starting cursor
out.geometry("500x200") 
def create_table():
    act.execute("CREATE TABLE IF NOT EXISTS Real_time_bit_price (Bitcoin TEXT,Price REAL,Time TIMESTAMP)") # creates table with all needed columns and also time stamp used for getting latest pricing
create_table()
r_set=act.execute("SELECT count(*) as no from Real_time_bit_price") # gets number of rows
rec_count=r_set.fetchone()[0]

def Commit(entry1,entry2,entry3=datetime.datetime.now()): # iputs the data into file bit_price.db
    act.execute("INSERT INTO Real_time_bit_price (Bitcoin,Price,Time) VALUES (?,?,?)",(entry1,entry2,entry3))


def Fetch():
    j=0
    while True:
        ky="https://api.binance.com/api/v3/ticker/price?symbol=" # API used for fetching real time pricing of bitcoins biance.com
        coins=["BTCUSDT"] # bit coin code used at the end of above link
        req=ky+coins[0]
        data=requests.get(req) # sends request to the url API of biance.com and stores its response in data variable
        data=data.json()   # converts json data get from request.get() into python dictionary
        Commit(str(data['symbol']),float(data['price']))
        j+=1
        
        if(j==100):
            show(0) # gives Graphic User Interface output using tkinter and applying paging gor list in decending order of timestamp i.e latest etry shows first than the earlier entries 
            out.mainloop() # starts the GUI interface
            conn.commit()
        # time.sleep(3)
def show(offset): 
    limit=10
    q="SELECT * from Real_time_bit_price ORDER BY Time DESC LIMIT "+ str(offset) +","+str(limit)
    r_set=act.execute(q) # selects list to be displayed wih limit of 10 at each page
    i=0 # row value inside the loop 
    for bit_coin in r_set: 
        for j in range(len(bit_coin)):
            e = Entry(out, width=10, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, bit_coin[j])
        i=i+1
    while (i<limit): # required to blank the balance rows if they are less 
        for j in range(len(bit_coin)):
            e = Entry(0, width=10, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, "")
        i=i+1
    # Show buttons 
    back = offset - limit # This value is used by Previous button
    next = offset + limit # This value is used by Next button       
    b1 = tk.Button(out, text='Next >', command=lambda: show(next))
    b1.grid(row=12,column=4)
    b2 = tk.Button(out, text='< Prev', command=lambda: show(back))
    b2.grid(row=12,column=1)
    if(rec_count <= next): 
        b1["state"]="disabled" # disable next button
    else:
        b1["state"]="active"  # enable next button
        
    if(back >= 0):
        b2["state"]="active"  # enable Prev button
    else:
        b2["state"]="disabled"# disable Prev button 
Fetch()