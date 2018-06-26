#!/bin/bash
set -x
 
sed -n -e '1,/^exit 0$/!p' $0 > "packages.tar.gz" 2>/dev/null
 
rm -rf packages
mkdir packages
tar xzf packages.tar.gz -C packages/

systemctl stop rms 
systemctl disable rms 
rm -rf /opt/rms/
 
cp -r packages/dist/rms    /opt/rms
# cp -r packages/static      /opt/rms
# cp -r packages/templates   /opt/rms
 
cp -rf packages/rms.service /usr/lib/systemd/system/
chmod 755 -R /usr/lib/systemd/system/rms.service

systemctl daemon-reload
systemctl enable rms
systemctl start  rms    
systemctl status rms  

rm -rf packages.tar.gz
rm -rf packages/
 
# exit 0 下面必须有一个空行， 而且不能有任何内容
exit 0
