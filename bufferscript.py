import arcpy
arcpy.env.workspace = "D:/working_temp/Eric/Learning/StandaloneScriptArcPy/Project.gdb"
# Set the spatial reference if needed
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference('WGS 1984')
input_fc = "Points"
output_folder = 'D:/working_temp/Eric/Learning/StandaloneScriptArcPy/output_folder'
output_shapefile = 'buffered_points.shp'
buffer_distance = '10 Miles' # Change as needed

# Construct the full path to the output shapefile
output_shapefile_path = arcpy.os.path.join(output_folder, output_shapefile)

# Apply the buffer
arcpy.Buffer_analysis(input_fc, output_shapefile_path, buffer_distance)
print("complete")