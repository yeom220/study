# Production 배포시 고려사항

- Production에는 바운드 마운트를 사용하지 않는다.
- 컨테이너 애플리케이션은 Build 과정이 필요하다.
- 멀티 컨테이너 프로젝트는 여러 호스트/리모트 머신들로 분리될 수 있다.
- 배포 프로세스를 단순화 해주는 솔루션에 대해 알아본다.

---
# 바인드 마운트, 볼륨 & 카피

>**개발 환경 특징**
>- 개발 환경에서는 런타임 환경을 캡슐화 해야 하지만, 소스 코드 캡슐화는 필수가 아니다.
>- 바인드 마운트를 통해 컨테이너에 호스트 머신의 프로젝트 파일을 전달할 수 있다.
>- 개발 편의를 위해 컨테이너의 재시작 없이 애플리케이션이 업데이트 되도록 허용한다.
>
>**운영 환경 특징**
>- 운영 환경에서는 소스 코드가 원격 머신에는 없기 때문에 컨테이너는 단독으로 동작 되어야 한다.
>- `COPY` 명령어를 통해 코드 스냅샷을 이미지에 복사하여야 한다.
>- 모든 이미지는 어떤 외부 코드나 환경설정 없이 동작이 되어야 한다.
>- 이미지/컨테이너는 단일 구성으로 동작 가능한 소스여야 한다.

![[bind_mounts_volumes_copy.png]]

---
# 단일 애플리케이션 구성 예시

![[standalone_nodejs_app.png]]

---
# 서버 직접 관리 VS 호스팅 프로바이더 솔루션

### 직접 관리하는 서버(예: EC2) 배포 단점
- 서버의 모든 것을 관리해야 하는 책임이 있다.
	- 필수 소프트웨어 최신화 유지
	- 네트워크, 방화벽 관리
	- 보안 이슈 관리
	- 트래픽 변동에 따라 서버 가용성 관리
	- 모니터링
- SSH 접속 후 직접 관리하는 불편함.

### 호스팅 프로바이더 솔루션(예: ECS) 특징
- 서버의 모든 것을 프로바이더가 관리 한다.(애플리케이션 제외)
	- 서버 생성
	- 소프트웨어 업데이트
	- 보안 이슈 관리
	- 트래픽 변동에 따른 서버 가용성
	- 모니터링

---
### 도커, ECS, MongoDB Atlas 활용한 애플리케이션 구조

![[cloud_app_architecture.png]]

---
# 도커 멀티 스테이지 빌드

>하나의 `Dockerfile` 에 여러 빌드 및 셋업을 구성할 수 있다. (Stages)
>스테이지는 서로 생성된 파일들을 복사할 수 있다.
>또한 이미지를 빌드할 때 모든 스테이지 뿐만 아니라, 특정 스테이지만 빌드도 가능하다.

**React 빌드 및 배포 Dockerfile**
```dockerfile
FROM node:14-alpine as build

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

RUN npm run build

FROM nginx:stable-alpine

COPY --from=build /app/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```
- `FROM node:14-alpine as build`
	- `FROM` 명령어는 베이스 이미지를 불러올 뿐 아니라 Dockerfile 내부에서 스테이지 분기점이 된다.
	- 다음 `FROM` 명령어 이전(`FROM ngnix...`)까지 `build` 스테이지이다.
- `COPY --from=build /app/build /usr/share/nginx/html`
	- `COPY` 명령어는 호스트 머신에서 파일을 복사하지만 `--from=build` 옵션을 줄 경우 `build` 스테이지를 가리킨다.
	- `build` 스테이지의 `/app/build` 디렉토리를 `FROM nginx...` 스테이지의 `/usr/share/nginx/html` 에 복사한다.

**특정 스테이지만 빌드**
```bash
$ docker build --target build .
```
- `--target build`
	- `--target` 옵션은 스테이지 지정 옵션으로 `build` 스테이지만 빌드를 진행한다.

---
