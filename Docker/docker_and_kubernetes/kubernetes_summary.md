# 애플리케이션 서비스 중 발생할 수 있는 문제들

>- 컨테이너가 충돌 되거나 중지되어, 새로운 컨테이너로 교체되어야 할 수 있다.
>- 트래픽에 따라 컨테이너 수가 증가할 필요가 있다.
>- 트래픽이 각각의 컨테이너에 균일하게 분배 되어야 한다.
>
>**호스팅 프로바이더 서비스(ECS) 사용시 위의 문제들이 해결될 수 있다.**
>하지만 프로바이더마다 설정 방법이 달라, 프로바이더를 변경해야할 때 해당 프로바이더 서비스에 대해 학습이 필요하다. 결국 해당 솔루션에 종속된다.
>
>**쿠버네티스는 이러한 문제들을 해결하기 위해 시작된 오픈소스 이다.**

---
# 쿠버네티스 ?

>쿠버네티스를 한마디로 정의하면 **"멀티 머신을 위한 도커 컴포즈"** 이다.
>쿠버네티스는 컨테이너화된 애플리케이션의 대규모 배포, 스케일링 및 관리를 자동화하는 오픈소스 컨테이너 오케스트레이션 플랫폼이다.

### 주요 특징

- **자동화된 운영**
	- 컨테이너의 배포, 확장 관리를 자동화하여 수동 프로세스를 최소화한다.
- **자동 복구**
	- 실패한 컨테이너를 자동으로 재시작하고, 노드 장애 시 다른 노드로 컨테이너를 이동한다.
- **로드 밸런싱**
	- 트래픽을 자동으로 분산시켜 애플리케이션의 안정성을 높인다.
- **확장성**
	- 명령어 하나로 컨테이너의 수를 쉽게 조절 가능하다.

![[what_is_kubernetes.png]]

### 쿠버네티스가 필요한 이유?

>컨테이너들의 구조를 정의하고, 클라우드 프로바이더 설정을 추가하면 어느 클라우드 프로바이더 또는 원격 머신에서도 동작한다.

![[why_kubernetes.png]]

---
# 쿠버네티스 아키텍처

![[kubernetes_architecture.png]]

### 워커 노드

![[worker_node_details.png]]

### 마스터 노드

![[master_node_details.png]]

### 코어 컴포넌트

![[kubernetes_core_components.png]]
- 클러스터(Cluster)
	- 노드 머신들의 구성
- 노드(Nodes)
	- 한개 또는 여러 파드(Pods)를 호스팅 하는 물리 또는 가상 머신
	- 마스터 노드(Master Node)
		- 워커 노드를 통해 파드를 관리하는 클러스터 컨트롤 플레인
	- 워커 노드(Worker Node)
		- 컨테이너가 실행되는 호스트 파드
- 파드(Pods)
	- 실행되는 애플리케이션 컨테이너와 그에 필요한 리소스를 포함하는 것
	- 쿠버네티스의 가장 기본적인 배포 단위
- 컨테이너(Containers)
	- 일반적인 컨테이너
- 서비스(Services)
	- 독립적인 IP 주소를 가진 파드들의 논리적 집합

---
# 쿠버네티스 자동화와 설정

![[kubernetes_work.png]]
- 쿠버네티스가 해주는 작업
	- `Pods` 의 생성 및 관리
	- `Pods` 모니터링을 통한 스케일링 및 재생성
	- 클라우드 리소스를 활용하여 구성을 적용
- 직접 해야 하는 작업
	- Cluster 및 Node 인스턴스 생성 (워커 + 마스터 노드)
	- API 서버, kubelet 및 기타 쿠버네티스 서비스들 노드에 설치
	- 필요시 클라우드 프로바이더 리소스 생성(Load Balancer, Filesystems)

---
# 쿠버네티스 작동 방식

>`kubectl` kube control은 클러스터의 마스터 노드에 `Deployment`, `Service` 등의 워커 노드를 제어할 동적 객체를 조정하는 명령을 보내는 툴이다.
>`Master Node` 는 기본적으로 명령을 적용하고 올바르게 실행되도록 하며 클러스터 내부에 존재한다.

![[how_to_work_kubenetes.png]]

## Kubernetes Objects

>쿠버네티스는 객체와 함께 동작한다.

![[kubernetes_objects.png]]
### Pod object

![[pod_object.png]]
- 쿠버네티스와 상호 작용하는 가장 작은 유닛.
- 1개 이상의 `Container` 를 실행.
- 모든 `Pod Containers` 의 공유된 리소스를 포함.
- 기본적으로 클러스터 내부 IP를 가짐
- `Pod` 내부의 `Containers` 은 `localhost`로 통신이 가능.
- `Pod` 는 `Container` 처럼 임시적으로 디자인 됨.
	- `Pod` 가 교체되거나 제거되면 데이터도 사라짐.

### Deployment object 

![[deployment_object.png]]
- `Pods` 을 컨트롤 하는 객체 (컨트롤러).
- 구성을 정의하면 쿠버네티스가 실행.
	- 사용자는 실행할 `Pods` 와 `Containers` 및 인스턴스 수를 정의.
- `Deployment` 는 일시중지, 삭제, 롤백이 가능.
- `Deployment` 는 오토 스케일링이 가능.
	- 사용자는 필요시 `Pods` 개수를 조절할 수 있다.
- `Deployment` 는 `Pods` 를 관리하고, 여러 개 생성이 가능.
- 사용자는 직접적으로 `Pods` 를 컨트롤 하지 않고, `Deployment` 에 구성을 정의하여 `Deployment` 가 자동으로 컨트롤 하도록 한다.

**Deployment 객체 생성**
```bash
$ kubectl create deployment first-app --image=yeom220/kub-first-app
```
- `create deployment first-app`
	- `deployment` 객체 생성 명령어
	- `first-app` 은 `deployment` 객체명
- `--image=yeom220/kub-first-app`
	- `deployment` 가 컨트롤할 `pod` 의 `container` 이미지 지정

**Deployment 객체 조회**
```bash
$ kubectl get deployments
```

**Deployment 객체 제거**
```bash
$ kubectl delete deployment first-app
```

**Deployment 직접 스케일링**
```bash
$ kubectl scale deployment/first-app --replicas=3
```
- `scale deployment/first-app`
	- first-app `Deployment` 객체에 스케일 명령.
- `--replicas=3`
	- `Pod` 객체를 3개로 지정.

**Deployment 업데이트**
```bash
$ kubectl set image deployment/first-app kub-first-app=yeom220/kub-first-app:2
```
- `set image deployment/first-app kub-first-app=yeom220/kub-first-app:2`
	- `first-app` `Deployment` 내부 `Pods`의 `kub-first-app` `Container` 의 이미지를 `yeom220/kub-first-app:2` 로 변경.
	- 실제 이미지가 달라졌다고 해도, 이미지 지정시 태그가 같으면 같은 이미지로 인식하여 업데이트 되지 않음.

**Deployment 업데이트 상태 확인**
```bash
$ kubectl rollout status deployment/first-app
```
- `rollout status deployment/first-app`
	- `first-app` `Deployment` 객체의 업데이트 상태 출력.
- **`Deployment` 객체의 업데이트는 `RollingUpdate` 방식으로 새로운 `Pods` 생성이 성공하면 새로운 `Pods` 로 변경한다.**
	- 실패시 성공할 때까지 기존 `Pods` 를 종료하지 않고 대기.

**Deployment 롤백**
```bash
$ kubectl rollout undo deployment/first-app
```
- `rollout undo deployment/first-app`
	- `first-app` `Deployment` 의 마지막 업데이트 사항을 취소한다.

**Deployment 특정 버전으로 롤백**
```bash
$ kubectl rollout history deployment/first-app
deployment.apps/first-app
REVISION  CHANGE-CAUSE
1         <none>
3         <none>
4         <none>
```
- `rollout history deployment/first-app`
	- `first-app` `Deployment` 변경 이력 조회.

```bash
$ kubectl rollout history deployment/first-app --revision=1
```
- `--revision=1`
	- 리비전 1의 구성 상세 조회.

```bash
$ kubectl rollout undo deployment/first-app --to-revision=1
```
- `--to-revision=1`
	- `1` 리비전으로 롤백.

### `kubectl` 작동 방식

![[how_to_work_kubectl.png]]
- `kubectl create` 명령어가 마스터 노드(컨트롤 플레인)에 전달.
- 스케줄러(`Scheduler`)는 현재 동작 중인 `Pods` 를 분석하고, 새로운 `Pods` 를 위한 최적의 노드를 찾는다.
- 선택된 워커 노드의 `kubelet` 서비스는 `Pod`를 관리하고, `Pod` 에서 `Container` 를 시작하고, 이 `Pod` 를 모니터링 한다.
	- `Pod` 는 `Deployment` 객체를 생성할 때 지정한 이미지를 기반으로 하는 `Container` 를 포함한다.

### Service Object

![[service_object.png]]
- `Service` 객체는 `Pods` 를 클러스터 또는 외부(웹)에 노출한다.
- `Pods` 는 기본적으로 내부 IP를 가지고 있지만, 외부에서 접근이 불가하고, `Pod` 이 교체될 때마다 변경된다.
	- IP 가 유동적이기 때문에 `Pods` 를 찾는 데 매우 어렵다.
- `Service` 는 `Pods` 를 그룹화 하고, 공유 주소, 공유 IP를 제공한다.
	- 해당 IP는 고정적이다.
- `Service` 는 `Pods` 의 외부 접속을 허용할 수 있다.
	- 기본값은 내부 전용이지만, `Service` 를 사용하여 덮어 쓸 수 있다.

**Service 객체 생성 및 외부 노출**
```bash
$ kubectl expose deployment first-app --type=LoadBalancer --port=8080
```
- `expose deployment first-app`
	- first-app `Deployment` 객체를 노출
- `--type=LoadBalancer`
	- 해당 `Service` 에 대한 고유 주소를 생성 및 노출.
	- `--type` 다른 설정들.
		- `--type=ClusterIP`
			- 기본값으로 클러스터 내부에서만 연결 가능.
		- `--type=NodePort`
			- 워커 노드 IP 주소를 통해 노출.
- `--port=8080`
	- 노출 포트로 `Container` 노출 포트에 매핑

---
# 명령적 VS 선언적 접근 방식

![[difference_of_imperative_declarative.png]]
- 명령적 접근 방식(Imperative)은 터미널에 각각 명령어를 사용하는 방식
- 선언적 접근 방식(Declarative)은 `YAML` 파일에 각 객체의 구성을 정의하는 방식

### 선언적 접근 방식 YAML 파일

**deployment.yaml(yml)**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: second-app-deployment
  labels:
    group: example
spec:
  replicas: 1
  selector:
	matchLabels:
	  app: second-app
	  # tier: backend
	# matchExpressions:
	#	- {key: app, operator: In, values: [second-app, first-app]}
  template:
    # kind: Pod
	metadata:
	  labels:
		app: second-app
		tier: backend
	spec:
	  containers:
		- name: second-node
		  image: yeom220/kub-first-app
		  imagePullPolicy: Always
		  livenessProbe:
			httpGet:
			path: /
			port: 8080
			periodSeconds: 10
			initialDelaySeconds: 5
		# - name: third-node
		#   image: yeom220/kub-first-app:8081
```
- `apiVersion: apps/v1`
	- 문서 버전 정의.
- `kind: Deployment`
	- 어떤 객체를 정의한 문서인지 정의 (`Deployment`)
- `metadata:`
	- `Deployment` 객체의 메타데이터 정의
	- `name: second-app-deployment`
		- `Deployment` 객체 이름 정의.
	- `labels:`
		- `group: example`
			- 레이블은 `key: value` 로 정의.
			- `second-app-deployment` `Deployment` 객체는 `group: example` 레이블을 가짐.
- `spec:`
	- `Deployment` 객체 구조 정의.
	- `replicas: 1`
		- 초기 생성할 `Pods` 수 정의 (1개).
	- `selector:`
		- 쿠버네티스에서 레이블을 기반으로 리소스를 선택하고 필터링 하는 메커니즘.
		- `matchLabels:`
			- `app: second-app`
				- 레이블이 `app: second-app` 인 `Pods`를 해당 `Deployment` 가 관리하도록 정의.
		- `matchExpressions:`
			- 리소스를 선택하는 다른 방법.
	- `template:`
		- `Deployment` 가 관리할 `Pod` 의 구조 정의.
		- `metadata:`
			- `Pod` 객체의 메타데이터 정의.
			- `labels:`
				- `app: second-app`
		- `spec:`
			- `Pod` 객체 구조 정의.
			- `containers:`
				- `- name: second-node`
					- `Container` 이름 정의.
				- `image: yeom220/kub-first-app`
				- `imagePullPolicy: Always`
					- 쿠버네티스는 기본적으로 이미지 태그가 변경되지 않으면 업데이트 되지 않는데, 해당 옵션을 `Always`로 설정하면 태그가 변경되지 않아도 항상 이미지를 `Pull` 하여 업데이트 한다.
				- `livenessProbe:`
					- 쿠버네티스에서 컨테이너의 건강 상태를 확인하는 메커니즘.
					- `httpGet:`
						- `path: /`
						- `port: 8080`
						- HTTP GET 메소드로 8080 포트의 `/` 경로로 확인하도록 정의.
					- `periodSeconds: 10`
						- 건강 상태 체크 주기 (초 단위).
					- `initialDelaySeconds: 5`
						- 컨테이너 생성 후 최초 체크까지의 시간 (초 단위).


**service.yaml(yml)**
```yaml
apiVersion: v1
kind: Service
metadata:
  name: second-service
  labels:
    group: example
spec:
  selector:
    app: second-app
    tier: backend
  ports:
    - protocol: 'TCP'
      # name: 'second-node'
      port: 80
      targetPort: 8080
    # - protocol: TCP
    #  name: 'third-node'
    #  port: 8081
    #  targetPort: 8081
  type: LoadBalancer
```
- `apiVersion: v1`
	- 문서 버전 정의.
- `kind: Service`
	- `Service` 객체 문서 정의.
- `metadata:`
	- `Service` 객체 이름을 `second-service` 로 정의.
	- 레이블을 `group: example` 로 정의.
- `spec:`
	- `Service` 객체 구조 정의.
	- `selector:`
		- `deployment.yaml` 의 `selector`와 동일하지만, 현재까지는 `matchLabels` 방식만 지원. (`key: value`)
	- `ports:`
		- 외부에 노출할 포트 정의.
		- `- protocol: 'TCP'`
			- IP 프로토콜을 `TCP` 로 정의 (기본값)
			- `UDP`, `SCTP` 정의 가능.
		- `name: 'second-node'`
			- `Service` 포트의 이름 정의.
			- `DNS_LABEL` 형식을 따라야 함. 
			- `Service` 내에 고유해야 함.
			- `Service` 포트가 1개일 때는 생략 가능.
		- `port: 80`
			- 해당 `Service` 에 의해 노출되는 포트.
		- `targetPort: 8080`
			- `Service` 가 타겟으로 하는 포드에 접근할 포트 번호 또는 이름.
			- 숫자인 경우, 1~65545 범위 내여야 함 (포트 범위)
			- 문자인 경우, `IANA_SVC_NAME` 형식을 따라야 함.
			- 지정하지 않으면, `port` 필드 값이 사용됨.
			- `Service` 로 들어온 트래픽을 파드의 어떤 포트로 전달할지 정의.
	- `type: LoadBalancer`
		- `Service` 의 노출 방식을 정의.
		- 유효한 옵션
			- `ClusterIP`(기본값)
			- `ExternalName`
			- `ClusterIP`
			- `NodePort`
			- `LoadBalancer`

---
# 쿠버네티스 데이터 & 볼륨 관리

## 쿠버네티스 볼륨 VS 도커 볼륨


## 쿠버네티스 볼륨 종류

### emptyDir 볼륨

>`Pod`의 수명을 공유하는 임시 디렉토리.
>`Pod`가 삭제되면 같이 삭제됨.
>`Pod`에 종속적인 볼륨으로 `Pod`가 여러 개인 경우 데이터가 공유되지 않음.
>`Pod` 내부 `Containers` 사이에는 데이터 공유.

```yaml
...
	spec:
		containers:
			- name: story
			  image: yeom220/kub-data-demo:1
			  volumeMounts:
				  - mountPath: /app/story
				    name: story-volume
		volumes:
			- name: story-volume
			  emptyDir: {}
```
- `volumeMounts:`
	- `Pod containers` 에 마운트 할 볼륨 정의.
	- `- mountPath: /app/story`
		- 컨테이너 내부 `/app/story` 디렉토리를 볼륨에 마운트
	- `name: story-volume`
		- 마운트 할 볼륨 이름 정의.
- `volumes:`
	- 볼륨 정의(생성).
	- `- name: story-volume`
		- `story-volume` 볼륨 생성.
	- `emptyDir: {}`
		- 볼륨 유형 정의.

### hostPath 볼륨

>컨테이너에 직접 노출되는 호스트 머신(워커노드)의 기존 파일이나 디렉토리.
>도커의 바인드 마운트와 비슷한 개념.
>`Node` 에 종속적인 볼륨으로 다른 `Node` 와 데이터가 공유되지 않음.
>`Node` 내부 `Pods` 사이에는 데이터 공유. 

```yaml
...
	spec:
		containers:
			- name: story
			  image: yeom220/kub-data-demo:1
			  volumeMounts:
				  - mountPath: /app/story
				    name: story-volume
		volumes:
			- name: story-volume
			  hostPath:
				  path: /data
				  type: DirectoryOrCreate
```
- `hostPath:`
	- 볼륨 유형 정의.
	- `path: /data`
		- 호스트 머신의 경로.
	- `type: DirectoryOrCreate`
		- 호스트 머신에 `/data` 디렉토리가 없는 경우 생성하도록 정의.

### CSI 볼륨

>**Container Storage Interface** 의 약자로 외부 스토리지와 연결할 수 있도록 제공되는 인터페이스.
>예를 들어 **AWS EFS CSI** 와 같은 드라이버를 사용하면 **AWS EFS** 스토리지 서비스와 쉽게 연결할 수 있다.

### 영구 볼륨(Persistent Volume)

>`Node` 와 `Pod` 에 종속되지 않고, 독립성을 가진 볼륨.
>모든 `Node` 및 `Pod` 와 공유 가능한 데이터.
>`Cluster` 에 새 리소스, 새 엔티티를 가진 볼륨을 생성하고, 각 `Node` 에 `PV Claim` 을 생성하여 영구 볼륨에 액세스 한다.
>각 영구 볼륨에 대해 각각의 `Claim` 을 가짐.

**영구 볼륨 정의 YAML**
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
	name: host-pv
spec:
	capacity:
		storage: 1Gi
	volumeMode: Filesystem # or Block
	accessModes:
		- ReadWriteOnce
		# - ReadOnlyMany
		# - ReadWriteMany
	hostPath:
		path: /data
		type: DirectoryOrCreate
```
- `kind: PersistentVolume`
	- 영구 볼륨 정의
- `spec:`
	- [PV spec 문서](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes)
	- `capacity:`
		- `storage: 1Gi`
			- 볼륨 크기를 최대 1GB 로 정의.
	- `volumeMode: Filesystem`
	- `accessModes:`
		- 영구 볼륨에 접근 가능 범위 정의.
		- `- ReadWriteOnce`
		- `- ReadOnlyMany`
		- `- ReadWriteMany`
	- `hostPath:`
		- 볼륨 유형 정의.
		- **hostPath는 단일 노드 환경(테스트 환경) 에서만 사용 가능.**

### 그 외 볼륨 유형
- [쿠버네티스 볼륨 유형 문서](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume/)



출처: [유데미 Docker & Kubernetes: 실전가이드](https://www.udemy.com/course/docker-kubernetes-2022/?couponCode=24T4MT180225)
