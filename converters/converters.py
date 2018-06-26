print("converters.py")

# Converters

def percent2float(x):
    return float(x.strip('%'))/100

def str2float(x):
    return float(x.replace(',',''))

def str2int(x):
    return int(str(x))