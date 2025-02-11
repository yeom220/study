# Docker Compose ?

>`Docker Compose` 는 여러 도커 컨테이너를 하나의 애플리케이션으로 정의하고 관리할 수 있도록 도와주는 도구이다.
>단일 **YAML** 파일을 통해 컨테이너의 설정, 네트워크, 볼륨 등을 정의할 수 있으며, 이를 통해 멀티 컨테이너 애플리케이션을 쉽게 배포하고 실행할 수 있다.

# 주요 개념

1. **서비스 (Service)**
	- 각 서비스는 하나의 컨테이너를 나타내며, 애플리케이션의 특정 역할(ex: 웹 서버, 데이터베이스 등)을 수행한다.
2. **네트워크 (Network)**
	- Compose 는 각 서비스 간의 통신을 위해 자동으로 네트워크를 생성한다.
3. **볼륨 (Volume)**
	- 데이터를 컨테이너 외부에 저장하거나 컨테이너 간 공유할 수 있는 스토리지.
4. **YAML 파일**
	- `docker-compose.yml` 파일을 사용하여 애플리케이션과 구성요소를 정의한다.


**docker-compose.yml**
```yaml
# version: '3.8'

services:
  mongodb:
    image: 'mongo'
    volumes:
      - data:/data/db
  backend:
    build: ./backend
    # build:
    #   context: ./backend
    #   dockerfile: Dockerfile
    #   args:
    #     some-arg: 1
    # container_name: goals-backend
    volumes:
      - logs:/app/logs
      - ./backend:/app
      - /app/node_modules
    ports:
        - '80:80'
    # environment:
    #   - DB_URL=mongodb
    #   - PORT=80
    env_file:
        - ./backend/.env
    depends_on:
      - mongodb
  frontend:
    build: ./frontend
    volumes:
      - ./frontend/src:/app/src:ro
    ports:
      - '3000:3000'
    depends_on:
      - backend

volumes:
  data:
  logs:
```
- 위 파일은 `goals` 애플리케이션의 구성요소를 작성한 `yaml` 파일이다.
- `versions: '3.8'`
	- Compose V1 에서 Compose 파일 포맷을 구분하기 위한 표기였지만, **Compose V2 에서는 더이상 사용하지 않는다.**
- `services:`
	- 구성할 서비스(컨테이너)를 작성.
	- `mongodb:`
		- Mongo DB 컨테이너의 서비스명.
		- `image: 'mongo'`
			- mongo 공식 이미지를 사용.
		- `volumes:`
			- `- data:/data/db`
				- 이름이 data인 볼륨을 만든다.
	- `backend:`
		- `build: ./backend`
			- ./backend 디렉토리 안의 Dockerfile을 기반으로 이미지를 빌드.
		- `build:`
			- 이미지 빌드 조건을 상세히 적을 때 사용.
			- `context: ./backend`
				- Dockerfile의 명령어가 사용되는 컨텍스트(위치)
			- `dockerfile: Dockerfile`
				- 빌드할 Dockerfile 이름(default: Dockerfile)
			- `args:`
				- 빌드 인수를 선언.
				- `some-arg: 1`
					- 빌드 옵션 --build-arg some-arg=1 와 동일.
			- `container_name: goals-backend`
				- 생성되는 컨테이너 이름 지정.
				- 지정하지 않을 경우 "{파일경로-서비스명-숫자}" 로 된다.
		- `volumes:`
			- `./backend:/app`
				- 바인드 마운트.
				- **docker run 과 다르게 Relative Path(상대 경로)도 사용이 가능하다.**
			- `/app/node_modules`
		- `ports:`
			- `- '80:80'`
				- docker run 옵션 -p 80:80 와 동일.
		- `environment:`
			- 환경 변수를 선언.
			- `- DB_URL=mongodb`
			- `- PORT=80`
				- docker run 옵션 -e PORT=80 와 동일.
		- `env_file:`
			- `- ./backend/.env`
				- 환경 변수 파일 지정
		- `depends_on:`
			- `- mongodb`
				- **backend 서비스는 mongodb 서비스에 의존하기 때문에 mongodb 컨테이너가 실행된 후에 실행되어야 한다.**
				- depends_on은 서비스 간 의존성 나타낸다.
				- mongodb 서비스 컨테이너 생성 후 backend 서비스 컨테이너 생성
	- `frontend`:
		- 프론트엔드 컨테이너

- `volumes:`
	- **명명된 볼륨은 아래와 같이 명시적으로 선언해주어야 한다.**
	- `data:`
		- `mongodb` 서비스에서 사용(마운트)하는 볼륨
	- `logs:`
		- `backend` 서비스에서 사용하는 볼륨

---
# 주요 명령어

- `$ docker-compose up`
	- 서비스를 빌드하고 컨테이너를 실행.
	- `--build` 옵션 사용 시 이미지 강제 재빌드.
- `$ docker-compose down`
	- 실행 중인 컨테이너를 중지하고 네트워크를 제거.
	- `-v` 옵션 사용 시 볼륨도 제거.
- `$ docker-compose ps`
	- 실행 중인 컨테이너 확인.
- `$ docker-compose build`
	- 이미지 빌드.
- `$ docker-compose logs`
	- 서비스 로그 확인.

---
