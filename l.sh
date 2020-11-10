rm -f *.proto
rm -f ../mmb/protos/*.proto

./scad2urdf.py
python -m urdf2webots.importer --input=robot.urdf

mv  *.proto ../mmb/protos
rm *.stl
