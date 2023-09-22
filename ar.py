import ipyvolume as ipv
fig = ipv.figure()
ipv.examples.klein_bottle()
ipv.save("ar.html", devmode=True)