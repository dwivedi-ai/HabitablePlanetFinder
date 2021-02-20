pi = 3.14159265359
au = 1.496*(10**11) # In meters
stefan_Boltzmann = 5.67 * (10**-8) # In Wm^-2K^-4
# Range of temperature for liquid water to exist = 192K-295K.

print("Welcome to habitable planet finder.")
print("Enter the following details.\n")

starx = float(input("Enter the value of star's luminosity (The x value of the number x*10^n): "))
starn = float(input("Enter the value of the star's luminosity (The n value of the number x*10^n): "))

starLuminosity = starx * (10**starn)

gravityx = float(input("Enter the value of the star's gravitational parameter(The x value for the number x*10^n): "))
gravityn = float(input("Enter the value of the star's gravitational parameter(The n value for the number x*10^n): "))

gravitationalParam = gravityx * (10**gravityn)

bondAlbedo = float(input("Enter the value of the Planetary Bond Albedo: "))

rInner = (((1-bondAlbedo)*starLuminosity)/(16*pi*stefan_Boltzmann*(295**4)))**0.5
rInner = rInner / au

rOuter = (((1-bondAlbedo)*starLuminosity)/(16*pi*stefan_Boltzmann*(192**4)))**0.5
rOuter = rOuter / au

time = float(input("Enter the time period in days: "))

time = time*24*60*60

a = (gravitationalParam*((time/(2*pi))**2))**(1/3)
a = a / au

print("The distance of your planet from the star is %.3f"%a," AU")

if (a<rOuter and a>rInner):
    print("Your planet is habitable")
else:
    print("Your planet is not habitable")

print("The habitable lies between %.3f"%rInner," AU - %.3f"%rOuter," AU")