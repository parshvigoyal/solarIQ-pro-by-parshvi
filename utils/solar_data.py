from pvlib.iotools import get_pvgis_hourly
import requests


def get_pvgis_irradiance(lat, lon):

    # Choose PVGIS database according to location coverage
    if 24 <= lat <= 50 and -125 <= lon <= -66:
        raddatabase = 'PVGIS-NSRDB'

    elif -60 <= lat <= 65 and -25 <= lon <= 45:
        raddatabase = 'PVGIS-SARAH'

    else:
        # Global fallback database
        raddatabase = 'PVGIS-ERA5'

    try:

        data, meta = get_pvgis_hourly(
            latitude=lat,
            longitude=lon,
            start=2015,
            end=2015,

            # PVGIS database
            raddatabase=raddatabase,

            # Automatically optimize tilt
            surface_tilt=0,
            optimal_surface_tilt=True,

            # South-facing panels
            surface_azimuth=180,

            # Enable PV calculation
            pvcalculation=True,

            # Base 1 kWp simulation
            peakpower=1,

            # Crystalline silicon panels
            pvtechchoice='crystSi',

            # Freestanding installation
            mountingplace='free',

            # Practical system losses
            loss=10,

            # Fixed tilt system
            trackingtype=0,

            optimalangles=False,

            url='https://re.jrc.ec.europa.eu/api/v5_2/'
        )

        # Extract irradiance safely
        if 'poa_global' in data.columns:
            irradiance = data['poa_global'].sum()

        elif 'E' in data.columns:
            irradiance = data['E'].sum()

        else:
            irradiance = (
                data
                .select_dtypes(include='number')
                .sum()
                .max()
            )

        # Convert Wh → kWh
        annual_irradiance_kwh = irradiance / 1000

        return annual_irradiance_kwh

    except requests.HTTPError as e:

        print(f"PVGIS API error: {e}")
        return None

    except Exception as e:

        print(f"Unexpected PVGIS error: {e}")
        return None
