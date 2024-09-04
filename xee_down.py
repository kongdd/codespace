import os.path
import ee
import xee
import xarray as xr
import xarray

# band, var = "surface_pressure", "Pa"
# band, var = "surface_net_thermal_radiation", "Rln"
bands = [
    "surface_net_thermal_radiation", "surface_net_solar_radiation", 
    "surface_latent_heat_flux", "surface_sensible_heat_flux", 
    "u_component_of_wind_10m", "v_component_of_wind_10m",
    "temperature_2m", "dewpoint_temperature_2m",
    "surface_pressure"
]
# prefix = "HuBei_%s_" % var
prefix = "HuBei_ERA5L_"

# ee.Initialize()
ee.Initialize(opt_url='https://earthengine-highvolume.googleapis.com')

# region = ee.Geometry.Rectangle(28.75, 108.5, 33.5, 116.25)
region = ee.Geometry.Rectangle(108.45, 28.75, 116.25, 33.55)

def ee_col_download_year(region, col_id='ECMWF/ERA5_LAND/HOURLY',
                         year=2022, save=False, prefix=""):

    fout = prefix + col_id.replace("/", "_") + "_" + str(year) + ".nc"
    if os.path.isfile(fout):
        return
    
    ic = (ee.ImageCollection(col_id)
          # .filterDate('2000-01-01', '2023-01-01')
          .filter(ee.Filter.calendarRange(year, year, 'year'))
          .select(bands)
        )
    print(fout)
    print(ic.size().getInfo())

    ds = xarray.open_dataset(
        ic,
        engine='ee',
        projection=ic.first().select(0).projection(),
        geometry=region
    )
    if save:
        ds.to_netcdf(fout)
    ds


def ee_col_download_years(region, col_id='ECMWF/ERA5_LAND/HOURLY',
                          year_beg=2022, year_end=2022, save=False, prefix=""):

    # for year in range(year_beg, year_end + 1):
    for year in range(year_end, year_beg - 1, -1):
        try:
            ee_col_download_year(region, col_id, year, save, prefix)
        except Exception as e:
            print(str(e))

# range = c(113.5, 115, 29.75, 31.5)
# region = ee.Geometry.Rectangle(113.5, 29.75, 115, 31.5)
# 108.52083  28.99917 116.06833  33.24833
# ee_col_download_year(region, year=2000, save=True)
ee_col_download_years(region, year_beg=2013,
                      year_end=2024, save=True, prefix=prefix)
