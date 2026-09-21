from pyscript import document
from pyscript import web

import random
from datetime import datetime


toggleswitch = False

# --- Dependent variables ---

# Data from the SKU Generator™
if True:
    counter = 0
    sku_category = ""
    sku_pname = ""
    sku_quantity = ""

# Data from the reciept generator
selected = [False, False, False, False, False]
amount = [0, 0, 0, 0, 0]
value = [0, 0, 0, 0, 0]
price = [0, 0, 0, 0, 0]

namedata = ""
# --- Independent variables for edited elements ---

# Elements from the SKU Generator™
if True:
    
    Output = document.getElementById("sku_output")

    t_pid = document.getElementById("t_pid")
    t_category = document.getElementById("t_category")
    t_name = document.getElementById("t_name")
    t_quantity = document.getElementById("t_quantity")

    # Sku Alerts
    t_productalert = document.getElementById("t_productalert")
    t_productcategory = document.getElementById("t_productcategory")

# Elements from the Reciept Generator (SPAGHETTI MONSTER)

r_output = document.getElementById("r_output")
show = document.getElementById("show")

name = document.getElementById("name")
ordername = document.getElementById("ordername")
itemorder1 = document.getElementById("itemorder1")
itemamount1 = document.getElementById("itemamount")
itemprice1 = document.getElementById("itemprice")

itemorder2 = document.getElementById("itemorder2")
itemamount2 = document.getElementById("itemamount2")
itemprice2 = document.getElementById("itemprice2")

itemorder3 = document.getElementById("itemorder3")
itemamount3 = document.getElementById("itemamount3")
itemprice3 = document.getElementById("itemprice3")

itemorder4 = document.getElementById("itemorder4")
itemamount4 = document.getElementById("itemamount4")
itemprice4 = document.getElementById("itemprice4")

itemorder5 = document.getElementById("itemorder5")
itemamount5 = document.getElementById("itemamount5")
itemprice5 = document.getElementById("itemprice5")

namealert = document.getElementById("namealert")

## Writes SKU
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

## Function that modifies order element with data given to save time (SO SO MUCH TIME ONG)
itemnumber = 0
def ordercheck(orderitem):
            itemnumber = str(int(orderitem+1))

            temporder = document.getElementById("itemorder" + itemnumber)
            tempamount = document.getElementById("itemamount" + itemnumber)
            tempprice = document.getElementById("itemprice" + itemnumber)

            if amount[orderitem] != 0:
                temporder.removeAttribute("hidden")
                tempamount.textContent = str(amount[orderitem])
                tempprice.textContent = "₱"+str(price[orderitem])

            itemnumber = 0

## Modifies Order
def create_order(event):
    global selected
    global amount
    global name
    global price

    ## Ditto 
    emptyform = False

    now = datetime.now()
    time = now.strftime("%H:%M")

    ## --- prepare to dive into spagetti ---

    ## gets name
    namedata = document.getElementById("name").value

    ## gets the value of each product
    value = [document.getElementById("item1").value, document.getElementById("item2").value, document.getElementById("item3").value, document.getElementById("item4").value, document.getElementById("item5").value]

    ## checks which items are selected
    selected = [document.getElementById("item1").checked, document.getElementById("item2").checked, document.getElementById("item3").checked, document.getElementById("item4").checked, document.getElementById("item5").checked]

    ## adds to counter depending on which ones are selected
    amount = [amount[0] + int(selected[0]), amount[1] + int(selected[1]), amount[2] + int(selected[2]), amount[3] + int(selected[3]), amount[4] + int(selected[4])]

    ## adds to price
    price = [price[0] + (int(value[0])*int(selected[0])), price[1] + (int(value[1])*int(selected[1])), price[2] + (int(value[2])*int(selected[2])), price[3] + (int(value[3])*int(selected[3])), price[4] + (int(value[4])*int(selected[4]))]

    # --- Checks if the name was inputted ---
    if namedata.strip() != "": 
        namealert.setAttribute("hidden", "true")
    else:
        namealert.removeAttribute("hidden")
        emptyform = True

    ordercheck(0)
    ordercheck(1)
    ordercheck(2)
    ordercheck(3)
    ordercheck(4)



    if emptyform == False:
        ordername.textContent = namedata + "," + time
        show.setAttribute("hidden", "true")
        r_output.removeAttribute("hidden")
        document.getElementById("totalorder").textContent = "₱"+str(int(price[0] + price[1] + price[2] + price[3] + price[4]))
    print(price)

## Resets Order  
def reset_order(event):
    global selected
    global amount
    global name
    global price

    ## Reset em variables

    selected = [False, False, False, False, False]
    amount = [0, 0, 0, 0, 0]
    value = [0, 0, 0, 0, 0]
    price = [0, 0, 0, 0, 0]

    namedata = ""

    ## Reset em elements, n' tell them their user that they resseted their doggone orders 

    resetcount = 0
    while resetcount != 4:

         resetcountstring = str(int(resetcount+1))
         temporder = document.getElementById("itemorder" + resetcountstring)
         tempamount = document.getElementById("itemamount" + resetcountstring)
         tempprice = document.getElementById("itemprice" + resetcountstring)

         temporder.setAttribute("hidden", "true")
         tempamount.textContent = ""
         tempprice.textContent = ""

         resetcount += 1
         
         

    r_output.setAttribute("hidden", "true")
    show.removeAttribute("hidden")
    show.innerHTML = "<p class='text-muted text-center mb-0'>You reset your order.</p>"


    