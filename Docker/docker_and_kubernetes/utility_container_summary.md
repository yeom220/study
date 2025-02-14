# 유틸리티 컨테이너란 ?

>애플리케이션 컨테이너는 애플리케이션과 애플리케이션을 실행하는 환경이 포함되어 있다.
>유틸리티 컨테이너는 특정 환경만 포함하는 컨테이너를 의미한다.
>이는 컨테이너(환경)을 실행할 때 애플리케이션을 시작하지 않는 것을 뜻한다.
>대신 특정 작업을 실행하기 위해 지정한 명령과 함께 실행한다.
>유틸리티 컨테이너의 장점은 특정 작업(예시: Node, Java, PHP, Phtyon 등..)을 위한 패키지를 컨테이너에 설치함으로써 호스트 머신을 깔끔하게 유지할 수 있다.

![[utility_containers.png]]

---
# Linux Utility Containers 권한 이슈

>Docker 데몬은 **root** 권한으로 실행되어 유틸리티 컨테이너에서 생성된 파일의 권한이 **root** 로 지정되는 이슈가 있다.
>이 문제를 해결할 수 있는 방법은 컨테이너의 리눅스 uid:gid 를 호스트 머신의 사용자 유저와 일치 시키는 방법이다.
>
>**솔루션 1: 사전 정의된 "node" 사용자 사용 (운이 필요)**
>>공식 Node.js 도커 컨테이너는 "node" 라는 사용자를 제공한다.
>```dockerfile
>FROM debian:name=slim
>RUN groupadd  --gid 1000 node \
>&& useradd --uid 1000 --gid node --shell /bin/bash --create-home node
>```
>>호스트 사용자 계정의 uid:gid 가 1000으로 일치한다면 Node Docker 이미지에서 정의한 "node" 사용자와 매핑 된다.
>>컨테이너는 기본적으로 "root" 계정으로 실행되므로 "node" 계정으로 실행되도록 Dockerfile에 명령을 추가한다.
>```dockerfile
>FROM node:14-slim
>USER node
>WORKDIR /app
>```
>>이미지를 빌드 후 `npm init` 을 실행하면 `package.json` 파일이 호스트 사용자 권한으로 생성된다.
>
>**솔루션 2: 사전 정의된 "node" 사용자를 제거하고 호스트 사용자를 추가**
>```dockerfile
>FROM node:14-slim
>RUN userdel -r node
>ARG USER_ID
>ARG GROUP_ID
>RUN addgroup --gid $GROUP_ID user
>RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user
>USER user
>WORKDIR /app
>```
>>이후 이미지 빌드시에 사용자 계정을 넘긴다.
>```bash
>$ docker build -t node-util --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g) .
>```
>>이미지 빌드 후 `npm init` 을 실행하면 파일이 ARG로 넘긴 사용자 권한으로 생성된다.
>>이 이미지는 이식(portable)할 수 없지만 유틸리티 컨테이너 목적을 위해서는 문제가 되지 않는다.






