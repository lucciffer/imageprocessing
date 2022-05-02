sudo apt install libzbar0 -y
wget https://exiftool.org/Image-ExifTool-12.40.tar.gz
gzip -dc Image-ExifTool-12.40.tar.gz | tar -xf -
cd Image-ExifTool-12.40
perl Makefile.PL
make test
sudo make install
pip install pyexiftool
sudo apt install libzbar0
pip install zbar pysolar 
pip install requests packaging pytest-xdist pyzbar mapboxgl jenkspy rawpy imageio gdal 
