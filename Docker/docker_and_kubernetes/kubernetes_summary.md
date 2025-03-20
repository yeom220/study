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

## 데이터 유형

![[understanding_state.png]]
- **유저 관련 데이터**
	- 주로 데이터베이스에 저장.
- **애플리케이션에서 생성된 임시 데이터**
	- 주로 메모리에 저장.

## 쿠버네티스 볼륨

![[kubernetes_volumes.png]]
- **다양한 볼륨 유형 및 드라이버 지원**
	- 로컬 볼륨들 (`Node` 의존)
	- 클라우드 프로바이저 볼륨들
- **`Pod` 에 의존하는 볼륨**
	- 컨테이너가 재시작 하거나 삭제되어도 볼륨 유지.
	- `Pod` 가 삭제될 경우 볼륨도 삭제.

## 쿠버네티스 볼륨 VS 도커 볼륨

![[difference_kuber_docker.png]]
- **쿠버네티스 볼륨**
	- 많은 타입 및 드라이버 지원.
	- 볼륨이 반드시 영구적인 것은 아니다.
	- 컨테이너가 재시작 하거나 삭제되어도 볼륨은 남는다.
- **도커 볼륨**
	- 기본적으로 타입 및 드라이버를 지원하지 않는다.
	- 볼륨은 직접 제거할 때까지 유지된다.
	- 컨테이너가 재시작 하거나 삭제되어도 볼륨은 남는다.

## 쿠버네티스 볼륨 종류

### emptyDir 볼륨

>`Pod`의 수명을 공유하는 임시 디렉토리.
>`Pod`가 삭제되면 같이 삭제됨.
>`Pod`에 종속적인 볼륨으로 `Pod`가 여러 개인 경우 데이터가 공유되지 않음.
>`Pod` 내부 `Containers` 사이에는 데이터 공유.

**Pod 정의 YAML**
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

**Pod 정의 YAML**
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

![[persistent_volumes.png]]

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
	storageClassName: standard
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
			- 볼륨 크기를 최대 1GB로 정의.
	- `volumeMode: Filesystem`
	- `storageClassName: standard`
		- `PV` 가 속한 `StorageClass` 정의.
		- `StorageClass` 는 쿠버네티스에서 관리자에게 스토리지 관리 방법과 볼륨 구성 방법을 세부적으로 제어할 수 있게 해주는 개념.
		- `minikube` 클러스터에는 `standard` 스토리지 클래스가 있음.
	- `accessModes:`
		- 볼륨의 읽기/쓰기 범위 정의.
		- `- ReadWriteOnce`
		- `- ReadOnlyMany`
		- `- ReadWriteMany`
	- `hostPath:`
		- 볼륨 유형 정의.
		- **hostPath는 단일 노드 환경(테스트 환경) 에서만 사용 가능.**

### 영구 볼륨 클레임(PV Claim)

>`Persistent Volume`(영구 볼륨)을 요청하는 방법.
>`Pod` 가 `Persistent Volume` 에 접근하기 위한 인터페이스.
>`PVC` 는 `PV` 와 1:1로 매핑되어, 하나의 `PVC` 는 하나의 `PV` 에만 바인딩 가능.

![[persistent_volumes_claims.png]]

**영구 볼륨 클레임 정의 YAML**
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
	name: host-pvc
spec:
	volumeName: host-pv
	accessModes:
		- ReadWriteOnce
	storageClassName: standard
	resources:
		requests:
			storage: 1Gi
```
- `spec:`
	- `volumeName: host-pv`
		- 바인딩 할 특정 볼륨 정의.
		- `volumeName` 이 정의 되지 않은 경우, 쿠버네티스가 `accessModes` 와 `resources` 를 수용하는 적절한 `PV` 를 바인딩.
	- `accessModes:`
		- `PVC`가 바인딩 요청할 볼륨의 읽기/쓰기 범위 정의.
		- **`PV` 의 accessModes와 일치하거나 부분 집합이어야 함.**
		- `- ReadWriteOnce`
	- `storageClassName: standard`
		- `PVC` 가 요청하는 `StorageClass` 지정.
		- 지정 하지 않으면 기본 스토리지 클래스 사용.
	- `resources:`
		- 클레임에 필요한 리소스 정의.
		- `requests:`
			- `storage: 1Gi`
				- 1GB의 스토리지 요청.

**Pod 볼륨을 PVC로 정의**
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
			  persistentVolumeClaim:
				  claimName: host-pvc
```
- `persistentVolumeClaim:`
	- 볼륨 유형을 `PVC` 로 정의.
	- `claimName: host-pvc`
		- 볼륨으로 사용할 `PVC` 정의.

### 볼륨 VS 영구 볼륨

![[normal_volumes_persistent_volumes.png]]
- **일반 볼륨**
	- 볼륨이 `Pod` 에 생성되어, `Pod` 생명주기를 따른다.
	- `Pod` 와 같이 정의하고 생성된다.
	- 반복적이고 글로벌 수준에서 관리하기 어렵다.
- **영구 볼륨**
	- 독립형 클러스터 리소스.
	- 독립 실행형으로 생성되고, `PVC` 를 통해 연결.
	- 한번 정의하여 여러 번 사용 가능.

### 그 외 볼륨 유형
- [쿠버네티스 볼륨 유형 문서](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume/)

---
## 환경 변수

### 환경 변수 직접 정의

**deployment.yaml**
```yaml
...
	spec:
	  containers:
	    - name: story
		  image: yeom220/kub-data-demo:2
	      env:
		    - name: STORY_DIR
	          value: 'story'
          volumeMounts:
            - mountPath: /app/story
              name: story-volume
...
```
- `env:`
	- `- name: STORY_DIR`
		- 환경변수 명을 `STORY_DIR` 로 정의.
	- `value: 'story'`
		- 환경변수 값 'story' 대입.

### ConfigMap 사용하여 환경 변수 정의

**environment.yaml**
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: data-store-env
data:
  folder: 'story'
```
- `data:`
	- `folder: 'story`
		- `{key}:{value}` 로 환경변수 정의.

**deployment.yaml**
```yaml
...
	spec:
	  containers:
	    - name: story
		  image: yeom220/kub-data-demo:2
	      env:
		    - name: STORY_DIR
	          valueFrom:
		        configMapKeyRef:
		          name: data-store-env
		          key: folder
          volumeMounts:
            - mountPath: /app/story
              name: story-volume
...
```
- `valueFrom:`
	- `configMapKeyRef:`
		- `name: data-store-env`
			- 쿠버네티스에 등록된 configMap 이름
		- `key: folder`
			- 사용할 환경 변수 `key` 지정.

---
# 쿠버네티스 네트워크

## 하나의 Pod 안에 있는 다중 컨테이너 통신

>동일 `Pod` 내부 컨테이너들은 **"localhost"** 키워드로 서로 통신이 가능하다.
>`Auth API` 컨테이너 와 `Users API` 컨테이너 는 동일 `Pod` 에 있으며 `Users API` 에서 `Auth API` 로 통신하는 시나리오.

![[kubernetes_network_first_sinario.png]]

**users-app.js**
```js
app.post('/singup', async (req, res) => {
  ...
  try {
    const hashedPW = await axios.get(
      `http://${process.env.AUTH_ADDRESS}/hashed-password/` + password
    );
    res.status(201).json({ message: 'User created!' });
    
  } catch (err) {
    return res.status(500).json({
      message: 'Creating the user failed - please try again later.'
    });
  }
});
```
- `Users API` 로 '/signup' 요청했을 때 `Auth API` 에서 해싱된 패스워드를 받아오는 프로세스.

**users-deployment.yaml**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: users-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: users
  template:
    metadata:
      labels:
        app: users
    spec:
      containers:
        - name: users
          image: yeom220/kub-demo-users:latest
          env:
            - name: AUTH_ADDRESS
              value: localhost
	    - name: auth
	      image: yeom220/kub-demo-auth:latest
```
- `containers:`
	- 하나의 `Pod` 에 `Users API` 와 `Auth API` 컨테이너 생성.
	- `env:`
		- `- name: AUTH_ADDRESS`
		- `value: localhost`
			- 동일 Pod에 있는 컨테이너들은 localhost 로 통신 가능.

**users-service.yaml**
```yaml
apiVersion: v1
kind: Service
metadata:
  name: users-service
spec:
  selector:
    app: users
  type: LoadBalancer
  ports:
    - protocol: TCP
      port: 8080
      targetPort: 8080
```
- `type: LoadBalancer`
	- 서비스를 로드 밸런서 타입으로 생성하여 외부 노출

---
## 클러스터 내부 다중 컨테이너 통신

>쿠버네티스는 서비스 생성시 환경변수를 각 `Pod`의 `ClusterIP` 를 가진 환경변수를 자동으로 생성해준다.
>각각의 `Pod` 에 있는 `Auth API`, `Users API`, `Tasks API` 컨테이너들이 통신하는 시나리오.

![[kubernetes_network_last_sinario.png]]

**users-service.yaml**
```yaml
apiVersion: v1
kind: Service
metadata:
  name: users-service
spec:
  selector:
    app: users
  type: LoadBalancer
  ports:
    - protocol: TCP
      port: 8080
      targetPort: 8080
```

**auth-service.yaml**
```yaml
apiVersion: v1
kind: Service
metadata:
  name: auth-service
spec:
  selector:
    app: auth
  type: ClusterIP
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
```
- `type: ClusterIP`
	- `Auth API`는 외부 노출 없이 내부에서만 통신하기 위해 ClusterIP 타입 서비스 생성.

**users-deployment.yaml**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: users-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: users
  template:
    metadata:
      labels:
        app: users
    spec:
      containers:
        - name: users
          image: yeom220/kub-demo-users:latest
          env:
            - name: AUTH_ADDRESS
              value: "10.105.102.32"
```
- `env:`
	- `- name: AUTH_ADDRESS`
	- `value: "10.105.102.32"`
		- auth-service 의 ClusterIP.
		- auth-service 가 삭제되기 전에는 변경되지 않는다.

**auth-deployment.yaml**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: auth-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: auth
  template:
    metadata:
      labels:
        app: auth
    spec:
      containers:
	    - name: auth
	      image: yeom220/kub-demo-auth:latest
```

**users-app.js**
```js
app.post('/singup', async (req, res) => {
  ...
  try {
    const hashedPW = await axios.get(
      `http://${process.env.AUTH_ADDRESS}/hashed-password/` + password
    );
    res.status(201).json({ message: 'User created!' });
    
  } catch (err) {
    return res.status(500).json({
      message: 'Creating the user failed - please try again later.'
    });
  }
});

app.post('/login', async (req, res) => {
  ...
  const response = await axios.get(
    `http://${process.env.AUTH_SERVICE_SERVICE_HOST}/token/` + hashedPassword + '/' + password
  );
  if (response.status === 200) {
    return res.status(200).json({ token: response.data.token });
  }
  return res.status(response.status).json({ message: 'Logging in failed!' });
});
```
- `${process.env.AUTH_SERVICE_SERVICE_HOST}`
	- 쿠버네티스가 자동으로 생성하는 환경변수.
		- `{서비스명의 대문자 스네이크 케이스}_SERVICE_HOST` 로 생성.
	- auth-service 의 ClusterIP 값을 가짐.

### 클러스터 내부 Pod DNS 통신

>쿠버네티스는 CoreDNS를 DNS 서버로 사용한다.
>쿠버네티스에서 CoreDNS의 역할
>- 기본 DNS 서버
>	- 쿠버네티스 1.13 버전 이후 기본 DNS 서버로 채택.
>- 서비스 디스커버리
>	- 클러스터 내의 Service 와 Pod 간 네트워크 통신 관리.
>- 이름 해석
>	- 클러스터 내부에서 서비스 이름을 IP 주소로 변환 (예: my-service.default.svc.cluster.local -> 10.0.0.1)
>- 외부 도메인 쿼리
>	- 클러스터 외부 도메인에 대한 쿼리를 외부 DNS 서버로 전달.
>- 배포 방식
>	- 쿠버네티스 클러스터에서 coredns라는 이름의 Deployment로 배포되며, 각 노드에서 DNS 요청을 처리.
>- 구성 관리
>	- CoreDNS의 설정은 ConfigMap을 통해 관리되며, Corefile 이라는 설정 파일로 정의.

**users-deployment.yaml**
```yaml
...
	containers:
	  - name: users
	    image: yeom220/kub-demo-users:latest
	    env:
	      - name: AUTH_ADDRESS
	        value: "auth-service.default"
```
- `env:`
	- `- name: AUTH_ADDRESS`
	- `value: "auth-service.default"`
		- 쿠버네티스 DNS 서버를 통해 IP로 변환.
		- `"auth-service.default"`
			- auth-service는 서비스 명이고 default는 네임스페이스로, `Service` 및 `Deployment` 의 기본 네임스페이스가 default.

**tasks-deployment.yaml**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: tasks-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: tasks
  template:
    metadata:
      labels:
        app: tasks
    spec:
      containers:
        - name: tasks
          image: yeom220/kub-demo-tasks:latest
          env:
            - name: TASKS_FOLDER
              value: tasks
            - name: AUTH_ADDRESS
              value: auth-service.default
```

**tasks-service.yaml**
```yaml
apiVersion: v1
kind: Service
metadata:
  name: tasks-service
spec:
  selector:
    app: tasks
  type: LoadBalancer
  ports:
    - protocol: TCP
      port: 8000
      targetPort: 8000
```

### 클러스터 내부 프론트엔드 앱 배포

**App.js (React)**
```js
function App() {
  const [tasks, setTasks] = useState([]);

  const fetchTasks = useCallback(function () {
    fetch(`http://127.0.0.1:58313/tasks`, {
      headers: {
        'Authorization': 'Bearer abc'
      }
    })
      .then(function (response) {
        return response.json();
      })
      .then(function (jsonData) {
        setTasks(jsonData.tasks);
      });
  }, []);

  useEffect(
    function () {
      fetchTasks();
    },
    [fetchTasks]
  );

  function addTaskHandler(task) {
    fetch(`http://127.0.0.1:58313/tasks`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: 'Bearer abc',
      },
      body: JSON.stringify(task),
    })
      .then(function (response) {
        console.log(response);
        return response.json();
      })
      .then(function (resData) {
        console.log(resData);
      });
  }

  return (
    <div className='App'>
      <section>
        <NewTask onAddTask={addTaskHandler} />
      </section>
      <section>
        <button onClick={fetchTasks}>Fetch Tasks</button>
        <TaskList tasks={tasks} />
      </section>
    </div>
  );
}

export default App;
```
- React 로 구현된 프론트엔드 코드

**frontend-deployment.yaml**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: frontend
  template:
    metadata:
      labels:
        app: frontend
    spec:
      containers:
        - name: frontend
          image: yeom220/kub-demo-frontend:latest
```

**frontend-service.yaml**
```yaml
apiVersion: v1
kind: Service
metadata:
  name: frontend-service
spec:
  selector:
    app: frontend
  type: LoadBalancer
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
```

#### 리버스 프록시 사용

>위의 프론트엔드 앱 코드에는 1가지 문제점이 있다.
>```js
>fetch(`http://127.0.0.1:58313/tasks`, {
>  headers: {
       'Authorization': 'Bearer abc'
    }
  })
>```
>API 요청을 위한 URL(호스트)이 브라우저에서 해석되기 때문에 환경에 따라 작동되지 않을 수 있다.
>이를 해결하기 위해 웹서버(Nginx)의 리버스 프록시를 사용해본다.

**App.js (React)**
```js
function App() {
...

  const fetchTasks = useCallback(function () {
    fetch(`/api/tasks`, {
      headers: {
        'Authorization': 'Bearer abc'
      }
...

  function addTaskHandler(task) {
    fetch(`/api/tasks`, {
      method: 'POST',
...
}

export default App;
```

**nginx.conf**
```conf
server {
  listen 80;

  location /api/ {
    proxy_pass http://tasks-service.default:8000/;
  }

  location / {
    root /usr/share/nginx/html;
    index index.html index.htm;
    try_files $uri $uri/ /index.html =404;
  }

  include /etc/nginx/extra-conf.d/*.conf;
}
```
- Nginx 설정 파일.
- `location /api/ {}`
	- `/api/` 로 시작하는 모든 요청을 처리 방식을 정의.
	- `proxy_pass http://tasks-service.default:8000/;`
		- 리버스 프록시 지시어로 `/api/` 로 오는 모든 요청을 `http://tasks-service.default:8000/` 로 전달
	- `tasks-service.default` 는 클러스터 내부에서만 사용할 수 있는 변수이기 때문에 App.js 에 직접 작성하면 브라우저에서는 404 에러가 발생하지만, Nginx 서버는 클러스터 내부에서 실행되기 때문에 `Cluster-IP` 로 변환 된다.

---
출처: [유데미 Docker & Kubernetes: 실전가이드](https://www.udemy.com/course/docker-kubernetes-2022/?couponCode=24T4MT180225)
