<template>
  <li>
    <h2>{{ friend.name }}</h2>
    <button @click="toggleDetails">
      {{ detailsAreVisible ? 'Hide' : 'Show' }} Details
    </button>
  </li>
  <ul v-if="detailsAreVisible">
    <li>
      <strong>Phone:</strong>
      {{ friend.phone }}
    </li>
    <li>
      <strong>Email:</strong>
      {{ friend.email }}
    </li>
  </ul>
</template>

<script>
export default {
  data() {
    return {
      detailsAreVisible: false,
      friend: {
        id: 'manuel',
        name: 'Manuel Lorenz',
        phone: '1234 1234',
        email: 'manuel@localhost.com'
      }
    };
  },
  methods: {
    toggleDetails() {
      this.detailsAreVisible = !this.detailsAreVisible;
    }
  }
};
</script>
