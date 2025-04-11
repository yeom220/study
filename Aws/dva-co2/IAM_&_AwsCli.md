# IAM
- 글로벌 서비스로 모든 리전에서 사용 가능
- Users
	- 실제 사용자 계정
	- AWS Console 접속을 위한 비밀번호 필요
- Groups
	- 사용자들로만 구성된 묶음
- Policies
	- JSON 포맷으로 된 사용자 또는 그룹을 위한 권한 정의
- Roles
	- EC2 인스턴스 또는 AWS 서비스를 식별하는데 사용
- Security
	- MFA + 비밀번호 정책
- AWS CLI
	- AWS 서비스를 관리할 수 있는 CLI
- AWS SDK
	- 프로그래밍 언어를 사용하여 AWS 서비스를 관리할 수 있는 패키지
- Access Keys
	- CLI 또는 SDK 를 통해 AWS에 접근하기 위한 키
- Audit
	- IAM Credential Reports (자격 증명 보고서) & IAM Access Advisor

## Users & Groups

![[iam_users_&groups.png]]

## Permissions

![[iam_permissions.png]]

## IAM 정책 상속(Inheritance)

![[iam_policies_inheritance.png]]

##  IAM 정책 파일 구조(Structure)

![[iam_policies_structure.png]]


## 비밀번호 정책

![[iam_password_policy.png]]

## IAM 모범 사례

![[iam_guidelines_&_best_practices.png]]


---
출처: [유데미 AWS DVA-CO2 시험 합격!](https://www.udemy.com/course/best-aws-certified-developer-associate/?couponCode=KEEPLEARNING)