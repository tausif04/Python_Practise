# Creating Zip File
import zipfile
with zipfile.ZipFile("my_archive.zip", "w") as zipf:
    zipf.write("example.txt")
    zipf.write("large_file.txt")

# Extract from Zip File
zip_file_path = "my_archive.zip"
with zipfile.ZipFile(zip_file_path, "r") as zipf:
    zipf.extractall()
    extracted_files = zipf.namelist()
    print("Extracted files:", extracted_files)

# Make Zip Form Directory
import shutil
# Specify the directory to be zipped
directory_to_zip = "demo"
# The name of the output zip file (without extension)
output_zip_name = "demo_archive"
# Create a zip archive
shutil.make_archive(output_zip_name, 'zip', directory_to_zip)
print(f"Directory '{directory_to_zip}' has been zipped into '{output_zip_name}.zip'")