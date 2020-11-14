//link: bit1
translate([0,0,0])
{
    union()
    {
        color([1,1,0])
        cube([0.1,0.1,1]);
    }
}

//link: bitb
translate([0,0,1.2])
{
    color([1,0,0])
    union()
    {
        cube([0.1,0.1,1]);
    }
}

//join: bit1,bitb
translate([0,0,1])
{
    rotate([90,0,0])
    color([0,0,1])
    cylinder(r=0.1,h=0.1);
}
