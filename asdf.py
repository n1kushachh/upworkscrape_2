new_link = []
link = 'https://www.advisoryexcellence.com/experts-search/?fwp_paged='
for x in range(1, 262):
    new_link.append(link+str(x))

print(new_link)    