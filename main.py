import netCDF4 as nc
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np
from datetime import datetime, timedelta


remote_folder = 'E:/nemo_4.2.2/cfgs/ERA5_input/'
filename = remote_folder + 'interp_2009.nc'
#df = nc.Dataset(filename, mode='a')
df = nc.Dataset(filename)
lon = df['lon']
lat = df['lat']
#list1 = ['u10','v10', 'd2m','t2m', 'msl', 'sp', 'tp',  'sf','strd','ssrd']
list2 = ['mtpr',  'msdwswrf','msdwlwrf','msr']
for str_v in list2:
    var = df[str_v]
    fig, axs = plt.subplots(figsize=(8, 8), nrows=1, ncols=1, subplot_kw={'projection': ccrs.PlateCarree()})
    fig1 = axs.pcolormesh(lon, lat, var[200, :, :], cmap=plt.get_cmap('hot'),
                          transform=ccrs.PlateCarree())
    axs.coastlines()
    fig.colorbar(fig1, label=var.name + ' units =' + var.units)
    axs.set_title('long_name = ' + var.long_name)
    axs.gridlines(draw_labels=True, dms=True, x_inline=False, y_inline=False)
    #axs.set_extent([0, 100, 0, 100])
    plt.show()

breakpoint()












remote_folder = 'E:/nemo_4.2.2/cfgs/ERA5_input/'
#filename = remote_folder + 'AQUA_MODIS.20170701.L3m.DAY.PAR.par.4km.nc'
# Start and end dates in the format YYYYMMDD
start_date = '20170705'
end_date = '20170707'
# Convert the date strings to datetime objects
current_date = datetime.strptime(start_date, '%Y%m%d')
end_date = datetime.strptime(end_date, '%Y%m%d')
while current_date <= end_date:
    # Format the current date as YYYYMMDD
    date_str = current_date.strftime('%Y%m%d')

    # Construct the filename
    filename = f'AQUA_MODIS.{date_str}.L3m.DAY.PAR.par.4km.nc'
    filepath = remote_folder + filename
    df = nc.Dataset(filepath)
    par = np.array(df['par'])
    par[par<-10000]=np.nan
    lon = np.array(df['lon'])
    idxlon = (lon<-30)&(lon>-42)
    lon = lon[idxlon]
    lat = np.array(df['lat'])
    idxlat = (lat<-50)&(lat>-58)
    lat = lat[idxlat]
    par1 = par[idxlat,:]
    par2 = par1[:,idxlon]
    par2 = (par2*6.02e23)/(86400*2.77e18)
    fig, axs = plt.subplots(figsize=(12, 8), nrows=1, ncols=1, subplot_kw={'projection': ccrs.PlateCarree()})
    fig1 = axs.pcolormesh(lon, lat, par2, cmap=plt.get_cmap('hot'), transform=ccrs.PlateCarree())
    fig.colorbar(fig1, label='W m${^-2}$', shrink=.5)
    axs.set_title('datetime: ' + df.time_coverage_start)
    axs.gridlines(draw_labels=True, dms=True, x_inline=False, y_inline=False)
    axs.coastlines()
    plt.show()
    breakpoint()

breakpoint()
df = nc.Dataset(filename)
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













remote_folder_cfg_default = 'D:/nemo_4.2.2/cfgs/ORCA2_ICE_PISCES_CIAN/EXP00/'

f_names = ['u_10.15JUNE2009_fill', 'v_10.15JUNE2009_fill', 'ncar_rad.15JUNE2009_fill', 'ncar_rad.15JUNE2009_fill',
           't_10.15JUNE2009_fill', 'q_10.15JUNE2009_fill', 'ncar_precip.15JUNE2009_fill', 'ncar_precip.15JUNE2009_fill',
           'slp.15JUNE2009_fill']
v_names = ['U_10_MOD', 'V_10_MOD', 'SWDN_MOD', 'LWDN_MOD', 'T_10_MOD','Q_10_MOD', 'PRC_MOD1', 'SNOW', 'SLP']
unit_names = ['m/s', 'm/s', 'w/m$^{2}$','w/m$^{2}$', 'degK','%','kg m $^{-2}$', 'kg m $^{-2}$', 'Pa']
var_names = ['10 metre U wind component', '10 metre V wind component', 'short-wave solar radiation downwards',
             'long-wave solar radiation downwards', '10m temperature','Specific humidity','total precipitation', 'snowfall',
             'surface pressure']

counter = -1
for name in f_names:
    counter += 1
    filename = remote_folder_cfg_default + name + '.nc'
    nc_file = nc.Dataset(filename)
    var = nc_file[v_names[counter]][0,:,:]
    if counter == 0:
        #lon not found in swdn_mod etc.
        lon = nc_file['lon'][:]
        lat = nc_file['lat'][:]
    fig, axs = plt.subplots(figsize=(8, 8), nrows=1, ncols=1, subplot_kw={'projection': ccrs.PlateCarree()})
    fig1 = axs.pcolormesh(lon, lat, var, cmap=plt.get_cmap('hot'),
                          transform=ccrs.PlateCarree())
    fig.colorbar(fig1, label='units =' + unit_names[counter])
    axs.set_title('long_name = ' + var_names[counter])
    axs.coastlines()
    axs.gridlines(draw_labels=True, dms=True, x_inline=False, y_inline=False)
    plt.show()
breakpoint()







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