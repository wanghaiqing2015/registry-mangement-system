cat >  ./Dockerfile << EOF
FROM frolvlad/alpine-glibc
MAINTAINER whq <krman@163.com>

RUN apk add --update bash --repository http://mirrors.ustc.edu.cn/alpine/v3.7/main/ --allow-untrusted
RUN rm -rf /var/cache/apk/* 
COPY ./dist/rms  /rms
COPY ./static/  /rms/static
COPY ./templates/  /rms/templates
WORKDIR /rms
 
EXPOSE 15000
CMD /rms/rms
EOF

rm -rf build/
rm -rf dist/
pyinstaller3  --clean rms.py  --additional-hooks-dir=. 
rm -rf build/

rm -rf rms-latest.tar
docker rm -f rms
docker rmi rms 

docker build -t rms   .
docker images
docker save -o rms-latest.tar rms:latest
 
docker tag rms:latest index.tenxcloud.com/krman/rms:latest
docker push index.tenxcloud.com/krman/rms:latest

docker run -itd  --restart=always --name rms -p 15000:15000 index.tenxcloud.com/krman/rms:latest

