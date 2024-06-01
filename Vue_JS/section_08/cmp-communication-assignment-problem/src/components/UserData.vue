<template>
  <section>
    <form @submit.prevent="submitData">
      <input type="text" v-model="enteredName" placeholder="Your Name" />
      <input type="text" v-model="enteredAge" placeholder="Your Age" />
      <button>Update User</button>
    </form>
  </section>
</template>

<script>
export default {
  emits: ['set-data'],
  data() {
    return {
      enteredName: '',
      enteredAge: ''
    };
  },
  methods: {
    submitData() {
      this.$emit('set-data', this.enteredName, this.enteredAge);
    }
  }
};
</script>
