>  _사전에 git 설치 및 name과 email 설정이 되어 있어야 한다_

# 1. 기존 SSH 키가 있는지 확인

터미널에서 아래 명령어 실행.
```bash
ls -al ~/.ssh
# Lists the files in your .ssh directory, if they exist
```

디렉터리 목록에 아래의 파일이 없으면 SSH 키를 생성 해야함.
- _id_rsa.pub_
- _id_ecdsa.pub_
- _id_ed25519.pub_
> *만약 ~/.ssh 가 존재하지 않는 다는 오류가 발생하면 기본 위치에 SSH 키가 없으므로 새로 생성.*
> *다른 디렉토리에 키가 존재할 수도 있으나 기본 위치에서 사용하는게 편리함.*


# 2. 새로운 SSH 키 생성 방법

GitHub 이메일 주소로 아래 명령을 실행하여 SSH 키를 생성한다.
```shell
ssh-keygen -t ed25519 -C "yeom220@gmail.com"
```

# 3. ssh-agent에 SSH 키 추가

백그라운드에서 ssh-agent 실행한다.
```shell
$ eval "$(ssh-agent -s)"
> Agent pid 21987
```

macOS Sierra 10.12.2 이상을 사용하는 경우 ssh-agent에 키를 자동으로 로드하고 키 집합에 암호를 저장하도록 `~/.ssh/config` 파일을 수정해야 한다.
```shell
$ open ~/.ssh/config
> The file /Users/YOU/.ssh/config does not exist.
```

파일이 없으면 생성한다.
```bash
touch ~/.ssh/config
```

config 파일에 아래 코드 입력 후 저장한다
```text
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
```
> 만약 SSH 키 생성할 때 경로나 파일명을 변경한 경우 _IdentityFile {SSH 키 생성된 경로} 로 저장한다._

ssh-agent에 SSH 프라이빗 키를 추가하고 키 집합에 암호를 저장한다. 만약, 다른 이름으로 키를 만들거나 이름이 다른 기존 키를 추가하는 경우 명령의 _id_ed25519_를 프라이빗 키 파일의 이름으로 바꾼다._
```shell
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```
> OS Monterey(12.0)이전 버전의 경우 _--apple-use-keychain_ 대신 _-K_ 구문을 사용한다.

# 4. GitHub 계정에 새 SSH 키 추가

클립보드에 SSH 공개키를 복사한다.
```shell
$ pbcopy < ~/.ssh/id_ed25519.pub
# Copies the contents of the id_ed25519.pub file to your clipboard
```

GitHub SSH 키 관리 페이지(https://github.com/settings/keys)로 이동하여 복사한 SSH 공개키 붙여넣은 후 저장한다.


# 5. SSH 연결 테스트

터미널에서 아래 명령어를 실행한다.
```shell
$ ssh -vT git@github.com
# Attempts to ssh to GitHub
```

실행결과 _debug1: Exit status 1_ 이 출력되면 테스트 통과이다.
```text
......
Hi yeom220! You've successfully authenticated, but GitHub does not provide shell access.
......
debug1: Exit status 1
```

# 마지막으로...

>[GitHub 공식문서] [https://docs.github.com/ko/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys]에 가면, 더욱 자세한 설명과 여러 에러케이스 및 해결방법이 나와있으니 꼭 보길 바란다.



# 참조 문서

- [GitHub 공식문서] [https://docs.github.com/ko/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys]


