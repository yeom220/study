<br>

# Vue 3 Composition API와 타입 스크립트
<br>

## 컴포넌트 Props 작성
### defineProps()

컴포넌트의 props를 정의하는 함수입니다.
`<script setup>` 을 사용할 때 `defineProps()`는 전달인자를 기반으로 `props` 타입 추론을 진행합니다.

**런타임 선언 방식**
```typescript
<script setup lang="ts">
const props = defineProps({
  foo: { type: String, required: true },
  bar: Number
})

props.foo // string
props.bar // number | undefined
</script>
```

**타입 기반 선언 방식 (많이 사용하는 방식)**
```typescript
<script setup lang="ts">
const props = defineProps<{
  foo: string
  bar?: number
}>()
</script>
```

컴파일러는 타입 전달인자를 기반으로 같은 런타임 옵션을 추론 하도록 시도합니다. 타입 기반 선언은 런타임 선언 방식과 정확히 동일한 런타임 옵션으로 컴파일 됩니다.

타입 기반 선언 또는 런타임 선언 중 하나를 사용할 수 있지만 동시에 둘 다 사용할 수는 없습니다.

**props 타입을 별도의 인터페이스로 지정**
```typescript
<script setup lang="ts">
interface Props {
  foo: string
  bar?: number
}

const props = defineProps<Props>()
</script>
```

##### 문법 제한
`defineProps()` 의 제너릭 전달인자는 다음 중 하나여야 합니다.

객체 리터럴 타입
```ts
defineProps<{ /*... */ }>()
```

**동일한 파일**에 있는 인터페이스 또는 객체 리터럴 타입에 대한 참조
```ts
interface Props {/* ... */}

defineProps<Props>()
```

`defineProps` 의 제네릭 전달인자는 가져온 타입을 **사용 할 수 없습니다**
```ts
import { Props } from './other-file'

// 지원하지 않음
defineProps<Props>()
```

[공식 문서](https://v3-docs.vuejs-korea.org/guide/typescript/composition-api.html#typing-component-props)


### withDefaults()

타입 기반 선언을 사용하면 `props`의 기본값을 선언할 수 없게 됩니다. 기본값 선언(초기화)을 위해 Vue는 `withDefaults` 함수를 제공합니다.

```ts
export interface Props {
  msg?: string
  labels?: string[]
}

const props = withDefaults(defineProps<Props>(), {
  msg: 'hello',
  labels: () => ['one', 'two']
})
```

- [공식 문서](https://v3-docs.vuejs-korea.org/guide/typescript/composition-api.html#props-default-values)
<br>

## 컴포넌트 Emits 작성

`<script setup>` 에서 런타임 선언 또는 타입 선언을 사용하여 `emit` 함수를 입력할 수 있습니다.

```ts
<script setup lang="ts">
// runtime
// 런타임
const emit = defineEmits(['change', 'update'])

// type-based
// 타입기반
const emit = defineEmits<{
  (e: 'change', id: number): void
  (e: 'update', value: string): void
}>()
</script>
```

타입 전달인자는 [호출 서명](https://www.typescriptlang.org/docs/handbook/2/functions.html#call-signatures) 이 있는 타입 리터럴이어야 합니다. 타입 리터럴은  `emit` 함수의 타입으로 사용됩니다. 타입 선언은 emit된 이벤트의 타입을 제약 조건을 상세하게 지정할 수 있습니다.
- [공식 문서](https://v3-docs.vuejs-korea.org/guide/typescript/composition-api.html#typing-component-emits)
<br>

### `ref()`에 타입 적용

Refs는 초기 값에서 타입을 추론합니다.

```ts
import { ref } from 'vue'

// 타입 유추: Ref<number>
const year = ref(2020)

// => TS Error: Type 'string' is not assignable to type 'number'.
year.value = '2020'
```

ref의 내부 값에 대해 복잡한 타입을 지정해야 할 수도 있습니다. `Ref` 타입을 사용하여 이를 수행할 수 있습니다.
```ts
import { ref } from 'vue'
import type { Ref } from 'vue'

const year: Ref<string | number> = ref('2020')

year.value = 2020 // ok!
```

또는 제네릭을 통해 타입을 정의할 수 있습니다.
```ts
// 결과 타입: Ref<string | number>
const year = ref<string | number>('2020')

year.value = 2020 // ok!
```

제네릭 형식 타입를 지정하지만 초기 값을 생략하면 결과 타입은 `undefined` 를 포함하는 유니온 타입이 됩니다.
```ts
// 추론된 타입: Ref<number | undefined>
const n = ref<number>()
```
- [공식 문서](https://v3-docs.vuejs-korea.org/guide/typescript/composition-api.html#typing-ref)
<br>

### `computed()`에 타입 지정

computed() 는 getter의 반환 값을 기반으로 해당 타입을 추론합니다
```ts
import { ref, computed } from 'vue'

const count = ref(0)

// 추론된 타입: ComputedRef<number>
const double = computed(() => count.value * 2)

// => TS Error: Property 'split' does not exist on type 'number'
const result = double.value.split('')
```

제네릭을 통해 명시적으로 타입을 지정할 수도 있습니다.
```ts
const double = computed<number>(() => {
  // type error if this doesn't return a number
})
```

<br>

### 이벤트 핸들러에 타입 지정

네이티브 DOM 이벤트를 처리할 때 핸들러에 명확하게 이벤트 타입을 정의하는 것이 유용할 수 있습니다. 다음 예를 살펴보겠습니다.
```ts
<script setup lang="ts">
function handleChange(event) {
  // `event` 는 어떤(`any`) 타입일수도 있음
  console.log(event.target.value)
}
</script>

<template>
  <input type="text" @change="handleChange" />
</template>
```

타입 어노테이션이 없으면 `event` 전달인자는 암묵적으로 `any` 타입을 갖습니다. `"strict": true` 또는 `"noImplicitAny": true` 가 `tsconfig.json` 에서 사용되는 경우에는 TS 에러가 발생합니다. 따라서 이벤트 핸들러의 전달에 타입을 지정하는 것을 권장합니다.
```ts
function handleChange(event: Event) {
  console.log((event.target as HTMLInputElement).value)
}
```
<br>

### nextTick()

다음 DOM 업데이트 발생을 기다리는 유틸리티입니다.

반응형 상태를 변경한 결과는 동기적으로 DOM에 업데이트되지 않습니다. 그대신, 상태를 얼마나 많이 변경했는지에 관계없이 "다음 틱"까지 버퍼링하여, 각 컴포넌트가 한 번만 업데이트 되었음을 보장합니다.

`nextTick()`은 상태 변경 직후에 DOM 업데이트가 완료될 때까지 대기하는 데 사용할 수 있습니다. 콜백을 인자로 전달하거나, 프로미스(Promise) 반환을 기다릴 수 있습니다.

```ts
<script setup>
import { nextTick } from 'vue'

const count = ref(0);
const increment = async () => {
	this.count++
	
	// 아직 DOM 업데이트되지 않음.
	console.log(document.getElementById('counter').textContent) // 0
	
	await nextTick()
	// 이제 DOM 업데이트됨.
	console.log(document.getElementById('counter').textContent) // 1
}
</script>

<template>
  <button id="counter" @click="increment">{{ count }}</button>
</template>
```
- [공식 문서](https://v3-docs.vuejs-korea.org/api/general.html#nexttick)
<br>

### defineComponent()

타입 추론으로 Vue 컴포넌트를 정의하기 위한 함수입니다.

타입스크립트가 컴포넌트 옵션 내에서 타입을 올바르게 추론할 수 있도록 하려면 [`defineComponent()`](https://v3-docs.vuejs-korea.org/api/general.html#definecomponent) 를 사용하여 컴포넌트를 정의해야 합니다.

또한 `defineComponent()` 는 `<script setup>` 없이 Composition API를 사용할 때 `setup()` 에 전달된 props의 추론을 지원합니다.
```ts
import { defineComponent } from 'vue'

export default defineComponent({
  // 타입추론 활성화
  props: {
    message: String
  },
  setup(props) {
    props.message // type: string | undefined
  }
})
```

- [공식 문서](https://v3-docs.vuejs-korea.org/guide/typescript/overview.html#definecomponent)
<br>

### defineAsyncComponent()

거대한 앱에서는 앱을 더 작게 조각내어 나누고, 필요할 때만 서버에서 컴포넌트를 로드해야 할 수 있습니다. 이를 구현하기 위해 [`defineAsyncComponent`](https://v3-docs.vuejs-korea.org/api/general.html#defineasynccomponent) 함수를 제공합니다
```ts
import { defineAsyncComponent } from 'vue'

const AsyncComp = defineAsyncComponent(() => {
  return new Promise((resolve, reject) => {
    // ...서버에서 컴포넌트를 로드하는 로직
    resolve(/* 로드 된 컴포넌트 */)
  })
})
// ... 일반 컴포넌트처럼 `AsyncComp`를 사용 
```

위 예제처럼 `defineAsyncComponent`는 Promise를 반환하는 로더 함수를 사용합니다. Promise의 `resolve` 콜백을 호출해 서버에서 가져온 정의되어 있는 컴포넌트를 반환합니다. 로드가 실패했음을 나타내기 위해 `reject(reason)`를 호출할 수도 있습니다.

`import(...)`도 Promise를 반환하므로, 대부분의 경우 `defineAsyncComponent`와 함께 사용합니다.
```ts
import { defineAsyncComponent } from 'vue'

const AsyncComp = defineAsyncComponent(() =>
  import('./components/MyComponent.vue')
)
```

반환된 `AsyncComp`는 페이지에서 실제로 렌더링될 때만 로더 함수를 호출하는 래퍼 컴포넌트입니다. 또한 모든 props를 내부 컴포넌트에 전달하므로, 기존 구현된 컴포넌트를 비동기 래퍼 컴포넌트로 문제없이 교체하여 지연(lazy) 로드를 구현할 수 있습니다.

##### 로딩 및 에러 상태

비동기 작업에는 필연적으로 로드 및 에러 상태가 포함됩니다. `defineAsyncComponent()`는 고급 옵션을 통해 이러한 상태 처리를 지원합니다:
```ts
const AsyncComp = defineAsyncComponent({
  // 로더 함수
  loader: () => import('./Foo.vue'),

  // 비동기 컴포넌트가 로드되는 동안 사용할 로딩 컴포넌트입니다.
  loadingComponent: LoadingComponent,
  // 로딩 컴포넌트를 표시하기 전에 지연할 시간. 기본값: 200ms
  delay: 200,

  // 로드 실패 시 사용할 에러 컴포넌트
  errorComponent: ErrorComponent,
  // 시간 초과 시, 에러 컴포넌트가 표시됩니다. 기본값: 무한대
  timeout: 3000
})
```

로딩 컴포넌트가 제공되면 내부 컴포넌트가 로딩되는 동안 먼저 표시됩니다. 로딩 컴포넌트가 표시되기 전에 기본 200ms 지연시간이 있습니다. 이는 빠른 네트워크에서 인스턴트 로딩 상태가 너무 빨리 교체되어 깜박임처럼 보일 수 있기 때문입니다.

에러 컴포넌트가 제공되면 로더 함수의 Promise가 reject로 반환될 때 표시됩니다. 요청이 너무 오래 걸릴 때 에러 컴포넌트를 표시하도록 시간 초과를 지정할 수도 있습니다

- [공식 문서](https://v3-docs.vuejs-korea.org/guide/components/async.html#async-components)
<br>
-----

# Pinia

피니아는 Vue의 스토어 라이브러리로 컴포넌트/페이지 간에 상태를 공유할 수 있습니다.

###  defineStore()
- https://pinia.vuejs.kr/core-concepts/#defining-a-store

### Composables
- https://pinia.vuejs.kr/cookbook/composables.html



-----




# 기타
### v-memo
- https://v3-docs.vuejs-korea.org/api/built-in-directives.html#v-memo