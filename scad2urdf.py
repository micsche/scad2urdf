#!/usr/bin/env python

import os
import string


filepath = 'walker.scad'
printable = set(string.ascii_letters)
names = []

urdfout = 'robot.urdf'
robotname = "pointone"

wf = open(urdfout , "w")
wf.write('<?xml version="1.0" encoding="utf-8"?>\n')
wf.write('<robot name="'+robotname+'">\n')
wf.write('\n')

def write_join(joins):
    [par,child] = joins
    par = "".join(par.split())
    child = "".join(child.split())
    wf.write('<joint name="'+par+"2"+child+'" type="revolute">\n')
    wf.write('<parent link="'+par+'"/>\n')
    wf.write('<child link="'+child+'"/>\n')
    wf.write('</joint>\n')
    wf.write('\n')

def write_link(linkname, trans,rgb,filename_stl):
    #linkname = filename_stl.split('.')[0]

    wf.write('<link name="'+linkname+'">\n')
    wf.write('<visual>\n')
    wf.write(' <origin rpy="0 0 0" xyz="'+trans[0]+' '+trans[1]+' '+trans[2]+'"/>\n')
    wf.write('  <geometry>\n')
    wf.write('    <mesh filename="'+filename_stl+'"/>\n')
    wf.write('  </geometry>\n')
    wf.write('  <material name="">\n')
    wf.write('    <color rgba="'+rgb[0]+' '+rgb[1]+' '+rgb[2]+' 1"/>\n')
    wf.write('  </material>\n')
    wf.write('</visual>\n')
    wf.write('<collision>\n')
    wf.write('  <origin rpy="0 0 0" xyz="'+trans[0]+' '+trans[1]+' '+trans[2]+'"/>\n')
    wf.write('  <geometry>\n')
    wf.write('    <mesh filename="'+filename_stl+'"/>\n')
    wf.write('  </geometry>\n')
    wf.write('</collision>\n')
    wf.write('<inertial>\n')
    wf.write('  <mass value="4"/>\n')
    wf.write('  <origin rpy="0 0 0" xyz="0 0 0"/>\n')
    wf.write('  <inertia ixx="0.0216667" ixy="0" ixz="0" iyy="0.0216667" iyz="0" izz="0.0240667"/>\n')
    wf.write('</inertial>\n')
    wf.write('</link>\n')
    wf.write('\n')

with open(filepath) as fp:
    s = 0
    p = 0
    line = " "
    outline = ""
    idio = 0
    while line:
        a = line.count("{") - line.count("}")
        s = s + a

        if line.startswith("//"):

            if "join" in line:
                joins = line.strip().split(":")[1].split(',')
                write_join(joins)
            myname = ''.join(filter(lambda x: x in printable, line))



        if ("translate" in line) and (s==0):
            trans=(line.split('[')[1].split(']')[0].split(','))
            line = "translate([0,0,0])"

        if "color" in line:
            rgb=(line.split('[')[1].split(']')[0].split(','))

        outline = outline + line

        if s==0 and p==1:

            if myname == None:
                filename_scad = str(idio)+"mesh.scad"
                filename_stl = str(idio)+"mesh.stl"

            else:
                if myname in names:
                    filename_scad = myname + str(idio) + ".scad"
                    filename_stl  = myname + str(idio) + ".stl"
                    filename_stlout = myname + str(idio) + "2.stl"
                    linkname = myname + str(idio)
                else:
                    filename_scad = myname + ".scad"
                    filename_stl  = myname + ".stl"
                    filename_stlout = myname + "2.stl"
                    linkname = myname
                    names.append(myname)

                myname = None

            idio = idio + 1

            f = open(filename_scad, "w")
            f.write(outline)
            f.close()

            os.system("openscad "+filename_scad+" -o "+filename_stl)
            os.system("meshlabserver -i "+filename_stl+" -o "+filename_stlout)
            os.system("rm "+filename_stl)
            os.system("rm "+filename_scad)

            write_link(linkname, trans,rgb,filename_stlout)

            outline = ""
        p=s
        line = fp.readline()


wf.write("</robot>\n")
wf.close()
