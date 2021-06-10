site = "http://google.com"
site = site[site.index("/")+2:site.index(".")]
three = site[:3]
length = len(site)
e = site.count("e")
print(f"{three}{length}{e}!")

site = "http://google.com"
site = site[site.index("/")+2:site.index(".")]
print(site[:3]+str(len(site))+str(site.count("e"))+"!")
