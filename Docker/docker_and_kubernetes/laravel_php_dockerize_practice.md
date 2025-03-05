# Laravel 프레임워크와 PHP를 도커로 구축

>호스트 머신에 관련 패키지 설치 없이 도커만으로 Laravel 애플리케이션을 구축해본다.
>구성은 아래와 같다.
>
>**애플리케이션 구동 컨테이너**
>1. MySQL 컨테이너
>2. Nginx 웹 서버 컨테이너
>3. PHP 인터프리터 컨테이너
>
>**유틸리티 컨테이너**
>1. Node 컨테이너
>2. Laravel Artisan 컨테이너 (DB 마이그레이션)
>3. Composer 컨테이너 (Laravel 빌드)

![[laravel_app_architecture.png]]

---
# composer.Dockerfile

```dockerfile
FROM composer:latest

WORKDIR /var/www/html

ENTRYPOINT ["composer", "--ignore-platform-reqs"]
```

# php.Dockerfile

```dockerfile
FROM php:8.2-fpm-alpine

WORKDIR /var/www/html

RUN docker-php-ext-install pdo pdo_mysql
```

# docker-compose.yml 정의

```yaml
services:
	server:
		image: 'nginx:stable-alpine'
		ports:
			- '8000:80'
		volumes:
			- ./src:/var/www/html
			- ./nginx/nginx.conf:/etc/nginx/conf.d/default.conf:ro
		depends_on:
			- php
			- mysql
	php:
		build:
			context: ./dockerfiles
			dockerfile: php.Dockerfile
		volumes:
			- ./src:/var/www/html:delegated
	mysql:
		image: 'mysql:5.7'
		env_file:
			- ./env/mysql.env
	composer:
		build:
			context: ./dockerfiles
			dockerfile: composer.Dockerfile
		volumes:
			- ./src:/var/www/html
	artisan:
		build:
			context: ./dockerfiles
			dockerfile: php.Dockerfile
		volumes:
			- ./src:/var/www/html
		entrypoint: ['php', '/var/www/html/artisan']
	npm:
		image: 'node:14'
		working_dir: /var/www/html
		entrypoint: ['npm']
		volumes:
			- ./src:/var/www/html
```
- `depends_on:`
	- 컨테이너간의 종속성을 나타냄.
	- 도커 데몬이 `server` 컨테이너를 `php`, `mysql` 컨테이너 생성 후에 생성.
	- `$ docker compose up server` 명령어로 `server` 컨테이너만 실행하여도 종속성에 의해 `php`, `mysql`도 같이 실행됨.
- `entrypoint:`
	- `CMD` 명령 같이 컨테이너 실행 후에 실행되는 명령어.
	- `CMD` 가 `run` 또는 `up` 명령시에 전달된 명령어가 있는 경우 해당 명령어로 Override 되는 것과 달리 전달된 명령어가 명시된 명령어 뒤에 붙어 사용됨.
	- 예시: `entrypoint: ['npm']`
		- `$ docker run npm install`: `npm` 컨테이너가 실행될 때 `['npm']`과 결합되어 `npm install` 명령어가 실행됨.
- `working_dir:`
	- Dockerfile의 `WORKDIR`과 동일
	- Dockerfile을 작성하지 않고 `npm` 컨테이너 같이 compose.yml 파일에 정의 가능
	- compose.yml 에 정의 가능한 Dockerfile 명령어
		- 가능: `WORKDIR`, `ENTRYPOINT`, `VOLUME`, `FROM`
		- 불가능: `COPY`, `RUN`

---
# docker-compose.yml 에서 특정 서비스만 구동

```bash
$ docker compose run --rm artisan migrate
```
- `artisan` 서비스만 구동
- `migrate`
	- `entrypoint`에 전달되는 명령어
	- `php /var/www/html/artisan migrate`

```bash
$ docker compose up -d --build server
```
- `server` 서비스만 구동
	- `server` 서비스는 `php`, `mysql` 서비스에 종속되어(`depends_on`)있어, `php`, `mysql` 서비스도 같이 실행됨.
- `--build`
	- 실행되는 서비스의 이미지를 재빌드하여 반영

---
# 바인드 마운트 VS COPY

>바인드 마운트는 호스트 머신에 연결되어 실시간 반영 및 컨테이너 생성파일 공유 등 유용한 점이 많다. 하지만 배포할 때 다른 머신에는 바인드 마운트로 정의된 디렉토리가 없다. 이 경우 오류가 발생한다.
>따라서 배포의 경우 필요한 것들(소스, 설정 파일 등...)을 모두 이미지에 `COPY`를 통해 담는다.

>`nginx` 서비스 Dockerfile 생성

```dockerfile
FROM nginx:stable-alpine

WORKDIR /etc/nginx/conf.d

COPY nginx/nginx.conf .

RUN mv nginx.conf default.conf

WORKDIR /var/www/html

COPY src .
```

>`docker-compose.yml` 수정
```yaml
services:
	server:
		#image: 'nginx:stable-alpine'
		build:
			context: .
			dockerfile: dockerfiles/nginx.Dockefile
		ports:
			- '8000:80'
		#volumes:
		#	- ./src:/var/www/html
		#	- ./nginx/nginx.conf:/etc/nginx/conf.d/default.conf:ro
		depends_on:
			- php
			- mysql
	php:
		build:
			#context: ./dockerfiles
			#dockerfile: php.Dockerfile
			context: .
			dockerfile: dockerfiles/php.Dockerfile
		volumes:
			- ./src:/var/www/html:delegated
	mysql:
		image: 'mysql:5.7'
		env_file:
			- ./env/mysql.env
	composer:
		build:
			context: ./dockerfiles
			dockerfile: composer.Dockerfile
		volumes:
			- ./src:/var/www/html
	artisan:
		build:
			context: .
			dockerfile: dockerfiles/php.Dockerfile
		volumes:
			- ./src:/var/www/html
		entrypoint: ['php', '/var/www/html/artisan']
	npm:
		image: 'node:14'
		working_dir: /var/www/html
		entrypoint: ['npm']
		volumes:
			- ./src:/var/www/html
```

>php.Dockerfile 수정

```dockerfile
FROM php:8.2-fpm-alpine

WORKDIR /var/www/html

COPY src .

RUN docker-php-ext-install pdo pdo_mysql

RUN chown -R www-data:www-data /var/www/html
```
- `COPY src .`
	- 이전 php.Dockerfile 에는 소스 코드를 복사하지 않고 바인드 마운트로 참조했기 때문에 다른 머신에는 소스코드가 존재 할 수 없다.
	- 바인드 마운트 대신 `COPY`를 통해 소스 코드를 이미지에 저장한다.
- `RUN chown -R www-data:www-data /var/www/html`
	- php는 여러가지 파일을 소스 디렉토리에 생성하는 데, 권한 오류가 발생할 수 있다.
	- `php` 이미지는 `www-data` 사용자를 생성하여 사용하기 때문에 소스 디렉토리(`/var/www/html`)의 소유자를 `www-data`로 변경하여 권한 문제를 해결한다.

---
