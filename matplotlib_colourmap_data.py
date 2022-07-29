from matplotlib import cm

cmap = cm.get_cmap('coolwarm')

rgb_data = []
for i in range(0, 255+1):
    rgba = cmap(i/255)
    rbg = list(rgba[0:3])
    rbg = [round(f,5) for f in rbg]
    rgb_data.append(rbg)

print(rgb_data)