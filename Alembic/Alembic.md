# Alembic이란?

>Alembic은 Python 기반의 데이터베이스 마이그레이션 도구로, SQLAlchemy를 기본 엔진으로 사용하여 관계형 데이터베이스에 대한 변경 관리 스크립트를 만들고, 관리하고, 호출할 수 있도록 해줍니다. 
>Alembic은 데이터베이스 구조가 변경될 때 이를 추적하고, 쉽게 롤백하거나 적용할 수 있도록 돕는 강력한 도구 입니다. 

---
# Alembic 주요 개념

1. **마이그레이션(Migration)**
	- 데이터베이스 스키마의 변화를 코드로 관리 
	- 예: 테이블 추가, 삭제, 컬럼 변경 등
2. **버전 제어(Version Control)**
	- 데이터베이스의 현재 상태(DDL)를 특정 버전으로 기록
	- 마이그레이션 히스토리를 관리하여 이전 상태로 되돌릴 수 있음
3. **SQLAlchemy 통합**
	- SQLAlchemy와 함께 사용되며, SQLAlchemy의 메타데이터를 기반으로 마이그레이션 자동 생성

---
# Alembic 설치

Alembic은 Python 패키지 관리자(pip)로 설치 합니다.

```bash
pip install alembic
```

---
# Alembic 환경 구성

#### [마이그레이션 환경 생성](https://alembic.sqlalchemy.org/en/latest/tutorial.html#the-migration-environment)

Alembic 사용은 마이그레이션 환경 생성부터 시작합니다.
마이그레이션 환경은 한 번만 생성되고, 애플리케이션의 소스 코드와 함께 유지 관리 됩니다.
환경은 Alembic의 ***init*** 명령을 사용하여 생성됩니다.

```bash
alembic init migrations
```

생성된 마이그레이션 환경의 구조는 다음과 같습니다.

```
yourproject/
    migrations/
        env.py
        README
        script.py.mako
        versions/
            3512b954651e_add_account.py
            2b1ae634e5cd_add_order_id.py
            3adcc9a56557_rename_username_field.py
	alembic.ini
```

- **yourproject**
	- 애플리케이션 소스 코드의 루트 디렉토리
- **migrations**
	- 마이그레이션 환경의 홈 디렉토리
	- 아무 이름이나 지정 가능
	- 여러 데이터베이스를 사용하는 프로젝트는 2개 이상을 가질 수 있음
- **env.py**
	- 마이그레이션 환경을 설정하는 스크립트로, SQLAlchemy 엔진 및 메타데이터 연결을 정의
	- Alembic 마이그레이션 도구가 호출될 때마다 실행되는 Python 스크립트
	- SQLAlchemy 엔진을 통해 데이터베이스 커넥션을 구성하고 마이그레이션 엔진을 호출 방법이 정의되어 있음
	- 여러 엔진을 작동시키거나 사용자 정의 인수를 마이그레이션 환경으로 전달하는 등, 커스터마이징 가능
- **script.py.mako**
	- 새로운 마이그레이션 스크립트를 생성하는 데 사용되는 **Mako** 템플릿 파일
	- **verions** 디렉토리에 생성되는 각 마이그레이션 파일의 구조를 정의
- **versions**
	- 각 마이그레이션 스크립트를 저장하는 디렉토리
	- 마이그레이션 파일은 `{revision id}_{slug}` 로 생성됨
- **alembic.ini**
	- Alembic 설정 파일로, 데이터베이스 URL, 마이그레이션 스크립트 위치 등을 정의
	- [공식 문서](https://alembic.sqlalchemy.org/en/latest/tutorial.html#editing-the-ini-file)

---
# 마이그레이션 스크립트 생성

```bash
$ alembic revision -m "create account table"
```

>위의 명령어 실행시 `1975ea83b712_create_account_table.py` 이 생성됩니다.
>생성된 마이그레이션 스크립트 파일의 내용은 아래와 같습니다.

```python
"""create account table

Revision ID: 1975ea83b712
Revises:
Create Date: 2011-11-08 11:40:27.089406

"""

# revision identifiers, used by Alembic.
revision = '1975ea83b712'
down_revision = None
branch_labels = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    pass

def downgrade():
    pass
```

- **revision**
	- 마이그레이션을 구분할 고유 식별자
- **down_revision**
	- 올바른 마이그레이션 순서를 위한 이전 마이그레이션 식별자
	- 다음 마이그레이션 스크립트 생성시 `1975ea83b712` 로 지정됨
- **upgrade()**
	- 변경사항을 데이터베이스에 적용하기 위한 함수
- **downgrade()**
	- 데이터베이스에 적용된 변경사항을 되돌리기 위한 함수

>`account` 테이블을 생성하기 위한 스크립트 작성

```python
def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )

def downgrade():
    op.drop_table('account')
```

[Alembic 지시어(op) 문서](https://alembic.sqlalchemy.org/en/latest/ops.html#ops)

---

