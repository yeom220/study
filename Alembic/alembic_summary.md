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
$ pip install alembic
```

---
# Alembic 환경 구성

#### [마이그레이션 환경 생성](https://alembic.sqlalchemy.org/en/latest/tutorial.html#the-migration-environment)

Alembic 사용은 마이그레이션 환경 생성부터 시작합니다.
마이그레이션 환경은 한 번만 생성되고, 애플리케이션의 소스 코드와 함께 유지 관리 됩니다.
환경은 Alembic의 ***init*** 명령을 사용하여 생성됩니다.

```bash
$ alembic init migrations
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
	- 변경사항을 데이터베이스에 적용하기 위한 함수 (마이그레이션 적용)
- **downgrade()**
	- 데이터베이스에 적용된 변경사항을 되돌리기 위한 함수 (롤백)

>`account` 테이블 생성 스크립트 작성

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
# 마이그레이션 적용

#### 최초의 마이그레이션 적용
```bash
$ alembic upgrade head
INFO  [alembic.context] Context class PostgresqlContext.
INFO  [alembic.context] Will assume transactional DDL.
INFO  [alembic.context] Running upgrade None -> 1975ea83b712
```

>`alembic upgrade head` 명령어는 현재 데이터베이스 `revision` 에서 지정된 `revision` 으로 업그레이드 작업(마이그레이션)을 진행합니다.
>Alembic 은 우선 데이터베이스에 `alembic_version` 이라는 테이블이 없으면 생성하고, 이 테이블에 진행된 `revision` 을 저장합니다.
>Alembic 은 `alembic_version` 테이블을 확인하여 현재 적용되어 있는 `revision` 을 파악하고 요청된 버전까지 업그레이드를 진행합니다.

#### 두번째 마이그레이션 스크립트 생성 및 적용

>마이그레이션 스크립트 생성
```bash
$ alembic revision -m "Add a column"
Generating /path/to/yourapp/alembic/versions/ae1027a6acf_add_a_column.py...
done
```

>`last_transaction_date` 컬럼 추가 마이그레이션 스크립트 작성

```python
"""Add a column

Revision ID: ae1027a6acf
Revises: 1975ea83b712
Create Date: 2011-11-08 12:37:36.714947

"""

# revision identifiers, used by Alembic.
revision = 'ae1027a6acf'
down_revision = '1975ea83b712'

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))

def downgrade():
    op.drop_column('account', 'last_transaction_date')
```

> 마이그레이션 적용

```bash
$ alembic upgrade head
INFO  [alembic.context] Context class PostgresqlContext.
INFO  [alembic.context] Will assume transactional DDL.
INFO  [alembic.context] Running upgrade 1975ea83b712 -> ae1027a6acf
```

#### 상대적 마이그레이션 적용

>`alembic upgrade head` 명령어는 최신 스크립트까지 적용하는 명령어 입니다.
>만약 현재 `revision` 에서 2개의 마이그레이션 스크립트만 적용하고 싶다면 아래와 같이 할 수 있습니다.

```bash
$ alembic upgrade +2
```

>다운그레이드(롤백)에는 음수를 사용합니다.

```bash
$ alembic downgrade -1
```

>마이그레이션을 적용하지 않은 상태로 롤백은 `base` 키워드를 사용합니다.

```bash
$ alembic downgrade base
INFO  [alembic.context] Context class PostgresqlContext.
INFO  [alembic.context] Will assume transactional DDL.
INFO  [alembic.context] Running downgrade ae1027a6acf -> 1975ea83b712
INFO  [alembic.context] Running downgrade 1975ea83b712 -> None
```

---
# 자동 생성 마이그레이션

>Alembic 은 데이터베이스의 테이블과 ORM 모델(테이블 메타데이터)을 비교하여 마이그레이션 스크립트를 생성할 수 있습니다.
>자동 생성을 사용하려면 `env.py` 를 수정하여 마이그레이션을 생성할 테이블의 메타데이터를 지정해야 합니다.

```python
# env.py
...

from myapp.mymodel import Base
target_metadata = Base.metadata

...
```

>자동 생성은 `alembic revision` 명령어에 `--autogenerate` 옵션을 추가합니다. `MetaData` 에 `account` 테이블에 대한 정의가 포함되어 있고, 데이터베이스에 `account` 테이블이 없다고 하면 아래와 같이 스크립트가 생성됩니다.

```bash
$ alembic revision --autogenerate -m "Added account table"
INFO [alembic.context] Detected added table 'account'
Generating /path/to/foo/alembic/versions/27c6a30d7c24.py...done
```

```python
"""Added account table

Revision ID: 27c6a30d7c24
Revises: None
Create Date: 2011-11-08 11:40:27.089406

"""

# revision identifiers, used by Alembic.
revision = '27c6a30d7c24'
down_revision = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
    'account',
    sa.Column('id', sa.Integer()),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.VARCHAR(200)),
    sa.Column('last_transaction_date', sa.DateTime()),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###

def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("account")
    ### end Alembic commands ###
```

[자동 마이그레이션 문서](https://alembic.sqlalchemy.org/en/latest/autogenerate.html#auto-generating-migrations)

---
# 왜 마이그레이션 도구를 사용할까?

>자바 JPA 는 SQLAlchemy 와 달리 모델(엔티티)와 테이블을 비교하여 자동으로 엔티티에 맞게 테이블을 수정(DDL)하는 기능이 있지만, `Flyway` 라는 마이그레이션 도구를 많이 사용합니다.

### 개인적인 생각

>데이터베이스는 테이블 또는 컬럼이 삭제되면 데이터도 같이 삭제됩니다.
>JPA의 경우 엔티티에서 컬럼 하나를 주석하고 애플리케이션만 실행해도 테이블에서 해당 컬럼이 삭제되어 데이터를 잃게 됩니다.
>이러한 위험성으로 인해 편리함에도 불구하고 안정성을 위해 명시적인 마이그레이션 도구를 사용합니다.
>마이그레이션 도구는 직접 명령어를 사용해야만 적용되기 때문에 한번 더 체크할 수 있어 실수로 인한 데이터 유실 가능성이 낮습니다.
>또한, 각각의 데이터베이스 변경사항을 스크립트로 관리하기 때문에 이력 추적이 쉽고, 데이터베이스 구조를 소스 코드처럼 버전 관리도 가능합니다.

---
[Alembic 공식 문서](https://alembic.sqlalchemy.org/en/latest/index.html)
