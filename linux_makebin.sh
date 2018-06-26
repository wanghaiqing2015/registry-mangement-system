#!/bin/bash

rm -rf build/
rm -rf dist/
pyinstaller3  --clean rms.py  --add-data static:static --add-data templates:templates --additional-hooks-dir=.  
rm -rf build/


rm -rf packages.tar.gz
 
tar zcvf packages.tar.gz rms.service dist/rms/  

cat linux_install.sh packages.tar.gz > rms-tool.sh

chmod +x rms-tool.sh

rm -rf packages.tar.gz
