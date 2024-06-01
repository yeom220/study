const app = Vue.createApp({
  data() {
    return {};
  }
});

app.component('friend-contact', {
  template: `
    <li>
    <h2>{{friend.name}}</h2>
    <button @click="toggleDetail">{{detailAreVisible ? 'Hide' : 'Show'}} Details</button>
    <ul v-if="detailAreVisible">
      <li><strong>Phone:</strong> {{friend.phone}}</li>
      <li><strong>Email:</strong> {{friend.email}}</li>
    </ul>
    </li>
	`,
  data() {
    return {
      detailAreVisible: false,
      friend: {
        name: 'Manuel Lorenz',
        phone: '01234 5678 991',
        email: 'manuel@localhost.com'
      }
    };
  },
  methods: {
    toggleDetail() {
      this.detailAreVisible = !this.detailAreVisible;
    }
  }
});

app.mount('#app');
