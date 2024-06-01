const app = Vue.createApp({
  data() {
    return {
      currentUserInput: '',
      message: 'Vue is great!'
    };
  },
  methods: {
    saveInput(event) {
      this.currentUserInput = event.target.value;
    },
    setText() {
      // this.message = this.currentUserInput;
      console.dir(this.$refs.userText);
      this.message = this.$refs.userText.value;
    }
  },
  beforeCreate() {
    console.log('called beforeCreate');
  },
  created() {
    console.log('called created');
  },
  beforeMount() {
    console.log('called beforeMount');
  },
  mounted() {
    console.log('called mounted');
  },
  beforeUpdate() {
    console.log('called beforeUpdate');
  },
  updated() {
    console.log('called updated');
  },
  beforeUnmount() {
    console.log('called beforeUnmount');
  },
  unmounted() {
    console.log('called unmounted');
  }
});

app.mount('#app');

setTimeout(function () {
  app.unmount();
}, 3000);

const app2 = Vue.createApp({
  template: `
    <p>{{favoriteMeal}}</p>
  `,
  data() {
    return {
      favoriteMeal: 'Pizza'
    };
  }
});
app2.mount('#app2');

// const data = {
//   message: 'Hello',
//   longMessage: 'Hello World'
// };

// const handler = {
//   set(target, key, value) {
//     if (key === 'message') {
//       target.longMessage = value + ' world';
//     }
//     target.message = value;
//   }
// };

// const proxy = new Proxy(data, handler);

// proxy.message = 'Hello!!!';

// console.log(proxy.longMessage);
