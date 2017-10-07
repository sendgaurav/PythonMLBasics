from numpy import loadtxt
import urllib.request as ulib
raw_data = ulib.urlopen('https://goo.gl/vhm1eU')
dataset = loadtxt(raw_data, delimiter=",")
print(dataset.shape)
