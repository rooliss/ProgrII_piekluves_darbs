import requests
import bs4
from pprint import pprint
import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox

global url
url = 'https://www.ss.com/lv/transport/cars'

class App:
  def __init__(self, root):
    #loga nosaukums
    root.title("SS.com pārlūks")
    #Loga izmēri
    width = 600
    height = 500
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2,
                                (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)
    

    #Poga lai izvēlētos mercedes-benz auto
    mercedes_poga = tk.Button(root)
    mercedes_poga["bg"] = "#efefef"
    mercedes_poga["activebackground"] = "#28c943"
    ft = tkFont.Font(family='Times', size=10)
    mercedes_poga["font"] = ft
    mercedes_poga["fg"] = "#000000"
    mercedes_poga["justify"] = "center"
    mercedes_poga["text"] = "Mercede-benz"
    mercedes_poga.place(x=40, y=140, width=111, height=50)
    mercedes_poga["command"] = self.mercedes_poga_command

    #poga lai izvēlētos BMW pogu
    bmw_poga = tk.Button(root)
    bmw_poga["bg"] = "#efefef"
    bmw_poga["activebackground"] = "#28c943"
    ft = tkFont.Font(family='Times', size=10)
    bmw_poga["font"] = ft
    bmw_poga["fg"] = "#000000"
    bmw_poga["justify"] = "center"
    bmw_poga["text"] = "BMW"
    bmw_poga.place(x=170, y=140, width=111, height=50)
    bmw_poga["command"] = self.bmw_poga_command

    #poga lai izvēlētos Audi pogu
    audi_poga = tk.Button(root)
    audi_poga["bg"] = "#efefef"
    audi_poga["activebackground"] = "#28c943"
    ft = tkFont.Font(family='Times', size=10)
    audi_poga["font"] = ft
    audi_poga["fg"] = "#000000"
    audi_poga["justify"] = "center"
    audi_poga["text"] = "Audi"
    audi_poga.place(x=300, y=140, width=111, height=50)
    audi_poga["command"] = self.audi_poga_command

    #poga lai izvēlētos Porche pogu
    porsche_poga = tk.Button(root)
    porsche_poga["background"] = "#efefef"
    porsche_poga["activebackground"] = "#28c943"
    ft = tkFont.Font(family='Times', size=10)
    porsche_poga["font"] = ft
    porsche_poga["fg"] = "#000000"
    porsche_poga["justify"] = "center"
    porsche_poga["text"] = "Porche"
    porsche_poga.place(x=440, y=140, width=111, height=50)
    porsche_poga["command"] = self.porsche_poga_command

    #informatīvs teksts
    info_txt_1 = tk.Label(root)
    ft = tkFont.Font(family='Times', size=15)
    info_txt_1["font"] = ft
    info_txt_1["fg"] = "#333333"
    info_txt_1["justify"] = "center"
    info_txt_1["text"] = "Uzzini vai ss.com šodien ir ielikta mašīna ko meklē!"
    info_txt_1.place(x=40, y=0, width=513, height=62)

    #Poga lai sāktu meklēt izvēlēto auto
    meklet_poga = tk.Button(root)
    meklet_poga["bg"] = "#efefef"
    ft = tkFont.Font(family='Times', size=10)
    meklet_poga["font"] = ft
    meklet_poga["fg"] = "#000000"
    meklet_poga["justify"] = "center"
    meklet_poga["text"] = "MEKLĒT"
    meklet_poga.place(x=100, y=320, width=390, height=74)
    meklet_poga["command"] = self.meklet_poga_command

    #vieta lai ievadītu meklējamā auto modeli
    global ievad_lauk
    var = tk.StringVar()
    ievad_lauk = tk.Entry(root, textvariable=var)
    ievad_lauk["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times', size=10)
    ievad_lauk["font"] = ft
    ievad_lauk["fg"] = "#333333"
    ievad_lauk["justify"] = "center"
    ievad_lauk["text"] = "Entry"
    ievad_lauk.place(x=240, y=240, width=111, height=30)

    #informējošais teksts
    info_txt_2 = tk.Label(root)
    ft = tkFont.Font(family='Times', size=12)
    info_txt_2["font"] = ft
    info_txt_2["fg"] = "#333333"
    info_txt_2["justify"] = "center"
    info_txt_2["text"] = "Izvēlies kādu no dotajām mašīnu markām"
    info_txt_2.place(x=120, y=100, width=350, height=32)

    #informējošais teksts
    info_txt_3 = tk.Label(root)
    ft = tkFont.Font(family='Times', size=12)
    info_txt_3["font"] = ft
    info_txt_3["fg"] = "#333333"
    info_txt_3["justify"] = "center"
    info_txt_3["text"] = "Ievadi mašīnas modeli ko vēlies iegādāties"
    info_txt_3.place(x=40, y=200, width=510, height=37)

    
  #mercedes-benz poga
  def mercedes_poga_command(self):
    global current_url
    current_url = None
    current_url = url + "/mercedes/today"

  #BMW poga
  def bmw_poga_command(self):
    global current_url
    current_url = None
    current_url = url + "/bmw/today"
    
  #Audi poga
  def audi_poga_command(self):
    global current_url
    current_url = None
    current_url = url + "/audi/today"

  #porche poga
  def porsche_poga_command(self):
    global current_url
    current_url = None
    current_url = url + "/porsche/today"

  #poga lai uzsāktu meklēt mašīnu
  def meklet_poga_command(self):
    global search_params
    global url
    url = 'https://www.ss.com/lv/transport/cars'
    try:
      data = requests.get(current_url)
      html = bs4.BeautifulSoup(data.text, 'html.parser')
      
      search_params = ievad_lauk.get()
      
      sludDict = {}
        
      tables = html.select('#filter_frm table')
      sludinajumi = tables[2]
      ieraksti = sludinajumi.select('tr')
      skaits = 0
      if search_params == "":
        messagebox.showerror("showerror", "Ievadi mašīnas modeli")
      else:
        for each in ieraksti:
          teksts = each.select('.msga2-o')
          sludDict[skaits] = {}
          for i, katrs in enumerate(teksts):
              if i == 0:
                if not katrs.text == search_params:
                  sludDict.pop(skaits)
                  break
                else:  
                  sludDict[skaits]["Modelis"] = katrs.text
              if i == 1:
                sludDict[skaits]["gads"] = katrs.text
              if i == 2:
                sludDict[skaits]["motora tilpums"] = katrs.text
              if i == 3:
                sludDict[skaits]["nobraukums"] = katrs.text
              if i == 4:
                sludDict[skaits]["Cena"] = katrs.text
          skaits += 1
        del(sludDict[0])
        print(len(sludDict))
        if len(sludDict) == 1:
          keys = list(sludDict.keys())
          if sludDict[keys[0]] == {}:
            del(sludDict[keys[0]])

        
        pprint(sludDict, sort_dicts=False)

        messagebox.showinfo("Apsveicam", sludDict)
    except NameError:
      messagebox.showerror("showerror", "Ievadi mašīnas marku")
      
if __name__ == "__main__":
  root = tk.Tk()
  app = App(root)
  root.mainloop()