cat >  ./Dockerfile << EOF
FROM frolvlad/alpine-glibc
MAINTAINER whq <krman@163.com>

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories
RUN apk add --update-cache bash  
RUN rm -rf /var/cache/apk/* 
COPY ./dist/rms  /rms
WORKDIR /rms
 
EXPOSE 15000
CMD /rms/rms
EOF

rm -rf build/
rm -rf dist/
pyinstaller3  --clean rms.py  --add-data static:static --add-data templates:templates --additional-hooks-dir=. 
rm -rf build/

rm -rf rms-latest.tar
 
docker stop rms
docker rm -f rms
docker rmi rms:latest

docker rmi index.tenxcloud.com/krman/rms:latest

docker build -t rms   .
docker images
docker save -o rms-latest.tar rms:latest
 
docker tag rms:latest index.tenxcloud.com/krman/rms:latest
docker push index.tenxcloud.com/krman/rms:latest
if [ $? -eq 0 ]; then
    echo -e "\033[42;37;5m镜像推送成功\033[0m"
else
    echo -e "\033[41;37;5m镜像推送失败\033[0m"
fi

docker run -itd  --restart=always --name rms -p 15000:15000 index.tenxcloud.com/krman/rms:latest

