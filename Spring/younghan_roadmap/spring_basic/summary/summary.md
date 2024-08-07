# 스프링 핵심 원리 - 기본편 요약
---

## 0.강의 소개
### 목표
- SOLID
- 스프링 기본 기능 학습
- 스프링 본질 깊은 이해
- 객체 지향 설계를 고민하는 개발자로 성장

## 1.객체 지향 설계와 스프링
- 자바 진영의 추운 겨울과 스프링 탄생
- J2EE(EJB)
- POJO
- 스프링이란?
	- 필수
		- 스프링 프레임워크
		- 스프링 부트
	- 선택
		- 스프링 데이터
		- 스프링 세션
		- 스프링 시큐리티
		- 스프링 Rest Docs
		- 스프링 배치
		- 스프링 클라우드
- 스프링 == DI 컨테이너
- 핵심개념
	- 왜 만들었는가?
		- 이전 EJB 의존성에 객체 지향 프로그래밍을 할 수 없었다. 
	- 핵심 컨셉?
		- 좋은 객체 지향 애플리케이션을 개발할 수 있게 돕는다.
- 좋은 객체 지향 프로그래밍이란?
	* 역할과 구현을 분리
	* 클라이언트는 대상의 역할(인터페이스)만 알면 된다.
	* 구현 대상 내부 구조를 몰라도 된다.
	* 구현 대상 내부 구조가 변경되어도 영향받지 않는다.
	* 구현 대상 자체를 변경해도 영향받지 않는다.
	* 자바의 다형성 활용
		* 역할 = 인터페이스
		* 클래스 = 구현
	* ***클라이언트를 변경하지 않고, 서버의 구현 기능을 유연하게 변경할 수 있다.***
	* ***인터페이스를 안정적으로 설계하는 게 중요!!***

- 좋은 객체 지향 설계의 5가지 원칙(SOLID)
	- SRP: 단일 책임 원칙
		- 중요한 기준은 변경, 변경이 있을 때 파급 효과가 적으면 잘 따른 것
	- OCP: 개방-폐쇄 원칙
		- 소프트웨어 요소는 확장에는 열려 있으나 변경에는 닫혀 있어야 한다.
		- 인터페이스를 구현한 새로운 클래스를 하나 만들어서 새로운 기능을 구현(다형성 활용)
	- LSP: 리스코프 치환 원칙
		- 프로그램의 객체는 프로그램의 정확성을 깨뜨리지 않으면서 하위 타입의 인스턴스로 바꿀 수 있어야 한다.
		- 다형성에서 하위 클래스는 인터페이스 규약을 다 지켜야 한다는 것, 다형성을 지원하기 위한 원칙, 인터페이스를 구현한 구현체는 믿고 사용하려면, 이 원칙이 필요하다.
	- ISP: 인터페이스 분리 원칙
		- 특정 클라이언트를 위한 인터페이스 여러 개가 범용 인터페이스 하나보다 낫다.
		- 자동차 인터페이스 -> 운전 인터페이스, 정비 인터페이스로 분리
	- DIP: 의존관계 역전 원칙
		- 프로그래머는 “추상화에 의존해야지, 구체화에 의존하면 안된다.” 의존성 주입은 이 원칙을 따르는 방법 중 하나다.
		- 구현 클래스에 의존하지 말고, 인터페이스에 의존해야한다.
		- MemberService는 인터페이스에 의존하지만, 구현 클래스도 동시에 의존한다.
		- MemberRepository m = new ***MemoryMemberRepository();** (DIP 위반)
	- 다형성 만으로는 구현 객체를 변경할 때 클라이언트 코드도 함께 변경된다.
	- 다형성 만으로는 OCP, DIP를 지킬 수 없다.

- 객체 지향 설계와 스프링
	- 스프링은 다음 기술로 다형성, OCP, DIP를 가능하게 지원
		- DI: 의존관계, 의존성 주입
		- DI 컨테이너 제공
	- 클라이언트 코드의 변경 없이 기능 확장이 가능
	- 코드가 추상화 되면서 생기는 단점도 있다.
		- 인터페이스를 도입하면 추상화라는 비용이 발생한다.
		- 기능을 확장할 가능성이 없다면, 구현 클래스를 직접 사용하고, 향후 꼭 필요할 때 리팩토링해서 인터페이스를 도입하는 것도 방법이다.  

## 2.스프링 핵심 원리 이해1 - 예제 만들기

### 비즈니스 요구사항과 설계
- 회원
	- 회원을 가입하고 조회할 수 있다.
	- 회원은 일반과 VIP 두 가지 등급이 있다.
	- 회원 데이터는 자체 DB를 구축할 수 있고, 외부 시스템과 연동할 수 있다.(미확정)
- 주문과 할인 정책
	- 회원은 상품을 주문할 수 있다.
	- 회원 등급에 따라 할인 정책을 적용할 수 있다.
	- 할인 정책은 모든 VIP는 1000원을 할인해주는 고정 금액 할인을 적용해달라.(나중에 변경 가능)
	- 할인 정책은 변경 가능성이 높다. 회사의 기본 할인 정책을 아직 정하지 못했고, 오픈 직전까지 고민을 미루고 싶다. 최악의 경우 할인을 적용하지 않을 수도 있다.(미확정)
- 화원 도메인 설계
	- 요구사항
		- 회원을 가입하고 조회할 수 있다.
		- 회원은 일반과 VIP 두 가지 등급이 있다.
		- 회원 데이터는 자체 DB를 구축할 수 있고, 외부 시스템과 연동할 수 있다.(미확정)
- 회원 도메인 개발
- 회원 도메인 실행과 테스트
- 주문과 할인 도메인 설계
	- 요구사항
		- 주문과 할인 정책 회원은 상품을 주문할 수 있다.
		- 회원 등급에 따라 할인 정책을 적용할 수 있다. 
		- 할인 정책은 모든 VIP는 1000원을 할인해주는 고정 금액 할인을 적용해달라. (나중에 변경 될 수 있다.) 
		- 할인 정책은 변경 가능성이 높다. 
		- 회사의 기본 할인 정책을 아직 정하지 못했고, 오픈 직전까지 고민을 미루 고 싶다. 
		- 최악의 경우 할인을 적용하지 않을 수 도 있다. (미확정)
- 주문과 할인 도메인 실행과 테스트

## 3.스프링 원리 이해2 - 객체 지향 원리 적용

- **새로운 할인 정책 개발**
	- 정액 할인에서 10% 정률 할인으로 변경
- **새로운 할인 정책 적용과 문제점**
	- 할인 정책을 변경하려면 클라이언트인 `OrderServiceImpl` 코드를 고쳐야 한다.
	```java
	public class OrderServiceImpl implements OrderService { 
	  // private final DiscountPolicy discountPolicy = new FixDiscountPolicy(); 
	  private final DiscountPolicy discountPolicy = new RateDiscountPolicy(); }
	  ```
	- 문제점
		- 우리는 역할과 구현을 충실하게 분리했다. OK 
		- 다형성도 활용하고, 인터페이스와 구현 객체를 분리했다. OK 
		- OCP, DIP 같은 객체지향 설계 원칙을 충실히 준수했다 
			- 그렇게 보이지만 사실은 아니다. 
		- DIP: 주문서비스 클라이언트( `OrderServiceImpl` )는 `DiscountPolicy` 인터페이스에 의존하면서 DIP를 지킨 것 같은데?
		- 클래스 의존관계를 분석해 보자. 추상(인터페이스) 뿐만 아니라 **구체(구현) 클래스에도 의존**하고 있다.
			- 추상(인터페이스) 의존: `DiscountPolicy` 
			- 구체(구현) 클래스: `FixDiscountPolicy` , `RateDiscountPolicy` 
		- OCP: 변경하지 않고 확장할 수 있다고 했는데! 
			- **지금 코드는 기능을 확장해서 변경하면, 클라이언트 코드에 영향을 준다!** 따라서 **OCP를 위반**한다.
		- 문제해결방법
			- 클라이언트 코드인 `OrderServiceImpl` 은 `DiscountPolicy` 의 인터페이스 뿐만 아니라 구체 클래스도 함께 의존한다. 
			- 그래서 구체 클래스를 변경할 때 클라이언트 코드도 함께 변경해야 한다. 
			- **DIP 위반** 추상에만 의존하도록 변경(인터페이스에만 의존) 
			- DIP를 위반하지 않도록 인터페이스에만 의존하도록 의존관계를 변경하면 된다.
- **관심사의 분리**
	- AppConfig 클래스 추가
		- 애플리케이션의 전체 동작 방식을 구성(config)하기 위해, **구현 객체를 생성**하고, **연결**하는 책임을 가지는 별도의 클래스를 만든다.
		- 구현객체의 생성과 연결은 AppConfig가 담당한다.
		- DIP 완성: MemberServiceImpl은 MemberRepository인 추상에만 의존한다.
		- 관심사의 분리: 객체를 생성하고 연결하는 역할과 실행하는 역할이 명확히 분리되었다.
		- 클라이언트인 `memberServiceImpl` 입장에서 의존관계를 마치 외부에서 주입해주는 것 같다고 해서 DI(Dependency Injection), 의존관계 주입 또는 의존성 주입이라 한다.
- **AppConfig 리팩토링**
- **새로운 구조와 할인 정책 적용**
	- **사용 영역**과 **구성 영역** 분리 (관심사 분리)
	- 구현 객체가 변경되어도 구성 영역(AppConfig)만 수정하면 된다.
	- DIP, OCP를 모두 만족한다.
- **전체 흐름 정리**
- **좋은 객체 지향 설계의 5가지 원칙의 적용**
	- SRP 단일 책임 원칙
		- 한 클래스는 하나의 책임만 가져야 한다.
		- 클라이언트 객체는 직접 구현 객체를 생성하고, 실행하는 다양한 책임을 가지고 있었다.
		- SRP 단일 책임 원칙을 따르면서 관심사를 분리.
		- 구현 객체를 생성하고 연결하는 책임은 AppConfig가 담당.
		- 클라이언트 객체는 실행하는 책임만 담당.
	- DIP 의존관계 역전 원칙
		- 프로그래머는 “추상화에 의존해야지, 구체화에 의존하면 안된다” 의존성 주입은 이 원칙을 따르는 방법 중 하나다.
		- 기존에는 새로운 할인 정책을 개발하고, 적용하려면 클라이언트 코드도 변경해야 했다.
		- 클라이언트 코드가 DiscountPolicy 추상화 인터페이스에만 의존하도록 변경.
		- 하지만 클라이언트 코드는 인터페이스만으로는 아무것도 실행할 수 없다.
			- AppConfig가 FixDiscountPolicy 객체 인스턴스를 클라이언트 코드 대신 생성해서 클라이언트 코드에 의존관계를 주입했다.
- OCP 개방-폐쇄 원칙
	- 소프트웨어 요소는 확장에는 열려 있으나 변경에는 닫혀 있어야 한다.
		- 다형성 사옹하고 클라이언트가 DIP를 지킴
		- 애플리케이션을 사용 영역과 구성 영역으로 나눔
		- AppConfig가 의존관계를 FixDiscountPolicy -> RateDiscountPolicy로 변경해서 클라이언트 코드에 주입하므로 클라이언트 코드는 변경하지 않아도 된다.
		- 소프트웨어 요소를 새롭게 확장해도 사용 영역의 변경은 닫혀 있다.
- **IoC, DI, 컨테이너**
	- IoC(Inversion of Control)
		- 프로그램의 제어 흐름을 직접 제어하는 것이 아니라 외부에서 관리하는 것을 제어의 역전(IoC)이라 한다.
	- 프레임워크 vs 라이브러리
		- 프레임워크가 내가 작성한 코드를 제어하고, 대신 실행하면 그것은 프레임워크가 맞다. (JUint)
		- 반면에 내가 작성한 코드가 직접 제어의 흐름을 담당한다면 그것은 프레임워크가 아니라 라이브러리다.
	- 의존관계 주입 DI(Dependency Injection)
		- 의존관계는 **정적인 클래스 의존관계와, 실행 시점에 결정되는 동적인 객체(인스턴스) 의존관계** 둘을 분리해서 생각해야 한다.
		- **정적인 클래스 의존관계**
			- 클래스가 사용하는 import 코드만 보고 의존관계를 쉽게 판단할 수 있다. 정적인 의존관계는 애플리케이션을 실행하지 않아도 분석할 수 있다.
		- **동적인 객체 인스턴스 의존관계**
			- 애플리케이션 실행 시점(런타임)에 실제 생성된 객체 인스턴스의 참조가 연결된 의존 관계다.
	- **IoC 컨테이너, DI 컨테이너**
		- AppConfig 처럼 객체를 생성하고 관리하면서 의존관계를 연결해 주는 것을 IoC 컨테이너 또는 **DI 컨테이너**라 한다.
		- 최근에는 주로 DI 컨테이너라 하고, 어샘블러, 오브젝트 팩토리 등으로 불리기도 한다.
- **스프링으로 전환하기**
	- `ApplicationContext`를 스프링 컨테이너라 한다.

## 4. 스프링 컨테이너와 스프링 빈

##### 스프링 컨테이너 생성
- `ApplicationContext`를 스프링 컨테이너라 한다.
- `ApplicationContext`는 인터페이스이다.
- 스프링 컨테이너는 XML 또는 애노테이션 기반의 자바 설정 클래스로 만들 수 있다.
##### 스프링 컨테이너 생성 과정
1. 스프링 컨테이너 생성
	- `new AnnotaionConfigApplicationContext(APPCONFIG.CLASS)`
	- 스프링 컨테이너를 생성할 때는 구성 정보를 지정해주어야 한다.
	- `AppConfig.class`를 구성 정보로 지정.
2. 스프링 빈 등록
	- 스프링 컨테이너는 파라미터로 넘어온 설정 정보(`AppConfig.class`)를 사용해서 스프링 빈을 등록한다.
	- 빈 이름은 메서드 이름을 사용한다. 
	```java
	@Bean
	public MemberService meberService() {
		return new MemberServiceImpl(memberRepository());
	}
	```
	- 빈 이름을 직접 부여할 수도 있다. `@Bean(name="이름")`
	- 빈 이름은 항상 다른 이름을 부여해야 한다. 같은 이름 부여시, 다른 빈이 무시되거나, 기존 빈을 덮어버리거나 설정에 따라 요류가 발생한다.
3. 스프링 빈 의존관계 설정 - 준비
4. 스프링 빈 의존관계 설정 - 완료
	- 스프링 컨테이너는 설정 정보를 참고해서 의존관계를 주입(DI)한다.
	- 스프링은 빈을 생성하고, 의존관계를 주입하는 단계가 나뉘어 있다. 하지만 자바 코드로 스프링 빈을 등록하면 생성자를 호출하면서 의존관계 주입도 한번에 처리된다. (파라미터로 의존관계의 메소드 호출)
##### 컨테이너에 등록된 모든 빈 조회
- 모든 빈 출력하기
	- `ac.getBeanDefinitionNames()`: 스프링에 등록된 모든 빈 이름을 조회한다.
	- `ac.getBean()`: 빈 이름으로 빈 객체(인스턴스)를 조회한다.
- 애플리케이션 빈 출력하기
	- 스프링이 내부에서 사용하는 빈은 `getRole()`로 구분할 수 있다.
		- `ROLE_APPLICATION`: 일반적으로 사용자가 정의한 빈
		- `ROLE_INFRASTRUCTURE`: 스프링이 내부에서 사용하는 빈
##### 스프링 빈 조회 - 기본
스프링 컨테이너에서 빈을 찾는 기본적인 방법
- `ac.getBean(빈이름, 타입)`
- `ac.getBean(타입)`
- 조회 대상 스프링 빈이 없으면 예외 발생
	- `NoSuchBeanDefinitionException: No bean named 'xxx' available`
- 구체 타입으로 조회하면 변경시 유연성이 떨어진다.
##### 스프링 빈 조회 - 동일한 타입이 둘 이상
- 타입으로 조회시 같은 타입의 스프링 빈이 둘 이상이면 오류가 발생한다. 이때는 빈 이름을 지정하자.
- `ac.getBeansOfType()`을 사용하면 해당 타입의 모든 빈을 조회할 수 있다.
##### 스프링 빈 조회 - 상속 관계
- 부모 타입으로 조회하면 자식 타입도 함께 조회한다.
- 그래서 모든 자바 객체의 최고 부모인 `Object`타입으로 조회하면 모든 스프링 빈을 조회한다.
##### BeanFactory와 ApplicationContext
- BeanFactory
	- 스프링 컨테이너의 최상위 인터페이스다.
	- 스프링 빈을 관리하고 조회하는 역할을 담당한다.
	- `getBean()`을 제공한다.
- ApplicationContext
	- BeanFactory 기능을 모두 상속받아서 제공한다.
	- 애플리케이션을 개발할 때는 빈을 관리하고 조회하는 기능은 물론이고, 수 많은 부가기능이 필요하다.
- ApplicationContext 부가기능
	- 메시지소스를 활용한 국제화 기능
		- 예를 들어 한국에서 들어오면 한국어로, 영어권에서 들어오면 영어로 출력
	- 환경변수
		- 로컬, 개발, 운영등을 구분해서 처리
	- 애플리케이션 이벤트
		- 이벤트를 발행하고 구독하는 모델을 편리하게 지원
	- 편리한 리소스 조회
		- 파일, 클래스패스, 외부 등에서 리소스를 편리하게 조회
##### 다양한 설정 형식 지원 - 자바 코드, XML
- 스프링 컨테이너는 다양한 형식의 설정 정보를 받아들일 수 있게 유연하게 설계되어 있다.
	- 자바 코드, XML, Grooby 등등
- 애노테이션 기반 자바 코드 설정 사용
	- `new AnnotationConfigApplicationContext(AppConfig.class)`
	- `AnnotationConfigApplicationContext`클래스를 사용하면서 자바 코드로된 설정 정보를 넘기면 된다.
- XML 설정 사용
	- 최근에는 스프링 부트를 많이 사용하면서 XML기반의 설정은 잘 사용하지 않는다. 아직 많은 레거시 프로젝트 들이 XML로 되어 있다.
	- XML을 사용하면 컴파일 없이 빈 설정정보를 변경할 수 있는 장점이 있다.
	- `GenericXmlApplicationContext`를 사용하면서 `xml`설정 파일을 넘기면 된다.
	- xml 기반의 `appConfig.xml`스프링 설정 정보와 자바 코드로 된 `AppConfig.java`설정 정보를 비교해보면 거의 비슷하다.
	- 더 자세한 것은 스프링 공식 레퍼런스 문서를 확인.
##### 스프링 빈 설정 메타 정보 - BeanDefinition
- 스프링은 어떻게 다양한 설정 형식을 지원하는가? 그 중심에는 `BeanDefinition`이라는 추상화가 있다.
- 쉽게 말해 **역할과 구현을 개념적으로 나눈 것**이다.
	- XML을 읽어서 BeanDefinition을 만들면 된다.
	- 자바 코드를 읽어서 BeanDefinition을 만들면 된다.
	- 스프링 컨테이너는 자바 코드인지, XML인지 몰라도 된다. 오직 BeanDefinition만 알면 된다.
- `BeanDefinition`을 빈 설정 메타정보라 한다.
	- `@Bean`, `<bean>`당 각각 하나씩 메타 정보가 생성된다.
- 스프링 컨테이너는 이 메타정보를 기반으로 스프링 빈을 생성한다.
- 코드레벨로 확인
	- `AnnotationConfigApplicationContext`는 `AnnotatedBeanDefinitionReader`를 사용해서 `AppConfig.class`를 읽고 `BeanDefinition`을 생성한다.
	- `GenericXmlApplicationContext`는 `XmlBeanDefinitionReader`를 사용해서 `appConfig.xml`설정 정보를 읽고 `BeanDefinition`을 생성한다.
	- 새로운 형식의 설정 정보가 추가되면, XxxBeanDefinitionReader를 만들어서 `BeanDefinition`을 생성하면 된다.
- BeanDefinition 정보
	- BeanClassName: 생성할 빈의 클래스 명(자바 설정 처럼 팩토리 역할의 빈을 사용하면 없음)
	- factoryBeanName: 팩토리 역할의 빈을 사용할 경우 이름, 예) appConfig
	- factoryMethodName: 빈을 생성할 팩토리 메서드 지정, 예) memberService
	- Scope: 싱글톤(기본값)
	- lazyInit: 스프링 컨테이너를 생성할 때 빈을 생성하는 것이 아니라, 실제 빈을 사용할 때 까지 최대한 생성을 지연 처리 하는지 여부
	- InitMethodName: 빈을 생성하고, 의존관계를 적용한 뒤에 호출되는 초기화 메서드 명
	- DestroyMethodName: 빈의 생명주기가 끝나서 제거하기 직전에 호출되는 메서드 명
	- Constructor arguments, Properties: 의존관계 주입에서 사용한다. (자바 설정 처럼 팩토리 역할의 빈을 사용하면 없음)
- BeanDefinition을 직접 생성해서 스프링 컨테이너에 등록할 수도 있다. 하지만 실무에서 BeanDefinition을 직접 정의하거나 사용할 일은 거의 없다.
- 스프링이 다양한 형태의 설정 정보를 BeanDefinition으로 추상화해서 사용하는 것 정도만 일단 이해하자.

## 5. 싱글톤 컨테이너
##### 웹 애플리케이션과 싱글톤
- 순수한 DI 컨테이너인 AppConfig는 요청을 할 때 마다 객체를 새로 생성한다.
- 고객 트래픽이 초당 100이 나오면 초당 100개 객체가 생성되고 소멸된다. -> 메모리 낭비
- 해결방안은 해당 객체가 딱 1개만 생성되고, 공유하도록 설계하면 된다. -> 싱글톤 패턴
##### 싱글톤 패턴
- 클래스의 인스턴스가 1개만 생성되는 것을 보장하는 디자인 패턴이다.
- 따라서, 객체 인스턴스를 2개 이상 생성하지 못하도록 막아야 한다.
- private 생성자를 사용하여 외부에서 임의로 new 키워드를 사용하지 못하도록 막는다.
- 싱글톤 패턴을 구현하는 방법은 여러가지가 있다. 여기서는 객체를 미리 생성해두는 가장 단순하고 안전한 방법을 선택했다.
- **싱글톤 패턴 문제점**
	- 싱글톤 패턴을 구현하는 코드 자체가 많다.
	- 의존관계상 클라이언트가 구체 클래스에 의존한다. -> DIP 위반
	- 클라이언트가 구체 클래스에 의존해서 OCP 원칙을 위반할 가능성이 높다.
	- 테스트하기 어렵다.
	- 내부 속성을 변경하거나 초기화 하기 어렵다.
	- private 생성자로 자식 클래스를 만들기 어렵다.
	- 결론적으로 유연성이 떨어진다.
	- 안티패턴으로 불리기도 한다.
##### 싱글톤 컨테이너
- 스프링 컨테이너는 싱글톤 패턴의 문제점을 해결하면서, 객체 인스턴스를 싱글톤으로 관리한다.
- 스프링 컨테이너는 싱글톤 컨테이너 역할을 한다. 이렇게 싱글톤 객체를 생성하고 관리하는 기능을 싱글톤 레지스트리라 한다.
- 스프링 컨테이너의 이런 기능 덕분에 싱글톤 패턴의 모든 단점을 해결하면서 객체를 싱글톤으로 유지할 수 있다.
	- 싱글톤 패턴을 위한 지저분한 코드가 들어가지 않아도 된다.
	- DIP, OCP, 테스트, private 생성자로 부터 자유롭게 싱글톤을 사용할 수 있다.
- 스프링의 기본 빈 등록 방식은 싱글톤이지만, 싱글톤 방식만 지원하는 것은 아니다. 요청할 때 마다 새로운 객체를 생성해서 반환하는 기능도 제공한다.
##### 싱글톤 방식의 주의점
- 싱글톤 패턴이든, 스프링 같은 싱글톤 컨테이너를 사용하든, 객체 인스턴스를 하나만 생성해서 공유하는 싱글톤 방식은 여러 클라이언트가 하나의 같은 객체 인스턴스를 공유하기 때문에 싱글톤 객체는 유지(stateful)하게 설계하면 안된다.
- 무상태(stateless)로 설계해야 한다!
	- 특정 클라이언트에 의존적인 필드가 있으면 안된다.
	- 특정 클라이언트가 값을 변경할 수 있는 필드가 있으면 안된다!
	- 가급적 읽기만 가능해야 한다.
	- 필드 대신에 자바에서 공유되지 않는 **지역변수, 파라미터, ThreadLocal** 등을 사용해야 한다.
##### @Configuration과 싱글톤
- `AppConfig`를 보면 `new MemoryMemberRepository()`를 실행하는 `memberRepository()`메서드는 총 3번 호출될 걸로 예상되는데 실제로는 1번만 호출되고 있다. 그 이유는???
##### @Configuration과 바이트코드 조작의 마법
>스프링 컨테이너는 싱글톤 레지스트리다. 따라서 스프링 빈이 싱글톤이 되도록 보장해주어야 한다. 그런데 스프링이 자바 코드까지 핸들링 하기는 어렵다. 자바 코드를 보면 분명 3번 호출되어야 하는 것이 맞다.
>그래서 스프링은 클래스의 바이트코드를 조작하는 라이브러리를 사용한다.

- `AnnotationConfigApplicationContext`에 파라미터로 넘긴 값은 스프링 빈으로 등록된다. 따라서, `AppConfig`도 스프링 빈이 된다.
- `AppConfig` 클래스 정보를 조회해보면 `class hello.core.AppConfig$$SpringCGLIB$$0`로 출력된다. 이것은 내가 만든 클래스가 아니라 스프링이 CGLIB라는 바이트코드 조작 라이브러리를 사용해서 AppConfig 클래스를 상속받은 임의의 다른 클래스를 만들고, 그 다른 클래스를 스프링 빈으로 등록한 것이다.
- 그 임의의 다른 클래스가 바로 싱글톤이 보장되도록 해준다.
- @Bean이 붙은 메서드마다 이미 스프링 빈이 존재하면 존재하는 빈을 반환하고, 스프링 빈이 없으면 생성해서 스프링 빈으로 등록하고 반환하는 코드가 동적으로 만들어진다. 이로 인해 싱글톤이 보장된다.
>`@Configuration` 을 적용하지 않고, `@Bean` 만 적용하면 어떻게 될까?

- `class hello.core.AppConfig` , 이 출력 결과를 통해서 AppConfig가 CGLIB 기술 없이 순수한 AppConfig로 스프링 빈에 등록된 것을 확인할 수 있다.
- *정리*
	- @Bean만 사용해도 스프링 빈으로 등록되지만, 싱글톤을 보장하지 않는다.
		- `memberRepository()` 처럼 의존관계 주입이 필요해서 메서드를 직접 호출할 때 싱글톤을 보장하지 않는다.

## 6. 컴포넌트 스캔
##### 컴포넌트 스캔과 의존관계 자동 주입 시작하기
- 지금까지 스프링 빈을 등록할 때 자바 코드의 @Bean 또는 XML의 <bean>등을 통해 설정 정보를 직접 등록할 스프링 빈을 나열했다.
- 등록해야 할 스프링 빈이 수십, 수백개가 되면 일일히 등록하기 힘들고, 설정 정보도 커지고, 누락하는 문제도 발생한다.
- 스프링은 자동으로 스프링 빈을 등록하는 컴포넌트 스캔이라는 기능을 제공한다.
- 또한, 의존관계도 자동으로 주입하는 `@Autowired` 라는 기능도 제공한다.
- 컴포넌트 스캔을 사용하려면 먼저 `@ComponentScan`을 설정 정보에 붙여준다.
- 컴포넌트 스캔은 `@Component` 애노테이션이 붙은 클래스를 스캔해서 스프링 빈으로 등록한다.
- 이전 AppConfig에서는 `@Bean`으로 직접 설정 정보를 작성하고, 의존관계도 직접 명시했다. 이제는 이런 설정 정보 자체가 없기 때문에, 의존관계 주입도 해당 클래스 안에서 해결한다.
- `@Autowired`는 의존관계를 자동으로 주입해준다.
##### @ComponentScan
- `@ComponentScan`은 `@Component`가 붙은 모든 클래스를 스프링 빈으로 등록한다.
- 스프링 빈의 기본 이름은 클래스명을 사용하되 맨 앞글자만 소문자를 사용한다.
	- *빈 이름 기본 전략*: MemberServiceImpl 클래스 -> memberServiceImpl
	- *빈 이름 직접 지정*: `@Component("memberService2")`
##### @Autowired 의존관계 자동 주입
- 생성자에 `@Autowired`를 지정하면, 스프링 컨테이너가 자동으로 해당 스프링 빈을 찾아서 주입한다.
##### 탐색 위치와 기본 스캔 대상
- 탐색할 패키지의 시작 위치 지정
	- `@ComponentScan(basePackages = "hello.core")`
	- basePackages 를 포함해서 하위 패키지 모두 탐색한다.
	- `(basePackages = "hello.core", "hello.service")` 이렇게 여러 시작 위치 지정도 가능하다.
	- 지정하지 않으면 `@ComponentScan` 이 붙은 설정 정보 클래스의 패키지가 시작위치가 된다.
- 설정 정보 클래스의 위치를 프로젝트 최상단에 두는 것을 권장한다. 스프링 부트도 이 방법을 기본으로 제공한다.
- 애노테이션에는 상속관계라는 것이 없다. 그래서 이렇게 애노테이션이 특정 애노테이션을 들고 있는 것을 인식할 수 있는 것은 자바 언어가 지원하는 기능은 아니고, 스프링이 지원하는 기능이다.
- 다음 애노테이션이 있으면 컴포넌트 스캔의 용도 뿐만 아니라 부가 기능을 수행한다.
	- `@Controller`: 스프링 MVC 컨트롤러로 인식
	- `@Repository`: 스프링 데이터 접근 계층으로 인식하고, 데이터 계층의 예외를 스프링 예외로 변환해준다.
	- `@Configuration`: 스프링 설정 정보로 인식하고, 스프링 빈이 싱글톤을 유지하도록 추가 처리를 한다.
	- `@Service`: 추가 기능은 없지만, 비지니스 계층을 인식하는데 도움이 된다.
	- `useDefaultFilters` 옵션은 기본으로 켜져있는데, 이 옵션을 끄면 기본 스캔 대상들이 제외된다.
##### 필터
- `includeFilters`: 컴포넌트 스캔 대상을 추가로 지정한다.
- `excludeFilters`: 컴포넌트 스캔에서 제외할 대상을 지정한다.
- FilterType 옵션
	- ANNOTATION: 기본값, 애노테이션을 인식해서 동작한다.
		- `org.example.SomeAnnotation`
	- ASSIGNABLE_TYPE: 지정한 타입과 자식 타입을 인식해서 동작한다.
		- `org.example.SomeClass`
	- ASPECTJ: AspectJ 패턴 사용
		- `org.example..*Service+`
	- REGEX: 정규 표현식
		- `org\.example\.Default.*`
	- CUSTOM: `TypeFilter` 라는 인터페이스를 구현해서 처리
		- `org.example.MyTypeFilter`
- `@Component`면 충분하기 때문에, `includeFilters`를 사용할 일은 거의 없다. `excludeFilters`는 여러가지 이유로 간혹 사용할 때가 있지만 많지 않다.
- 스프링 부트는 컴포넌트 스캔을 기본으로 제공하는데, 옵션을 변경하면서 사용하기 보다는 스프링의 기본 설정에 최대한 맞추어 사용하는 것을 권장한다.
##### 중복 등록과 충돌
- 자동 빈 등록 vs 자동 빈 등록
	- `ConfilctingBeanDefinitionException` 예외 발생
- 수동 빈 등록 vs 자동 빈 등록
	- 수동 빈 등록이 우선권을 가진다. (수동 빈이 자동 빈을 오버라이딩 한다.)
	- 스프링 부트에서는 수동 빈 등록과 자동 빈 등록이 충돌나면 오류가 발생하도록 기본 값을 바꾸었다.
