# 목차
- Vue란?
- Vue 핵심 개념
- vuex
- router
- Composition API


# Vue란?
>[!Vue]
>사용자 인터페이스를 구축하기 위해 설계된 자바스크립트 프레임워크이다.
>Vue는 단순성과 유연성 덕분에 프론트엔드 영역에서 많이 활용되고 있다.

### 주요 특징
- **반응형 데이터 바인딩**
	- Vue.js는 MVVM(Model-View-ViewModel) 패턴을 기반으로 하여, 데이터 모델과 뷰 사이의 반응형 데이터 바인딩을 제공한다. 이는 데이터가 변경되면 자동으로 UI가 업데이트 되도록 한다.
- **컴포넌트 기반 구조**
	- Vue.js는 UI를 컴포넌트 단위로 나누어 개발할 수 있다. 컴포넌트는 재사용 가능하고 독립적이며, 복잡한 애플리케이션을 개발할 때 모듈화된 코드를 작성할 수 있게 한다.
- **디렉티브 및 템플릿 구문**
	- Vue.js는 `v-bind`, `v-model`, `v-if`, `v-for` 등 다양한 디렉티브를 제공하여, 데이터와 DOM 간의 상호 작용을 쉽게 구현할 수 있게 한다. 템플릿 구문을 통해 선언적으로 UI를 구성할 수 있다.
- **강력한 생태계**
	- Vue.js는 Vue Router, Vuex, Vue CLI 등 다양한 공식 라이브러리 및 도구를 통해 라우팅, 상태 관리, 프로젝트 생성 및 빌드 설정을 지원한다. 이를 통해 복잡한 애플리케이션 개발이 용이해진다.
- **유연성**
	- Vue.js는 다양한 방식으로 사용될 수 있다. 작은 위젯이나 컴포넌트로 시작하여, 점진적으로 복잡한 SPA(Single Page Application)로 확장할 수 있다.



# Vue 핵심 개념

### Vue 앱 인스턴스 생성 및 DOM 연결
- Vue 앱 초기화
	- createApp 함수에 루트가 될 뷰 파일을 파라미터로 넘긴 후에DOM(html)에 마운트 한다.
```javascript
// main.js
import { createApp } from 'vue';

import App from './App.vue';

const app = createApp(App);
app.mount('#app');
```

```html
<!DOCTYPE html>
<html lang="en">
  <body>
    <div id="app"></div>
  </body>
</html>
```

```javascript
<template>
  <section>
	{{ hello }}
  </section>
</template>

<script>
export default {
  data() {
    return {
	    hello: 'Hello World',
    };
  }
};
</script>
```



### `{{ }}` 보간법
- 데이터 바인딩은  `{{ data }}` 문법을 사용하며, `data` 값이 변경되면, 화면도 함께 변경된다.
```javascript
<template>
  <section>
	{{ data }}
  </section>
</template>

<script>
export default {
  data() {
    return {
	    data: 'Hello World',
    };
  }
};
</script>
```



### V-디렉티브

- `v-once`
	- 한번만 렌더링 되고 데이터(`message`)의 값이 변경돼도 화면을 갱신하지 않는다.
```javascript
<p v-once>{{ message }}</p>
```

- `v-html`
	- `<template>`에 html 을 출력 해야하는 경우 사용
	- 단, XSS(교차 사이트 스크립팅) 취약점이 있으므로, 가급적 사용하지 않는다.
```javascript
<p v-html="rawHtml"><p>
```

- `v-bind`
	- html 태그 속성에 사용하는 경우 `v-bind` 사용 (`:속성명`으로 축약 가능)
```javascript
<a v-bind:href="vueLink">naver</a>
<a :href="vueLink">naver</a>  // 위와 동일
```

- `v-bind:class`
	- html class에 반응형 객체 바인딩에 사용한다. (축약가능 `:class`)
	- 기존 class 와 같이 사용 가능하다.
	- 값으로 변수, 객체, 배열을 받을 수 있다.
```html
<button :class="isActive ? active : ''" class="btnClass">Button</button> // 변수
<button :class="[isActive ? active : '', btnClass]">Button</button> // 배열
<button :class="{active : isActive, btnClass : true}">Button</button> // 객체
```

- `v-if="조건식"` `v-else-if="조건식"` `v-else`
	- 조건식이 true 일 경우 렌더링
	- `v-if`, `v-else-if`, `v-else` 사이에 다른 태그가 들어가면 오류 발생
```html
<h2 v-if="type === 'A'">A</h2>
<h2 v-else-if="type === 'B'">B</h2>
<!-- <h2>오류 발생</h2> -->
<h2 v-else>Else</h2>
```

- `v-show`
	- 조건식이 true 일 경우 UI 노출 (렌더링은 되어있지만 display 속성으로 노출 여부 변경)
```html
<h1 v-show="visible">제목</h1>
```

`v-if`와 `v-show`는 렌더링 여부에서 차이가 있다. 동일 UI의 노출/비노출 전환이 많은 경우는 `v-show`를 사용하고, 일반적으로는 `v-if`를 사용한다.

- `v-for`
	- `v-for="item in items"` 문법을 사용하여 배열에서 항목을 순차적으로 할당한다.
	- `v-for="(item, index) in items"` 문법을 사용하면 항목과 인덱스를 함께 가져올 수 있다.
	- `v-for="(value, key, index) in object"` 문법을 사용하면 객체의 속성, 값, 인덱스를 가져올 수 있다.
	- **`v-for`를 사용할 때 `:key` 속성에 유니크 값을 지정해야 한다. (필수)**
```html

```


----

# Vue 3 (Composition API)
### `<template>`에서 `v-if`
- https://v3-docs.vuejs-korea.org/api/built-in-special-elements.html#template

### defineProps()
- https://v3-docs.vuejs-korea.org/guide/typescript/composition-api.html#typing-component-props

### withDefaults()
- https://v3-docs.vuejs-korea.org/guide/typescript/composition-api.html#props-default-values

### defineAsyncComponent()
- https://v3-docs.vuejs-korea.org/api/general.html#defineasynccomponent

### v-cloack
- https://v3-docs.vuejs-korea.org/api/built-in-directives.html#v-cloak

### v-memo
- https://v3-docs.vuejs-korea.org/api/built-in-directives.html#v-memo

### v-on.once 사용 예


----

# Vuetify

### `<v-select>`
- https://vuetifyjs.com/en/api/v-select/#links

### `<v-window>`
- https://vuetifyjs.com/en/components/windows/#account-creation


----


# Pinia
###  defineStore()
- https://pinia.vuejs.kr/core-concepts/#defining-a-store

### Composables
- https://pinia.vuejs.kr/cookbook/composables.html



-----


# Nuxt
### useFetch()
- https://nuxt.com/docs/api/composables/use-fetch

### useRuntimConfig()
- https://nuxt.com/docs/api/composables/use-runtime-config


### definePageMeta()
- https://nuxt.com/docs/api/utils/define-page-meta

