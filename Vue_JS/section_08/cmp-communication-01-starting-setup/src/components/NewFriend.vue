<template>
  <form @submit.prevent="submitData">
    <div>
      <label>Name</label>
      <input type="text" v-model="enteredName" />
    </div>
    <div>
      <label>Phone</label>
      <input type="text" v-model="enteredPhone" />
    </div>
    <div>
      <label>E-Mail</label>
      <input type="text" v-model="enteredEmail" />
    </div>
    <button>Add Contact</button>
  </form>
</template>

<script>
export default {
  emits: ['add-friend-contact'],
  data() {
    return {
      enteredName: '',
      enteredPhone: '',
      enteredEmail: ''
    };
  },
  methods: {
    submitData() {
      this.$emit(
        'add-friend-contact',
        this.enteredName,
        this.enteredPhone,
        this.enteredEmail
      );
    }
  }
};
</script>
