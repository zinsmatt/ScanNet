import os
import glob
import subprocess

folders = list(filter(os.path.isdir, glob.glob("/media/mzins/DATA1/ScanNet/scans/*")))
print(len(folders), "sequences")

for f in folders[::100]:
    name = os.path.splitext(os.path.basename(f))[0]
    filename = os.path.join(f, name + ".sens")
    cmd = ["python2", "reader.py", "--filename", filename, "--output_path test", "--export_color_images"]
    os.system(" ".join(cmd))
    print("==========>", name, "done.")
