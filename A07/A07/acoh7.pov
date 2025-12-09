#include "colors.inc"
#include "babel_povray3.inc"
#include "molecule.pov"

// Define PI
#declare MyPi = 3.1415926535;

// Camera
camera {
    location <0, 20, -35>
    look_at <0, 0, 0>
}

// Light
light_source {
    <50, 80, -60>
    color rgb <1,1,1>
}

// Radius of heptagon
#declare R = 10;

// Draw molecules around a circle
#declare k = 0;
#while (k < 7)

    #declare X = R*cos(2*MyPi*k/7);
    #declare Z = R*sin(2*MyPi*k/7);

    object {
        mol_0
        translate <X, 0, Z>
        rotate <0, -360*k/7, 0>
    }

    #declare k = k + 1;
#end

