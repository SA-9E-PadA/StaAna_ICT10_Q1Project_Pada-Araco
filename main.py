from pyscript import document
from pyscript import web

import random


toggleswitch = False

# --- Dependent variables ---

# Data from the SKU Generator™
counter = 0
sku_category = ""
sku_pname = ""
sku_quantity = ""



# --- Independent variables for edited elements ---

# Elements from the SKU Generator™
Output = document.getElementById("sku_output")

t_pid = document.getElementById("t_pid")
t_category = document.getElementById("t_category")
t_name = document.getElementById("t_name")
t_quantity = document.getElementById("t_quantity")

# Sku Alerts
t_productalert = document.getElementById("t_productalert")
t_productcategory = document.getElementById("t_productcategory")

def generate_sku(event):
    # The function presses the emptyform button to stop any incomplete form from entering the website
    emptyform = False

    # Hides the alerts if the user DID follow the instructions
    t_productcategory.setAttribute("hidden", "true")
    t_productalert.setAttribute("hidden", "true")

    # Steals the data from those pesky input fields
    sku_category = document.getElementById("category").value
    sku_pname = document.getElementById("product_name").value
    sku_quantity = document.getElementById("quantity").value

    # Checks if the name was inputted
    if sku_pname.strip() != "": 
        t_productalert.setAttribute("hidden", "true")
    else:
        t_productalert.removeAttribute("hidden")
        emptyform = True

    # Chekcs if the Quantity was given, and if it's positive
    if sku_quantity.strip() != "" and float(sku_quantity) > 0: 
        t_productcategory.setAttribute("hidden", "true")

    else:
          t_productcategory.removeAttribute("hidden")
          emptyform = True

    
    # Generates the code for the Sku
    if emptyform == False: 
        codenum1 = len(sku_category+sku_pname)*int(sku_quantity)
        codenum2 = (len(sku_category+sku_pname)+6+int(sku_quantity))**5
        codenum3 = (len(sku_category+sku_pname)+int(sku_quantity))**3

        codestring1 = str(int(str(codenum1)[:4]))
        codestring2 = str(int(str(codenum2)[:6]))
        codestring3 = str(int(str(codenum3)[:4]))

    # If the forms were properly inputted, send data to the html page
    if emptyform == False:

        t_pid.textContent = codestring1 + "-" + codestring2 + "-" + codestring3
        t_name.textContent = sku_pname
        t_category.textContent = "Category: " + sku_category
        t_quantity.textContent = "Quantity: " + sku_quantity
        
        Output.removeAttribute("hidden")


    



    