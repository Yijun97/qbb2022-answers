import bdg_loader
import sys
import matplotlib.pyplot as plt

D0_H3K27ac_data = bdg_loader.load_data(sys.argv[3])
D2_H3K27ac_data = bdg_loader.load_data(sys.argv[4])
D2_Klf4_data = bdg_loader.load_data(sys.argv[2])
D2_Sox2_R1_data = bdg_loader.load_data(sys.argv[1])

fig, ax = plt.subplots(4,1)


ax[3].fill_between(D2_H3K27ac_data["X"], D2_H3K27ac_data["Y"], y2 = 0, label = "H3K27ac_day2")

ax[2].fill_between(D0_H3K27ac_data["X"], D0_H3K27ac_data["Y"], y2 = 0, label = "H3K27ac_day0")
ax[1].fill_between(D2_Klf4_data["X"], D2_Klf4_data["Y"], y2 = 0, label = "Klf4")
ax[0].fill_between(D2_Sox2_R1_data["X"],D2_Sox2_R1_data["Y"], y2 = 0, label = "Sox2")
ax[2].xaxis.set_visible(False)
ax[1].xaxis.set_visible(False)
ax[0].xaxis.set_visible(False)

ax[2].set_ylim([0, 25000])

ax[0].legend()
ax[1].legend()
ax[2].legend()
ax[3].legend()

plt.show()
plt.savefig("Part1_ChIP_Plot.png")