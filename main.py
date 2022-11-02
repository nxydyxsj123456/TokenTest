# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from urllib.parse import urlparse

import numpy as np
import torch
import torch.nn.functional as F

import  re
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

#CharType="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.~!*'();:@&=+$,/?#[]"
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tmp= F.softmax( torch.zeros([64,63]))
    url="http://localhost:8080/tienda1/publico/registro.jsp?modo=registro&login=hogan&password=cha377&nombre=iannir&apellidos=lembomba+llargues&email=kaufman@mobilecrm.ao&dni=26321461p&direcciona=travesia+florida+129,+&ciudad=castillo+de+las+guardas,+el&cp=03294&provincia=navarra&ntc=3806083089052885&b1=registrar"
    #url="-_.~!*'();:@&=+$,/?#]["
    url_change =urlparse(url)



    b=re.split('(-)|(_)|(\.)|(~)|(!)|(\*)|(\')|(\()|(\))|(;)|(:)|(@)|(&)|(=)|(\+)|(,)|(/)|(\?)|(#)|(\[)|(\])', url)


    b  =  [char  for  char in b if char not in [None,""]]
    print_hi('PyCharm')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
