a = 'cY1S dCjG eDi 9idG y2Am y1Si IJCY 64d2 FdNq XMHM gQrT hvRh icvC VR0T ofMA qImb dBan ni7W XZIc rOl0 ZLMt ngsQ LP5Q O8fI QCy8 wuAv'
comb = a.split(' ')
letter_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

mapper = {'cY1S': 'a', 'dCjG': 'b', 'eDMi': 'c', '9idG': 'd', 'y2Am': 'e', 'y1Si': 'f', 'IJCY': 'g', '64d2': 'h', 'FdNq': 'i', 'XMHM': 'j', 'gQrT': 'k', 'hvRh': 'l', 'icvC': 'm', 'VR0T': 'n', 'ofMA': 'o', 'qImb': 'p', 'dBan': 'q', 'ni7W': 'r', 'XZIc': 's', 'rOl0': 't', 'ZLMt': 'u', 'ngsQ': 'v', 'LP5Q': 'w', 'O8fI': 'x', 'QCy8': 'y', 'wuAv': 'z',"sss":"}","fff":"{"}

encoded= ['y1Si', 'hvRh', 'cY1S', 'IJCY', 'fff', '64d2', 'y2Am', 'ni7W', 'y2Am', 'FdNq', 'XZIc', 'QCy8', 'ofMA', 'ZLMt', 'ni7W', '9idG', 'y2Am', 'eDMi', 'ofMA', '9idG', 'y2Am', '9idG', 'rOl0', 'y2Am', 'O8fI', 'rOl0', 'sss']

for i in encoded:
    print(mapper[i],end="")


