<template>
  <!-- <button @click="addOne">Add 2</button> -->
  <button @click="inc">Add 2</button>
  <button @click="increa({ value: 11 })">Add 11</button>
</template>

<script>
import { mapActions } from 'vuex';
export default {
  methods: {
    // addOne() {
    //   this.$store.dispatch('increment');
    // },
    ...mapActions('counter', ['increment', 'increase']),
    ...mapActions('counter', {
      inc: 'increment',
      increa: 'increase',
    }),
  },
};
</script>
