
#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import math
#math.log(x[, base])

vcf = sys.argv[1]
fs = open( vcf )

ac = []
for i, line in enumerate( fs ):
    if "#" in line:
        continue
    fields = line.split()
    info = fields[7].split(";")

    ac.append(int(info[0].replace("AC=","")))

fig, ax = plt.subplots()
ax.hist( ac, density=True )
ax.set_yscale("log")
ax.set_ylim(1e-8, 1e-2)
ax.set_title(vcf)
ax.set_xlabel("AC counts")
ax.set_ylabel("Frequency")
fig.savefig( vcf + ".png" )
plt.show()
fs.close()

