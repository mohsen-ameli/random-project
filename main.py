import numpy as np

AIR_DENSITY = 1.204 # kg/m3
STEEL_DENSITY = 7850 # kg/m3

# r: radius of the sphere
def volume(r: float) -> float:
    return 4/3 * np.pi * r**3

# f: force
# m: mass
def acceleration(f: float, m: float) -> float:
    return f / m

if __name__ == '__main__':
    radius = float(input('Enter the radius of the sphere (in meters): '))
    crust = float(input('Enter the thickness of the crust (in meters): '))
    # the radius of the sphere includes the crust

    mass_of_steel_crust = 7850 * (volume(radius) - volume(radius - crust))
    mass_of_air_sphere = 1.204 * volume(radius - crust)

    print(f"Mass of the steel crust: {mass_of_steel_crust/1000:0.0f} ton")
    print(f"Mass of the air sphere: {mass_of_air_sphere/1000:0.0f} ton")