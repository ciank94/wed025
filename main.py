import netCDF4 as nc
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np
remote_folder = 'D:/nemo_4.2.2/cfgs/ERA5_input/'
domain_prefix = 'WED025_5d'
year_prefix = '_20000101_20001231_'
var_prefix = 'grid_T'

#filename = remote_folder + domain_prefix + year_prefix + var_prefix +'.nc'
filename = remote_folder + 'interp_output.nc'
#filename = remote_folder + 'download1.nc'

df = nc.Dataset(filename)
Td = df['d2m'][0, :, :] - 273.15
T = df['t2m'][0, :, :] - 273.15
lon = df['lon']
lat = df['lat']
eTd = 6.1078*(np.exp((17.1*Td)/(235+Td)))
eT = 6.1078*(np.exp((17.1*T)/(235+T)))
RH = 100*(eTd/eT)
#RH = 100 - (T - Td)*5
fig, axs = plt.subplots(figsize=(8, 8), nrows=1, ncols=1, subplot_kw={'projection': ccrs.PlateCarree()})
fig1 = axs.pcolormesh(lon, lat, RH, cmap=plt.get_cmap('hot'),
                          transform=ccrs.PlateCarree())
axs.coastlines()
fig.colorbar(fig1, label='RH ' + ' units =' + '%')
axs.set_title('long_name = ' + 'relative humidity')
axs.gridlines(draw_labels=True, dms=True, x_inline=False, y_inline=False)
#axs.set_extent([0, 100, 0, 100])
plt.show()


breakpoint()
lon = df['lon']
lat = df['lat']
for str_v in ['u10','v10', 'd2m','t2m', 'msl', 'sp', 'tp',  'sf','strd','ssrd']:
    var = df[str_v]
    fig, axs = plt.subplots(figsize=(8, 8), nrows=1, ncols=1, subplot_kw={'projection': ccrs.PlateCarree()})
    fig1 = axs.pcolormesh(lon, lat, var[0, :, :], cmap=plt.get_cmap('hot'),
                          transform=ccrs.PlateCarree())
    axs.coastlines()
    fig.colorbar(fig1, label=var.name + ' units =' + var.units)
    axs.set_title('long_name = ' + var.long_name)
    axs.gridlines(draw_labels=True, dms=True, x_inline=False, y_inline=False)
    #axs.set_extent([0, 100, 0, 100])
    plt.show()
    breakpoint()


breakpoint()
fig, axs = plt.subplots(figsize=(8, 8), nrows=1, ncols=1, subplot_kw={'projection': ccrs.PlateCarree()})
fig1 = axs.pcolormesh(df['lon'], df['lat'], df['u10'][0,:,:], cmap=plt.get_cmap('hot'), transform=ccrs.PlateCarree())
axs.coastlines()
fig.colorbar(fig1, label='u10, units =' + df['u10'].units)
axs.set_title('long_name = ' + df['u10'].long_name)
plt.show()
breakpoint()
d_layers = df['deptht'][:]
#plt.plot(d_layers)
temp = df['thetao'][0,0,:,:]
temp[temp==0]=np.nan
dp = df['e3t'][0,0,:,:]
fig, axs = plt.subplots(figsize=(8, 8), nrows=1, ncols=1, subplot_kw={'projection': ccrs.PlateCarree()})
axs.pcolormesh(df['nav_lon'][:,0], df['nav_lat'][:,0],temp, cmap=plt.get_cmap('hot'), transform=ccrs.PlateCarree())
breakpoint()