# 도커가 필요한 이유

1. 개발 환경과 운영 환경의 의존성(환경) 차이 문제를 해결
2. 각 팀과 회사마다 다른 개발 환경에서 발생하는 의존성 차이 문제 해결
3. 각 프로젝트마다 다른 툴과 버전에서 발생하는 충돌 문제 해결
4. 공유, 재구축, 배포가 간단함
5. **단일 구성 파일로 공유 가능**

---
# 버츄얼 머신의 장단점

### 장점

- 분리(독립)된 환경
- 각각 격리된 환경 구성 가능
- 환경 구성의 안정적인 공유 및 재생산 가능

### 단점

- 새로운 버츄얼 머신을 설치할 때마다 중복 복제로 리소스를 낭비
- 성능이 느려질 수 있음
- 재생산 및 공유가 가능해도 원하는 모든 시스템에 버츄얼 머신을 설정하고 동일한 환경을 구성해야 함
- **단일 구성 파일로 공유 불가능**

---
# 컨테이너 vs 버츄얼 머신

### 컨테이너

- 컨테이너는 최소한의 OS 구성으로 빠르며, 적은 디스크를 점유
- 공유, 재구축, 배포가 간단
- **전체 머신(OS) 환경 대신, 애플리케이션 및 필요 환경(의존성)만 캡슐화**

### 버츄얼 머신

- 많은 OS 구성요소가 필요하여 속도가 느리며, 많은 디스크를 점유
- 공유, 재구축, 배포가 가능하지만 과정이 복잡함
- **애플리케이션 및 필요 환경뿐만 아니라, 전체 머신(OS) 환경을 포함하여 모두 캡슐화 한다**

---
# 도커 Playground

>브라우저에서 도커를 실행해주는 사이트
>https://labs.play-with-docker.com/

---
# 이미지 vs 컨테이너

### 이미지

- 코드와 코드를 실행하는데 필요한 도구(환경)를 패키징한 것
- 모든 설정 명령과 코드가 포함된 공유 가능한 패키지
- 이미지를 기반으로 다른 시스템과 서버에서 여러 번 실행 가능

### 컨테이너

- 이미지의 구체적인 실행 인스턴스
- 외부와 격리된 실행 애플리케이션

---
# [Docker Hub](https://hub.docker.com/)

>Docker 이미지를 저장하고 배포할 수 있는 클라우드 기반 레지스트리 서비스.
>개발 및 배포 프로세스를 단순화하고, 컨테이너화 된 애플리케이션을 공유하기 위해 사용된다.

### 주요 기능

1. 이미지 저장소
	- Docker 이미지를 저장, 관리, 배포할 수 있는 중앙 저장소
	- Public 또는 Private 저장소를 제공하며, Public 저장소는 무료
2. 공식 이미지 제공
	- Official 이미지를 제공하여 신뢰할 수 있는 베이스 이미지를 사용 가능
	- 예: `node`, `nginx`, `python` 등...
3. 이미지 검색
	- 다양한 오픈소스 및 커뮤니티 이미지를 검색하여 사용 가능
4. 공유 및 협업
	- 이미지를 공유하거나 다른 개발자가 만든 이미지를 가져다 사용 가능
	- 이미지를 **Push** 하거나 **Pull** 하는 방식으로 관리

---
# Dockerfile

>Dockerfile은 도커 이미지를 생성하기 위한 스크립트 파일로, 이미지 빌드 과정과 컨테이너 환경을 정의.
>Docker는 Dockerfile에 따라 이미지를 빌드하고, 그 결과로 애플리케이션이 실행되는 컨테이너를 생성.

**node 베이스 이미지 기반 Express.js 를 실행하는 Dockerfile**
```dockerfile
FROM node

WORKDIR /app

COPY . /app

RUN npm install

EXPOSE 80

CMD [ "node", "server.js" ]
```

- `FROM node`
	- `node` 이미지를 베이스 이미지로 지정
	- 도커 이미지는 기존 이미지 위에 쌓이는 방식으로 빌드되므로 베이스 이미지가 필요
- `WORKDIR /app`
	- 컨테이너 내부의 작업 디렉터리 설정
	- 리눅스 **`cd`**(chage directory) 같은 명령어
- `COPY . /app`
	- 호스트 머신의 파일(디렉토리)을 컨테이너 내부로 복사하는 명령어
	- 호스트 머신의 현재 디렉토리 파일(디렉토리)을 컨테이너 `/app` 경로에 복사
- `RUN npm install`
	- 이미지 빌드 과정에서 실행되는 명령어
	- 주로 패키지 설치 등의 환경 구성에 사용
- `EXPOSE 80`
	- 컨테이너에서 외부(호스트 머신)로 노출할 포트 표기
	- **사용할 포트를 나타낼 뿐 실제로 호스트 머신과 연결하지는 않음**
- `CMD [ "node", "server.js" ]`
	- 컨테이너 생성할 때 실행되는 명령어
	- 단일 명령어만 정의 가능

---
# Dockerfile 기반 커스텀 이미지 및 컨테이너 생성

>Docker 커스텀 이미지 생성

```bash
$ docker build .
```

- `build`
	- Dockerfile 기반으로 이미지를 생성하는 명령어
	- **`.`은 Dockerfile이 있는 경로를 뜻하며, 해당 경로가 Dockerfile의 빌드 컨텍스트 경로(context)**
- `build -t {Image name}`
	- `-t` 는 `--tag` 옵션의 약자로 이미지 이름을 지정할 때 사용한다.

>Docker 컨테이너 생성 및 실행

```bash
$ docker run {Image ID}
```

- `run {Image ID}`
	- 이미지 기반으로 컨테이너를 생성하는 명령어
	- 컨테이너 생성 및 Attatch mode(포그라운드) 실행
	- `{Image ID}`의 일부 문자로도 실행 가능 (고유 식별자 인 경우)

>**위 명령어 실행시 컨테이너는 생성되지만 접속이 되지 않는다.**
>그 이유는 **컨테이너는 격리된 환경으로 `-p` (publish) 옵션을 통해 외부(호스트 머신)로 노출(연결)해야 한다.**
>호스트 머신 8080 포트로 위의 애플리케이션에 접속하려면 아래와 같이 실행해야 한다.

```shell
$ docker run -p 8080:80 {Image ID}
```

---
# Docker 이미지 특징

### 블루프린트(읽기 전용)

>소스 코드를 수정 후 컨테이너를 다시 실행해도 변경 사항은 적용되지 않는다.
>그 이유는 이미지는 `build` 시점에 `Dockerfile` 에 명시된 대로 소스 코드를 컨테이너 내부로 복사하기 때문이다.
>즉, `build` 이후에 소스를 수정하여도 이미지에 저장된 코드는 변경되지 않기 때문에 적용되지 않는다.
>변경한 소스 코드를 적용하려면 이미지를 다시 빌드 해야 한다.

### 레이어 기반 아키텍처

>Docker는 이미지를 생성할 때 각각의 명령을 이미지로 만들어 쌓는다. (Layer)
>Docker는 이미지를 재생성할 때 각 명령(이미지 레이어)을 확인하여 변경 사항이 없는 경우 기존 이미지 레이어를 재사용(캐싱)하여 이미지 재생성을 최적화 한다.

![[image_layers_schematic_diagram.png]]
- 이미지 레이어 도식도

![[container_layers_schematic_diagram.png]]
- 컨테이너 레이어 도식도

---
# 컨테이너와 상호작용(인터렉티브 모드)


**python 베이스 이미지 기반 파이썬 코드를 실행하는 Dockfile**
```dockerfile
FROM python

WORKDIR /app

COPY . /app/

CMD ["python", "rng.py"]
```

>파이썬 애플리케이션 이미지 생성

```bash
$ docker build .
```

>컨테이너는 기본적으로 격리된 환경이기 때문에 상호작용 되지 않는다.
>상호 작용을 위해서는 컨테이너를 생성할 때 상호작용을 할 수 있도록 옵션을 주어야 한다.

```bash
$ docker run -it {Image ID}
```

- `run -i`
	- `--interactive` 옵션의 약자로 컨테이너에 입력이 가능하도록 하는 옵션(**STDIN**)
- `run -t`
	- `--tty` 옵션의 약자로 입력을 위한 터미널을 생성

>위의 파이썬 애플리케이션은 출력 후에 종료되기 때문에 컨테이너도 같이 종료된다.
>종료된 컨테이너를 다시 실행하는 명령어는 아래와 같다.

```bash
$ docker start -ia {Container ID}
```

- `start -a`
	- `--attach` 옵션 약자로 표준출력(**STDOUT**)과 표준에러(**STDERR**) 출력

---
# 컨테이너 및 이미지 제거

>컨테이너 제거

```bash
$ docker rm {Container ID}
```

- `rm {Container ID}`
	- 컨테이너 제거 명령어로 중지된 컨테이너만 제거 가능
	- 컨테이너를 생성할 때 `--rm` 옵션을 주면 컨테이너가 중지 되었을 때 자동 제거된다.
		- `$ docker run --rm {Container ID}`

>중지된 컨테이너 모두 제거

```bash
$ docker container prune
```

- `container prune`
	- 중지된 컨테이너 모두 제거

>이미지 제거

```bash
$ docker rmi {Image ID}
```

- `rmi {Image ID}`
	- 이미지 제거 명령어로 사용되지 않은 이미지(컨테이너화 되지 않은)만 제거 가능
	- `Image ID` 로 생성된 컨테이너가 있는 경우 제거 불가

>태그 되지 않거나 대체된 이미지 모두 제거

```bash
$ docker image prune
```

- `image prune`
	- `tag` 가 없거나 대체된 이미지 모두 제거
- `image prune -a`
	- 사용되지 않은 이미지(컨테이너화 되지 않은) 모두 제거

---
# 컨테이너 파일 복사

>호스트 -> 컨테이너로 파일 복사

```bash
$ docker cp ./copy_dir {Container ID}:/
```

- `cp`
	- 복사 명령어
	- 중지된 컨테이너도 복사 가능
- `./copy_dir`
	- 복사할 디렉토리 경로(호스트 머신)
	- `./copy_dir` 에 있는 모든 파일을 복사
	- 특정 파일만 복사할 경우 `{Path}/{File name}` 
- `{Container ID}:/`
	- `{Container ID}`는 복사할 컨테이너
	- `:/` 는 해당 컨테이너의 복사할 경로

>컨테이너 -> 호스트로 파일 복사

```bash
$ docker cp {Container ID}:/copy_dir/text.txt ./from_con
```

- `{Container ID}:/copy_dir/text.txt`
	- 복사할 파일 경로 (컨테이너)
- `./from_con.txt`
	- 복사한 파일을 생성할 경로 (호스트 머신)
	- 파일을 복사한 경우 `from_con` 이름으로 파일 생성
	- 디렉토리를 복사한 경우 `from_con` 이름으로 디렉토리 및 내부 파일 생성

---
# 이미지 태그

>이미지는 `name` 과 `tag` 로 구성된다.
>`name` 은 이미지 그룹이고,  `tag` 는 해당 이미지의 특정 버전이나 타입 등을 나타낸다.

```bash
$ docker run node:23-alpine
```

- `node:23-alpine`
	- `node` 는 `name`
	- `:23-alpine` 은 `tag` 로 노드 23 버전의 알파인(경량화된 리눅스) 이미지를 지정
	- `name` 만 지정하는 경우는 `node:latest` 와 동일 (최신 버전)

---
# 볼륨(Volumes)

>볼륨은 도커가 설치된 호스트 머신에 있는 디렉토리로서, 도커 컨테이너 내부의 디렉토리에 매핑 된다.
>컨테이너는 호스트 머신과 다른 독립적인 파일 시스템을 사용한다. (격리)
>컨테이너에서 생성된 파일들은 호스트 머신에 저장되지 않는다.
>따라서 컨테이너가 제거되면 해당 파일들도 같이 제거된다.
>도커 볼륨은 컨테이너가 제거되어도 유지해야 할 파일들을 유지할 수 있도록 한다.

```bash
$ docker run -v {Volume name}:{Container path} {Image ID}
```

- `-v`
	- `--volume` 옵션 약자로 도커 볼륨을 생성하는 명령어
	- `run -v {Volume name}:{Container path}` 를 실행하면 `{Container path}` 내부 파일 볼륨이 생성된다.

## 볼륨 종류

### 익명 볼륨(Anonymous Volumes)

**특징**
- 각각의 컨테이너마다 생성 된다.
	- 해당 컨테이너만 사용 가능한 볼륨
- ``--rm`` 옵션으로 컨테이너 생성시 컨테이너가 중지되면 컨테이너와 같이 볼륨도 삭제된다.
	- **`--rm` 옵션 없이 컨테이너 생성, 중지, 제거할 경우 볼륨은 제거되지 않는다.**
- 컨테이너 간의 볼륨 공유가 불가능하다.
- 볼륨을 재사용 할 수 없다.
	- 같은 이미지로 컨테이너를 생성하더라도 볼륨은 공유되지 않는다.
- **`Dockerfile` 에서 `VOLUME ["{Container Path}"]`으로도 생성 가능하다.**

```bash
$ docker run -v {Container path} {Image ID}
```

### 명명된 볼륨(Named Volumes)

**특징**
- 일반적인 볼륨
- 도커 CLI 명령어로 제거해야 한다.
- 컨테이너 간의 볼륨 공유가 가능하다.
- 볼륨 재사용이 가능하다.

```bash
$ docker run -v {Volume name}:{Container path} {Image ID}
```

### 바인드 마운트(Bind Mounts)

**특징**
- 호스트 머신 파일 시스템과 연결된다.
- 호스트 머신 파일 시스템에서 삭제해야 한다. (컨테이너에서 제거 불가능)
- 컨테이너 간의 볼륨 공유가 가능하다.
- 볼륨 재사용이 가능하다.

```bash
$ docker run -v {Host Absolute path}:{Container path} {Image ID}
```

>볼륨 사용 예시
```bash
$ docker run -d --rm --name feedback-app -p 3000:80 \
> -v "/root/volume:/app" \
> -v /app/node_modules \
> -v feedback:/app/feedback
> -v /app/temp \
> {Image ID}
```

### 읽기 전용(Read only) 볼륨

>읽기 전용 볼륨은 컨테이너에서 수정할 수 없는 볼륨이다.
>컨테이너 내부에서 수정하면 안되는 파일(ex: 호스트 머신 파일)을 가진 볼륨이 있는 경우 `:ro` 를 사용하여 지정할 수 있다.

```bash
$ docker run -v {Host Absolute path}:{Container path}:ro {Image ID}
```
- 컨테이너에서는 `{Container path}` 내부 파일을 수정할 수 없다.
- 호스트 머신에서는 `{Host Absolute path}` 내부 파일을 수정할 수 있다.

### 볼륨(`-v`)은 {Container path}가 구체적일수록 우선순위를 갖는다

>소스 코드의 변경 사항을 이미지 재빌드 없이 반영하고 싶은 경우는 아래와 같이 바인드 마운트를 활용할 수 있다.
>`$ docker run -v /source:/app {Image ID}`
>하지만 만약 노드처럼 런타임으로 모듈을 설치하고 해당 모듈이 바운드 마운트 디렉토리(`/app/node_modules`)에 생성되는 경우 **바인드 마운트에 의해 `/app/node_modules`는 덮어씌여져** 모듈을 찾을 수 없는 오류가 발생한다.
>이런 경우 구체적 경로가 더 우선 되는 볼륨의 특성을 사용하여 `node_modules` 디렉토리를 **Override** 한다.
>`$ docker run -v /source:/app -v /app:node_modules {Image ID}`


## 볼륨 관리하기

>도커 볼륨은 Docker CLI 를 통해 관리할 수 있다.

**조회**
```bash
$ docker volume ls
```

**생성**
```bash
$ docker volume create {Volume name}
```

**제거**
```bash
$ docker volume rm {Volume name}
```
- 컨테이너에서 사용중인 볼륨은 제거 불가

**상세정보 조회**
```bash
$ docker volume inspect {Volume name}
```

---
# `COPY` 제외 파일 설정 방법

>`Dockerfile` 의 `COPY . .` 명령어는 현재 디렉토리의 모든 파일을 복사한다.
>만약 호스트 머신에 `node_modules` 가 있다면 `npm install` 로 생성된 모듈 디렉토리가 아닌 호스트 머신의 디렉토리로 덮어쓰기가 된다.
>호스트 머신의 `node_modules` 가 오래전 생성된 것일 경우 모듈이 다운로드 되지 않는 이슈가 발생할 것이다.
>이 문제 해결을 위해 도커는 `COPY` 에서 제외할 수 있는 기능을 제공한다.

### `.dockerignore`

>`.gitignore` 처럼 해당 파일에 작성된 디렉토리(파일)는 `COPY` 에서 제외된다.
>도커 이미지(애플리케이션 실행)에 불필요한 디렉토리(파일)를 작성한다.
>`.dockerignore` 파일은 `Dockerfile` 과 같은 디렉토리에 있어야 한다.

```dockerignore
node_modules
dist
.git
Dockerfile
```
- `node_modules`
	- `npm install` 로 생성된 모듈 파일 디렉토리
- `dist`
	- `npm run build` 로 생성된 애플리케이션 정적 파일 디렉토리
- `Dockerfile`
	- `Dockerfile` 은 기본적으로 제외되지만, 명시적으로 작성

---
# 환경 변수

>`Dockerfile` 및 애플리케이션 코드에서 사용 가능한 환경변수를 설정할 수 있다.
>`Dockerfile` 에서 지정한 환경 변수 값을 컨테이너 생성할 때 변경할 수 있다.

### Dockerfile 환경 변수 사용
```dockerfile
FROM node:14

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

# VOLUME [ "/app/node_modules" ]

ENV PORT 80

EXPOSE $PORT

CMD [ "node", "server.js" ]
```

- `ENV PORT 80`
	- `ENV` 는 환경 변수 지정 명령어
	- `PORT` 는 변수명
	- `80` 은 기본값으로 사용됨
- `EXPOSE $PORT`
	- 환경 변수는 변수명 앞에 `$` 를 붙여서 사용


### 런타임 환경 변수 Override(변경)

##### CLI(커맨드) 방법
```bash
$ docker run -d --rm --name feedback-app -p 3000:8000 \
> -e PORT=8000 \
> -v "/root/env:/app" \
> -v /app/node_modules \
> -v feedback:/app/feedback \
> -v /app/temp \
> {Image ID}
```
- `-e PORT=8000`
	- `-e` 는 `--env` 의 약자로 환경 변수 설정 옵션
	- `PORT=8000` 은 `PORT` 라는 환경 변수에 `8000` 대입

##### 환경 변수 파일 방법

>`.env` 파일
```env
PORT=8000
```

>`.env` 적용 방법
```bash
$ docker run -d --rm --name feedback-app -p 3000:8000 \
> --env-file ./.env \
> -v "/root/env:/app" \
> -v /app/node_modules \
> -v feedback:/app/feedback \
> -v /app/temp \
> {Image ID}
```
- `--env-file ./.env`
	- `./.env` 는 현재 터미널 위치에 `.env` 파일이 있는 경우 (상대 경로)
	- `/root/e-env/.env` 같이 절대 경로도 사용 가능

---
# 빌드 인수(Arguments)

>`Dockerfile`에서 사용 가능한 변수이다. 
>`CMD` 커맨드와 애플리케이션 코드에서는 사용할 수 없다.
>이미지를 빌드할 때(`docker build`) 값을 Override(변경) 할 수 있다.

### Dockerfile에 인수 선언
```dockerfile
FROM node:14

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

# VOLUME [ "/app/node_modules" ]

ARG DEFAULT_PORT=80

ENV PORT=$DEFAULT_PORT

EXPOSE $PORT

CMD [ "node", "server.js" ]
```
- `ARG DEFAULT_PORT=80`
	- `ARG`: 빌드 인수 선언 명령어
	- `DEFAULT_PORT=80`: 변수명과 기본값
- `ENV PORT=$DEFAULT_PORT`
	- `$DEFAULT_PORT`: `DEFAULT_PORT` 변수 참조

### 런타임 빌드 인수 Override(변경)
```bash
$ docker build -t feedback:args --build-arg DEFAULT_PORT=9000 .
```
- `--build-arg DEFAULT_PORT=8000`
	- `--build-arg`: 빌드 인수 전달 옵션
	- `DEFAULT_PORT=9000`: `DEFAULT_PORT` 변수 값을 9000으로 변경

---
# 네트워크(Network)

>도커 컨테이너의 통신은 3가지로 분류할 수 있다.
>1. 컨테이너와 외부(예: 웹) 통신
>2. 컨테이너와 호스트 머신 통신
>3. 컨테이너와 컨테이너의 통신

### 컨테이너 <-> 웹 통신

>컨테이너는 기본적으로 격리되어 있지만 외부(예: 웹)와의 통신은 가능하다.
>그 이유는 웹 애플리케이션 컨테이너를 생성할 때 `-p` 옵션을 통해 호스트 머신의 포트와 매핑되기 때문이다.

**Node 애플리케이션 API 통신 메서드**
```js
app.get('/movies', async (req, res) => {
    try {
        const response = await axios.get('https://swapi.dev/api/films');
        res.status(200).json({ movies: response.data });
    } catch (error) {
        res.status(500).json({ message: 'Something went wrong.' });
    }
});
```
- `https://swapi.dev/api/films`에서 영화 목록을 요청하는 메서드

### 컨테이너 <-> 호스트 머신 통신

>컨테이너와 호스트 머신이 통신하기 위해서는 **특수한 예약어(host)** 가 필요하다.
>도커는 `host.docker.internal`를 호스트 머신의 IP로 변환한다.

**Mongo DB 접속 메서드**
```js
mongoose.connect(
    // 'mongodb://localhost:27017/swfavorites',
    'mongodb://host.docker.internal:27017/swfavorites',
    { useNewUrlParser: true },
    (err) => {
        if (err) {
            console.log(err);
        } else {
            app.listen(3000);
        }
    }
);
```
- `mongoose.connect()`
	- Mongo DB 접속 메서드
- `mongodb://localhost:27017/swfavorites`
	- `localhost:27017`의 `swfavorites` DB 커넥션을 요청한다.
	- `localhost:27017` 은 컨테이너의 **27017** 포트를 가리키고, 컨테이너에는 Mongo DB가 없기 때문에 에러가 발생한다.
- `mongodb://host.docker.internal:27017/swfavorites`
	- 도커는 `host.docker.internal` 을 호스트 머신의 IP로 변환한다.
	- **27017** 포트 MongoDB의 `swfavorites` DB 커넥션을 요청한다.
	- **`host.docker.internal` 을 통해 호스트 머신과 통신하기 위해서는 `host.docker.internal` 가 도커 게이트웨이를 가리키도록 지정해주어야 한다.**
		- `--add-host=host.docker.internal:host-gateway`

### 컨테이너 <-> 컨테이너 통신 (도커 네트워크)

>격리된 컨테이너끼리 통신하기 위해 도커는 docker 네트워크를 지원한다.
>아래는 웹 애플리케이션 컨테이너와 Mongo DB 컨테이너를 도커 네트워크를 사용하여 통신하는 시나리오이다.

##### Movie App Container <-> MongoDB Container 시나리오

**1. Docker Network 생성**
```bash
$ docker network create movie-net
```
- `network create movie-net`
	- `movie-net` 네트워크 생성

**2. MongoDB Container 생성 및 네트워크 연결**
```bash
$ docker run -d --rm --name mongodb --network movie-net mongo
```
- `--network movie-net`
	- `mongodb` 컨테이너를 `movie-net` 네트워크에 연결

**3. Movie App 코드에 MongoDB 접속 정보 작성**
```js
mongoose.connect(
    'mongodb://mongodb:27017/swfavorites',
    { useNewUrlParser: true },
    (err) => {
        if (err) {
            console.log(err);
        } else {
            app.listen(3000);
        }
    }
);
```
- `mongodb://mongodb:27017`
	- `mongodb`: 2번에서 생성한 Mongo DB 컨테이너 이름

**4. Movie App 이미지 생성**
```bash
$ docker build -t movie .
```

**5. Movie App Container 생성 및 네트워크 연결**
```bash
$ docker run -d --rm -p 3000:3000 --name movie-app --network movie-net movie
```

### Docker 네트워크 드라이버

>`Docker Networks` 는 네트워크 동작에 영향을 미치는 다양한 종류의 **드라이버**를 지원한다.
>드라이버는 네트워크 생성 시 `--driver` 옵션을 통해 설정할 수 있다.

- **bridge(default)**
	- 컨테이나가 동일한 네트워크에 있는 경우, 컨테이너 이름을 IP로 변환해준다.
	- 기본 드라이버(`--driver` 옵션 생략 시 적용)
- **host**
	- Standalone 컨테이너의 경우, 컨테이너와 호스트 시스템 간의 격리가 제거된다. (localhost를 네트워크로 공유)
- **overlay**
	- 여러 Docker 데몬(서로 다른 머신에서 실행되는 Docker)이 서로 연결될 수 있다.
	- 여러 컨테이너를 연결하는 거의 사용되지 않는 방법인 Swarm 모드에서만 작동된다.
- **macvlan**
	- 컨테이너에 커스텀 MAC 주소를 설정할 수 있다.
	- MAC 주소를 통신하는데 사용할 수 있다.
- **none**
	- 모든 네트워킹이 비활성화
- **third-party plugin**
	- 모든 종류의 동작과 기능을 추가할 수 있는 타사 플러그인을 설치할 수 있다.

---
# Docker로 다중 컨테이너 애플리케이션 구축

>도커 이미지, 컨테이너, 볼륨, 네트워크를 활용하여 **Goals App** 애플리케이션을 구현해본다.
>총 3개의 컨테이너와 도커 네트워크를 사용하여 **Goals App** 애플리케이션을 실행한다.
>1. 데이터베이스 컨테이너 (`Mongo DB`)
>2. 백엔드 컨테이너(`Express API`)
>3. 프론트엔드 컨테이너 (`React`)


### 데이터베이스 컨테이너 생성

>**컨테이너 요구 사항**
>- `mongo` 공식 이미지 사용.
>- 컨테이너 이름은 `mongodb`.
>- `"goals-net"` 도커 네트워크 사용.
>- 컨테이너 중지 시 자동 삭제.
>- DB 데이터 유지되도록 설정 (`Mongo DB` 컨테이너의 데이터 저장 위치는 `/data/db`).

###### 네트워크 생성 명령어
```bash
$ docker network create goals-net
```

###### Mongo DB 컨테이너 생성 명령어
```bash
$ docker run -d --name mongodb --network goals-net --rm -v data:/data/db mongo
```


### 백엔드 컨테이너 생성

>**컨테이너 생성 요구 사항**
>- `node:14` 공식 이미지 사용.
>- 컨테이너 이름은 `goals-backend`.
>- `goals-net` 도커 네트워크 사용.
>- 컨테이너 중지 시 자동 삭제.
>- **80** 포트 사용.
>- 환경 변수(`DB_URL`, `PORT`) 사용.
>	- `DB_URL`: **Mongo DB 컨테이너 접속 URL**
>	- `PORT`: 80
>- 애플리케이션 실행 명령어는 `node app.js`
>- `.env` 파일 사용.
>- 로그 데이터 유지되도록 설정 (`logs`)
>- 이미지 재빌드 없이 소스 코드 수정 사항 반영.

###### Dockerfile
```dockerfile
FROM node:14

WORKDIR /app

COPY package.json /app/

RUN npm install

COPY . /app/

VOLUME ["/app/node_modules"]

ENV DB_URL="mongodb"

ENV PORT=80

EXPOSE $PORT

CMD ["node", "app.js"]
```

###### .env
```env
DB_URL=mongodb
PORT=80
```

###### 이미지 빌드 명령어
```bash
$ docker build -t goals-node .
```

###### 백엔드 컨테이너 생성 명령어
```bash
$ docker run -d --name goals-backend --network goals-net --rm -p 80:80 \
> --env-file ./.env \
> -v logs:/app/logs \
> -v /root/goals/backend:/app \
> goals-node
```


### 프론트엔드 컨테이너 생성

>**컨테이너 생성 요구 사항**
>- `node:14` 공식 이미지 사용.
>- 컨테이너 이름은 `goals-frontend`
>- 컨테이너 중지 시 자동 삭제.
>- 이미지 재빌드 없이 소스 코드 수정 사항 반영.
>	- 컨테이너 내부에서 소스 코드 수정 안되도록 설정.
>- **3000** 포트 사용.
>- 애플리케이션 실행 명령어는 `npm start`

###### Dockerfile
```dockerfile
FROM node:14

WORKDIR /app

COPY package.json /app/

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
```

###### 이미지 빌드 명령어
```bash
$ docker build -t goals-react .
```

###### 프론트엔드 컨테이너 생성 명령어
```bash
$ docker run -d --name goals-frontend --rm -v /root/goals/frontend/src:/app/src:ro -p 3000:3000 goals-react
```

---
# 끝
