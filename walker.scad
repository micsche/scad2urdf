// CSG.scad - Basic example of CSG usage

//rightfemur
translate([0,-0.24,0])
{
    color([1,0,0])
    union() {
     cube([0.05,0.05,0.30]);

    rotate([90,0,0]) {
        translate([0.025,0,-0.025]) {
        cylinder(h=0.05,r=0.05,center=true);
        }
        }


    rotate([90,0,0]) {
        translate([0.025,0.30,-0.025]) {
        cylinder(h=0.05,r=0.05,center=true);
        }
        }

}
}

//rightthigh
translate([0,-0.19,0.30])
{
    color([1,0,0])
    union() {
    cube([0.05,0.05,0.30]);

    rotate([90,0,0]) {
        translate([0.025,0,-0.025]) {
        cylinder(h=0.05,r=0.05,center=true);
        }
        }


    rotate([90,0,0]) {
        translate([0.025,0.30,-0.025]) {
        cylinder(h=0.05,r=0.05,center=true);
        }
        }
    }
}

///rightfoot
translate ([0.025,-0.24,0])
{
    color([0,0,1])
    rotate([90,0,0]) {
    union()
    {
        cylinder(h=0.05,r=0.05);
        translate([-0.10,-0.05,0]) {
        cube([0.35,0.02,0.25]);
        }
        translate([-0.05,-0.05,0]) {
            cube([0.10,0.05,0.05]);
        }
    }
}
}


//leftfemur
translate([0,0.24,0])
{
    color([0,1,0])
    union() {
    cube([0.05,0.05,0.30]);

    rotate([90,0,0]) {
        translate([0.025,0,-0.025]) {
        cylinder(h=0.05,r=0.05,center=true);
        }
        }


    rotate([90,0,0]) {
        translate([0.025,0.30,-0.025]) {
        cylinder(h=0.05,r=0.05,center=true);
        }
        }
    }
}

//leftthigh
translate([0,0.19,0.30])
{

    union() {
    cube([0.05,0.05,0.30]);

    rotate([90,0,0]) {
        translate([0.025,0,-0.025]) {
        cylinder(h=0.05,r=0.05,center=true);
        }
        }


    rotate([90,0,0]) {
        translate([0.025,0.30,-0.025]) {
        cylinder(h=0.05,r=0.05,center=true);
        }
        }
    }
}

//leftfoot
translate ([0.025,0.34,0])
{
    color([0,1,0])
    rotate([90,0,0]) {
    union()
    {
        cylinder(h=0.05,r=0.05);
        translate([-0.10,-0.05,-0.20]) {
        cube([0.35,0.02,0.25]);
        }
        translate([-0.05,-0.05,0]) {
            cube([0.10,0.05,0.05]);
        }
    }
}
}

//hip
translate([0,-0.01,0])
{
    color([0.3,0.3,0.5])
    union()
    {
        translate([0.025,0.20,0.60])
        {
            rotate([90,0,0])
            {
                cylinder(h=0.05,r=0.04);
            }
        }
        translate([0.025,-0.08,0.60])
        {
            rotate([90,0,0])
            {
                cylinder(h=0.05,r=0.04);
            }
        }
        translate([-0.30,-0.11,0.62])
        {
            cube([0.60,0.28,0.03]);
        }

    }

}

//join: hip,rightthigh
translate([0.025,-0.15,0.60])
{
    color([0.5,0.5,0.5]);
    union()
    {
        translate([0.0,0.0,0.0])
        {
            rotate([90,0,0])
            {
                cylinder(h=0.1,r=0.01);
            }
        }
    }
}

//join: hip,leftthigh
translate([0.025,0.28,0.60])
{
   color([0.5,0.5,0.5]);
    union()
    {
        translate([0.0,0.0,0.0])
        {
            rotate([90,0,0])
            {
                cylinder(h=0.1,r=0.01);
            }
        }
    }
}

//join: rightthigh,rightfemur
//join: leftthigh,leftfemur
//join: rightfemur,rightfoot
//join: leftfemur,leftfoot
