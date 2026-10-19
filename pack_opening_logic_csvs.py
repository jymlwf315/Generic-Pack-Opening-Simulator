import math
import random
import os
import sys
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from PIL import Image
from PIL import ImageTk
from datetime import datetime
import csv

directory = os.path.dirname(os.path.abspath(sys.argv[0]))
directory_fixed = ""
iterate_d = 0
for fx in directory:
    if fx == '\\':
        directory_fixed += '/'
    else:
        directory_fixed += fx
    iterate_d += 1
print(directory_fixed)
filepath_packs = directory_fixed + "/Packs.csv"

total_iteration = 0
pack_name = []
common_pulls = []
rare_pulls = []
super_pulls = [""]
ultra_pulls = [""]
secret_pulls = [""]
commons_from_all_packs = []
rares_from_all_packs = []
supers_from_all_packs = []
ultras_from_all_packs = []
secrets_from_all_packs = []
common_numbers_from_each_pack = []
rare_numbers_from_each_pack = []
super_numbers_from_each_pack = []
ultra_numbers_from_each_pack = []
secret_numbers_from_each_pack = []
button_clicked = 0
#-----------------------------------------------------------------------------------------------------------#
#----------------------------------------This is where the code begins--------------------------------------#
#-----------------------------------------------------------------------------------------------------------#
with open(filepath_packs, newline = '') as packsfile:
    reader = csv.reader(packsfile,delimiter=';',quotechar='|')
    next(reader,None)
    for row in reader:
        commons_found = False
        for i in row:
            if i.isdigit() and commons_found == False:
                commons_found = True
                common_pulls.append(i)
            elif i.isdigit() and commons_found == True:
                rare_pulls.append(i)
            elif i.isdigit() == False:
                pack_name.append(i)
for i2 in range(len(pack_name)):
    pack_contents_commons = []
    pack_contents_commons_numbers = []
    pack_contents_rares = []
    pack_contents_rares_numbers = []
    pack_contents_supers = []
    pack_contents_supers_numbers = []
    pack_contents_ultras = []
    pack_contents_ultras_numbers = []
    pack_contents_secrets = []
    pack_contents_secrets_numbers = []
    with open(directory_fixed + "/Packs/" + pack_name[i2] + "/Commons.csv") as commonsfile:
        reader_common = csv.reader(commonsfile,delimiter=';',quotechar='|')
        next(reader_common,None)
        for row in reader_common:
            for i in row:
                if i.isdigit():
                    pack_contents_commons_numbers.append(i)
                else:
                    pack_contents_commons.append(i)
        commons_from_all_packs.append(pack_contents_commons)
        common_numbers_from_each_pack.append(pack_contents_commons_numbers)
    with open(directory_fixed + "/Packs/" + pack_name[i2] + "/Rares.csv") as raresfile:
        reader_rare = csv.reader(raresfile,delimiter=';',quotechar='|')
        next(reader_rare,None)
        for row in reader_rare:
            for i in row:
                if i.isdigit():
                    pack_contents_rares_numbers.append(i)
                else:
                    pack_contents_rares.append(i)
        rares_from_all_packs.append(pack_contents_rares)
        rare_numbers_from_each_pack.append(pack_contents_rares_numbers)
    with open(directory_fixed + "/Packs/" + pack_name[i2] + "/Super Rares.csv") as supersfile:
        reader_super = csv.reader(supersfile,delimiter=';',quotechar='|')
        next(reader_super,None)
        for row in reader_super:
            for i in row:
                if i.isdigit():
                    pack_contents_supers_numbers.append(i)
                else:
                    pack_contents_supers.append(i)
        supers_from_all_packs.append(pack_contents_supers)
        super_numbers_from_each_pack.append(pack_contents_supers_numbers)
    with open(directory_fixed + "/Packs/" + pack_name[i2] + "/Ultra Rares.csv") as ultrasfile:
        reader_ultra = csv.reader(ultrasfile,delimiter=';',quotechar='|')
        next(reader_ultra,None)
        for row in reader_ultra:
            for i in row:
                if i.isdigit():
                    pack_contents_ultras_numbers.append(i)
                else:
                    pack_contents_ultras.append(i)
        ultras_from_all_packs.append(pack_contents_ultras)
        ultra_numbers_from_each_pack.append(pack_contents_ultras_numbers)

    with open(directory_fixed + "/Packs/" + pack_name[i2] + "/Secret Rares.csv") as secretsfile:
        reader_secret = csv.reader(secretsfile,delimiter=';',quotechar='|')
        next(reader_secret,None)
        for row in reader_secret:
            for i in row:
                if i.isdigit():
                    pack_contents_secrets_numbers.append(i)
                else:
                    pack_contents_secrets.append(i)
        secrets_from_all_packs.append(pack_contents_secrets)
        secret_numbers_from_each_pack.append(pack_contents_secrets_numbers)

    total_iteration += 1                                                                                                 

#-----------------------------------------------------------------------------------------------------------#
#-------------------------------This is where the pack opening function is----------------------------------#
#-----------------------------------------------------------------------------------------------------------#
current_pulls_images = []
current_pulls_names = []
current_pulls_numbers = []
def openpack (c, r, clist, rlist, su_list, ulist, se_list, numbs_c, numbs_r, numbs_su, numbs_u, numbs_se, b):
    current_pulls_images.clear()
    current_pulls_names.clear()
    current_pulls_numbers.clear()
    iterate_c = 0
    iterate_r = 0
    iterate_su = 0
    iterate_u = 0
    iterate_se = 0
    iterate_numc = 0
    iterate_numr = 0
    iterate_numsu = 0
    iterate_numu = 0
    iterate_numse = 0
    cards_common = []
    for fc in range(len(clist)):
        cards_common.append(clist[iterate_c])
        iterate_c += 1
    cards_rare = []
    for fr in range(len(rlist)):
            cards_rare.append(rlist[iterate_r])
            iterate_r += 1
    cards_super = []
    for fsu in range(len(su_list)):
            cards_super.append(su_list[iterate_su])
            iterate_su += 1
    #print(cards_rare)
    cards_ultra = []
    for fu in range(len(ulist)):
            cards_ultra.append(ulist[iterate_u])
            iterate_u += 1
    cards_secret = []
    for fse in range(len(se_list)):
            cards_secret.append(se_list[iterate_se])
            iterate_se += 1
    card_numbers_common = []
    for fnc in range(len(numbs_c)):
            card_numbers_common.append(numbs_c[iterate_numc])
            iterate_numc += 1
    card_numbers_rare = []
    for fnr in range(len(numbs_r)):
            card_numbers_rare.append(numbs_r[iterate_numr])
            iterate_numr += 1
    card_numbers_super = []
    for fnsu in range(len(numbs_su)):
            card_numbers_super.append(numbs_su[iterate_numsu])
            iterate_numsu += 1
    card_numbers_ultra = []
    for fnu in range(len(numbs_u)):
            card_numbers_ultra.append(numbs_u[iterate_numu])
            iterate_numu += 1
    card_numbers_secret = []
    for fnse in range(len(numbs_se)):
            card_numbers_secret.append(numbs_se[iterate_numse])
            iterate_numse += 1
    common_amount = int(c)
    rare_amount = int(r)
    total_amount = common_amount + rare_amount
    #----------Card Image Variables----------#
    image_iterate = 0
    card_images = []
    ttk_images = []
    ttk_labels = []
    rare_images = 0
    #----------------------------------------#
    pulls_common = []
    pulls_common_numbers = []
    pulls_rare = []
    pulls_rare_numbers = []
    ratios = []
    commons_pulled = 0
    rares_pulled = 0
    random_pulled = 0
    rare_types_available = []

    check_ratios = open(directory_fixed + "/Packs/" + pack_name[b] + "/Ratios.txt")
    ratio_lines = check_ratios.readlines()
    for ratio in ratio_lines:
         current_number = ""
         for num in ratio:
              found_a_comma = False
              if num.isdigit() == True:
                current_number += num
              elif num.isdigit() == False:
                ratios.append(int(current_number))
                current_number = ""              
    check_ratios.close()

    if len(ratios) >= 1:
        for addrare in range(ratios[0]):
            rare_types_available.append("rare")
    if len(ratios) >= 2:
        for addsupers in range(ratios[1]):
            rare_types_available.append("super")
    if len(ratios) >= 3:
        for addultras in range(ratios[2]):
            rare_types_available.append("ultra")
    if len(ratios) >= 4:
        for addsecrets in range(ratios[3]):
            rare_types_available.append("secret")
    for i in range(total_amount):
        if rares_pulled < rare_amount:
            if len(rare_types_available) == 1:   
                random_pulled = random.randint(0,len(cards_rare) - 1)
                pulls_rare.append(cards_rare[random_pulled])
                current_pulls_names.append(pulls_rare[rares_pulled])
                pulls_rare_numbers.append(card_numbers_rare[random_pulled])
                try:
                    try:
                        card_images.append(Image.open(directory_fixed + '/Packs/' + pack_name[b] + '/Images/Rares/' + pulls_rare_numbers[rares_pulled] + ".png").resize((card_width_tk.get(), card_height_tk.get())))
                    except:
                        card_images.append(Image.open(directory_fixed + '/Packs/' + pack_name[b] + '/Images/Rares/' + pulls_rare_numbers[rares_pulled] + ".jpg").resize((card_width_tk.get(), card_height_tk.get())))
                    ttk_images.append(ImageTk.PhotoImage(card_images[i]))
                    current_pulls_images.append(ttk_images[i])
                    table.insert(parent = '', index = 0, values = (pulls_rare[i], 'Rare'), image = ttk_images[i])
                except: 
                    print("could not find rare image for " + pulls_rare_numbers[rares_pulled] + " in " + pack_name[b])
                    if size_picked.get() == 0:
                        current_pulls_images.append(small_tk)
                    elif size_picked.get() == 1:
                        current_pulls_images.append(medium_tk)
                    elif size_picked.get() == 2:
                        current_pulls_images.append(default_tk)
                    table.insert(parent = '', index = 0, values = (pulls_rare[i], 'Rare'))
            else:
                rare_type_pulled = random.choice(rare_types_available)
                if rare_type_pulled == "rare":
                    random_pulled = random.randint(0,len(cards_rare) - 1)
                    pulls_rare.append(cards_rare[random_pulled])
                    current_pulls_names.append(pulls_rare[rares_pulled])
                    pulls_rare_numbers.append(card_numbers_rare[random_pulled])
                    try:
                        try:
                            card_images.append(Image.open(directory_fixed + '/Packs/' + pack_name[b] + '/Images/Rares/' + pulls_rare_numbers[rares_pulled] + ".png").resize((card_width_tk.get(), card_height_tk.get())))
                        except:
                            card_images.append(Image.open(directory_fixed + '/Packs/' + pack_name[b] + '/Images/Rares/' + pulls_rare_numbers[rares_pulled] + ".jpg").resize((card_width_tk.get(), card_height_tk.get())))
                        ttk_images.append(ImageTk.PhotoImage(card_images[i]))
                        current_pulls_images.append(ttk_images[i])
                        table.insert(parent = '', index = 0, values = (pulls_rare[i], 'Rare'), image = ttk_images[i])
                    except:
                        print("could not find rare image")
                        if size_picked.get() == 0:
                            current_pulls_images.append(small_tk)
                        elif size_picked.get() == 1:
                            current_pulls_images.append(medium_tk)
                        elif size_picked.get() == 2:
                            current_pulls_images.append(default_tk)
                        table.insert(parent = '', index = 0, values = (pulls_rare[i], 'Rare'))
                elif rare_type_pulled == "super":
                    random_pulled = random.randint(0,len(cards_super) - 1)
                    pulls_rare.append(cards_super[random_pulled])
                    current_pulls_names.append(pulls_rare[rares_pulled])
                    pulls_rare_numbers.append(card_numbers_super[random_pulled])
                    try:
                        try:
                            card_images.append(Image.open(directory_fixed + '/Packs/' + pack_name[b] + '/Images/Super Rares/' + pulls_rare_numbers[rares_pulled] + ".png").resize((card_width_tk.get(), card_height_tk.get())))
                        except:
                            card_images.append(Image.open(directory_fixed + '/Packs/' + pack_name[b] + '/Images/Super Rares/' + pulls_rare_numbers[rares_pulled] + ".jpg").resize((card_width_tk.get(), card_height_tk.get())))
                        ttk_images.append(ImageTk.PhotoImage(card_images[i]))
                        current_pulls_images.append(ttk_images[i])
                        table.insert(parent = '', index = 0, values = (pulls_rare[i], 'Super Rare'), image = ttk_images[i])
                    except:
                        print("could not find super rare image")
                        if size_picked.get() == 0:
                            current_pulls_images.append(small_tk)
                        elif size_picked.get() == 1:
                            current_pulls_images.append(medium_tk)
                        elif size_picked.get() == 2:
                            current_pulls_images.append(default_tk)
                        table.insert(parent = '', index = 0, values = (pulls_rare[i], 'Super Rare'))
                elif rare_type_pulled == "ultra":
                    random_pulled = random.randint(0,len(cards_ultra) - 1)
                    pulls_rare.append(cards_ultra[random_pulled])
                    current_pulls_names.append(pulls_rare[rares_pulled])
                    pulls_rare_numbers.append(card_numbers_ultra[random_pulled])
                    try:
                        try:
                            card_images.append(Image.open(directory_fixed + '/Packs/' + pack_name[b] + '/Images/Ultra Rares/' + pulls_rare_numbers[rares_pulled] + ".png").resize((card_width_tk.get(), card_height_tk.get())))
                        except:
                            card_images.append(Image.open(directory_fixed + '/Packs/' + pack_name[b] + '/Images/Ultra Rares/' + pulls_rare_numbers[rares_pulled] + ".jpg").resize((card_width_tk.get(), card_height_tk.get())))
                        ttk_images.append(ImageTk.PhotoImage(card_images[i]))
                        current_pulls_images.append(ttk_images[i])
                        table.insert(parent = '', index = 0, values = (pulls_rare[i], 'Ultra Rare'), image = ttk_images[i])
                    except:
                        print("could not find ultra rare image")
                        if size_picked.get() == 0:
                            current_pulls_images.append(small_tk)
                        elif size_picked.get() == 1:
                            current_pulls_images.append(medium_tk)
                        elif size_picked.get() == 2:
                            current_pulls_images.append(default_tk)
                        table.insert(parent = '', index = 0, values = (pulls_rare[i], 'Ultra Rare'))
                elif rare_type_pulled == "secret":
                    random_pulled = random.randint(0,len(cards_secret) - 1)
                    pulls_rare.append(cards_secret[random_pulled])
                    current_pulls_names.append(pulls_rare[rares_pulled])
                    pulls_rare_numbers.append(card_numbers_secret[random_pulled])
                    try:
                        try:
                            card_images.append(Image.open(directory_fixed + '/Packs/' + pack_name[b] + '/Images/Secret Rares/' + pulls_rare_numbers[rares_pulled] + ".png").resize((card_width_tk.get(), card_height_tk.get())))
                        except:
                            card_images.append(Image.open(directory_fixed + '/Packs/' + pack_name[b] + '/Images/Secret Rares/' + pulls_rare_numbers[rares_pulled] + ".jpg").resize((card_width_tk.get(), card_height_tk.get())))
                        ttk_images.append(ImageTk.PhotoImage(card_images[i]))
                        current_pulls_images.append(ttk_images[i])
                        table.insert(parent = '', index = 0, values = (pulls_rare[i], 'Secret Rare'), image = ttk_images[i])
                    except:
                        print("could not find secret rare image")
                        if size_picked.get() == 0:
                            current_pulls_images.append(small_tk)
                        elif size_picked.get() == 1:
                            current_pulls_images.append(medium_tk)
                        elif size_picked.get() == 2:
                            current_pulls_images.append(default_tk)
                        table.insert(parent = '', index = 0, values = (pulls_rare[i], 'Secret Rare'))    
            rares_pulled += 1  
        else:
            random_pulled = random.randint(0,len(cards_common) - 1)
            pulls_common.append(cards_common[random_pulled])
            current_pulls_names.append(pulls_common[commons_pulled])
            pulls_common_numbers.append(card_numbers_common[random_pulled])
            try:
                try:
                    card_images.append(Image.open(directory_fixed + '/Packs/' + pack_name[b] + '/Images/Commons/' + pulls_common_numbers[commons_pulled] + ".png").resize((card_width_tk.get(), card_height_tk.get())))
                except:
                    card_images.append(Image.open(directory_fixed + '/Packs/' + pack_name[b] + '/Images/Commons/' + pulls_common_numbers[commons_pulled] + ".jpg").resize((card_width_tk.get(), card_height_tk.get())))
                ttk_images.append(ImageTk.PhotoImage(card_images[i]))
                #card_image.configure(image = ttk_images[i])
                current_pulls_images.append(ttk_images[i])
                #card_image.configure(image = current_pulls_images[i])
                table.insert(parent = '', index = 0, values = (pulls_common[i - rare_amount], 'Common'), image = ttk_images[i])
            except:
                print("Could not find common image for " + pulls_common_numbers[commons_pulled] + " in " + pack_name[b])
                if size_picked.get() == 0:
                    current_pulls_images.append(small_tk)
                elif size_picked.get() == 1:
                    current_pulls_images.append(medium_tk)
                elif size_picked.get() == 2:
                    current_pulls_images.append(default_tk)
                table.insert(parent = '', index = 0, values = (pulls_common[i - rare_amount], 'Common'))
            commons_pulled += 1
        #print(len(current_pulls_images))
    #print("Commons: ")  
    #print(pulls_common)
    #print("Common numbers: ")
    #print(pulls_common_numbers)
    #print("Rares: ")
    #print(pulls_rare)
    #print("Rare Numbers: ")
    #print(pulls_rare_numbers)
            
    #images loop
    #for pulls in range(total_amount):
    #    if rare_images < r:
    #        card_images.append(Image.open(directory_fixed + '/Packs/' + pack_name[b] + '/Images/Rares/' + pulls_rare_numbers[b] + ".png").resize((300, 440)))
    #        rare_images += 1
    #    else:
    #        card_images.append(Image.open(directory_fixed + '/Packs/' + pack_name[b] + '/Images/Commons/' + pulls_common_numbers[b] + ".png").resize((300, 440)))
    #    width, height = card_images[pulls].size 
    #    ttk_images.append(ImageTk.PhotoImage(card_images[pulls]))
            
        #canvas = tk.Canvas(window, width=cards_width)
        #canvas.create_image(0, 0, anchor='nw', image=ttk_images[pulls])
        #for rare_pulls in range(len(pulls_rare)):
            #ttk_labels.append(ttk.Label(master = window, text = pulls_rare[rare_pulls] + " (rare)"))
        #for common_pulls in range(len(pulls_common)):
            #ttk_labels.append(ttk.Label(master = window, text = pulls_common[common_pulls]))
            #table.insert(parent = '', index = 0, values = (pulls_common[common_pulls]))
        #ttk_labels[pulls].pack()
        
        
#print(rare_numbers_from_each_pack[button_clicked])
#openpack(common_pulls[button_clicked],rare_pulls[button_clicked],commons_from_all_packs[button_clicked],rares_from_all_packs[button_clicked],common_numbers_from_each_pack[button_clicked],rare_numbers_from_each_pack[button_clicked])

#-----------------------------------------------------------------------------------------------------------#
#---------------------------------------This is where the visuals begin-------------------------------------#
#-----------------------------------------------------------------------------------------------------------#
    
def setnumber(inp):
    new_pack.set(True)
    new_button_clicked.set(inp)
    print(new_button_clicked.get())
    deletetable()
    new_pack.set(False)

def runOpenPack ():
    deletetable()
    openpack(common_pulls[new_button_clicked.get()],
             rare_pulls[new_button_clicked.get()],
             commons_from_all_packs[new_button_clicked.get()],
             rares_from_all_packs[new_button_clicked.get()],
             supers_from_all_packs[new_button_clicked.get()],
             ultras_from_all_packs[new_button_clicked.get()],
             secrets_from_all_packs[new_button_clicked.get()],
             common_numbers_from_each_pack[new_button_clicked.get()],
             rare_numbers_from_each_pack[new_button_clicked.get()],
             super_numbers_from_each_pack[new_button_clicked.get()],
             ultra_numbers_from_each_pack[new_button_clicked.get()],
             secret_numbers_from_each_pack[new_button_clicked.get()],
             new_button_clicked.get())

def deletetable ():
    for i in table.get_children():
        table.delete(i)
    if size_picked.get() == 0:
         card_image.configure(image = small_tk)
    elif size_picked.get() == 1:
         card_image.configure(image = medium_tk)
    elif size_picked.get() == 2:
        card_image.configure(image = default_tk)

def setsmall ():
     card_width_tk.set(cards_width_small)
     card_height_tk.set(cards_height_small)
     size_picked.set(0)
     print('set small')
def setmedium ():
     card_width_tk.set(cards_width_medium)
     card_height_tk.set(cards_height_medium)
     size_picked.set(1)
     print('set medium')
def setlarge ():
     card_width_tk.set(cards_width_large)
     card_height_tk.set(cards_height_large)
     size_picked.set(2)

def savePulls():
     
     filename = ""
     if len(current_pulls_names) > 0:
        curtime = datetime.now()
        #print(curtime.strftime("%m"))
        #curtime.strftime("%Y") gets year
        #curtime.strftime("%m") gets month
        #curtime.strftime("%d") gets day
        #curtime.strftime("%H:%M:%S") gets exact time
        if curtime.strftime("%m") == "01":
            filename += "January"
        elif curtime.strftime("%m") == "02":
            filename += "February"
        elif curtime.strftime("%m") == "03":
            filename += "March"
        elif curtime.strftime("%m") == "04":
            filename += "April"
        elif curtime.strftime("%m") == "05":
            filename += "May"
        elif curtime.strftime("%m") == "06":
            filename += "June"
        elif curtime.strftime("%m") == "07":
            filename += "July"
        elif curtime.strftime("%m") == "08":
            filename += "August"
        elif curtime.strftime("%m") == "09":
            filename += "September"
        elif curtime.strftime("%m") == "10":
            filename += "October"
        elif curtime.strftime("%m") == "11":
            filename += "November"
        elif curtime.strftime("%m") == "12":
            filename += "December"
        filename += curtime.strftime("-" + "%d" + "-%Y" +"_%H %M %S")
        try:
            saved = open(directory_fixed + "/Packs/" + pack_name[new_button_clicked.get()] + "/Pulls/" + filename + ".txt","a")
            for sv in current_pulls_names:
                saved.write(sv + "\n")
            saved.close()
        except:
            os.mkdir(directory_fixed + "/Packs/" + pack_name[new_button_clicked.get()] + "/Pulls")
            saved = open(directory_fixed + "/Packs/" + pack_name[new_button_clicked.get()] + "/Pulls/" + filename + ".txt","a")
            for sv in current_pulls_names:
                saved.write(sv + "\n")
            saved.close()

default_width = "1600"
default_height = "900"
chosen_font = "Calibri"
fontsize = '24'
padding_x = int(int(default_width) / 100)
padding_y = padding_x
pack_iterate = 0
button_iterate = 0
pack_buttons = []
pack_numbers = []
cards_width_small = 330
cards_height_small = 440
cards_width_medium = 495
cards_height_medium = 660
cards_width_large = 660
cards_height_large = 880
cards_width = cards_width_medium
cards_height = cards_height_medium

#window
window = tk.Tk()
window.title('Card Pack Opening Simulator')
window.geometry(default_width + 'x' + default_height)
new_pack = tk.BooleanVar()
size_picked = tk.IntVar()
size_picked.set(2)
new_pack.set(False)
ratio_rares = tk.IntVar()
ratio_supers = tk.IntVar()
ratio_ultras = tk.IntVar()
ratio_secrets = tk.IntVar()

def item_select(_):
    if new_pack.get() == False:
        selected_value = table.focus()
        details_of_selected = table.item(selected_value)
        card_name = details_of_selected.get('values')[0]
        #print(card_name)
        iter = 0
        for i in current_pulls_names:
            if i == card_name:
                card_image.configure(image = current_pulls_images[iter])
            iter += 1
    
#side buttons
new_button_clicked = tk.IntVar()
input_frame = ttk.Frame(master = window)
for p in range(len(pack_name)):
    pack_buttons.append(ttk.Button(master = input_frame, text = pack_name[pack_iterate], command = lambda p = p:setnumber(p)))
    pack_buttons[pack_iterate].pack(padx = padding_x, pady = padding_y)
    pack_numbers.append(pack_iterate)
    pack_iterate += 1
input_frame.pack(side = 'left')

card_width_tk = tk.IntVar()
card_width_tk.set(cards_width)
card_height_tk = tk.IntVar()
card_height_tk.set(cards_height)
card_frame = ttk.Frame(master = window)
default_image = Image.open(directory_fixed + "/card_back.jpg")
res_image = default_image.resize((card_width_tk.get(),card_height_tk.get()))
res_image2 = default_image.resize((cards_width_medium,cards_height_medium))
res_image3 = default_image.resize((cards_width_small,cards_height_small))
default_tk = ImageTk.PhotoImage(res_image)
medium_tk = ImageTk.PhotoImage(res_image2)
small_tk = ImageTk.PhotoImage(res_image3)
card_image = ttk.Label(master = card_frame, text = "Card Image", image = default_tk)

button_small = tk.Button(card_frame, text = 'Small',width=20,height=2,command=setsmall)
button_medium = tk.Button(card_frame, text = 'Medium',width=20,height=2,command=setmedium)
button_large = tk.Button(card_frame, text = 'Large',width=20,height=2,command=setlarge)
card_image.pack(padx = padding_x)
button_small.pack(side='left',padx=padding_x,pady = padding_y)
button_medium.pack(side='left',padx=padding_x,pady=padding_y)
button_large.pack(side='left',padx=padding_x,pady=padding_y)
card_frame.pack(side='right')

#output
#cards_width = tk.IntVar()
#cards_width = int((int(default_width) * 2) / 3)
#cards_frame = tk.Canvas(master = window, bg = "white")
#cards_frame.pack()
font1 = ['Calibri',18,'normal']
style = ttk.Style()
style.configure("Treeview", rowheight=40, font = font1)
style.configure("Treeview.Heading", font=(None,24))
table = ttk.Treeview(window, columns = ('card name','card rarity'), show = 'headings')
table.heading('card name', text="Card Name")
table.heading('card rarity', text="Card Rarity")
table.pack(fill = 'both', expand = True)
openPackButton = tk.Button(master = window, text = 'OpenPack',width=20,height=2, command = runOpenPack)
openPackButton.pack(side='left',padx=padding_x,pady = padding_y)
savePullsButton = tk.Button(window, text = "Save Pulls",width=20,height=2, command = savePulls)
savePullsButton.pack(side='right',padx=padding_x,pady=padding_y)

table.bind('<<TreeviewSelect>>', item_select)

#run
window.mainloop()