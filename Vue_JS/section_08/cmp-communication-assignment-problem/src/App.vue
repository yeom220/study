<template>
  <active-user :name="user.name" :age="user.age"></active-user>
  <user-data @set-data="setUserData"></user-data>
</template>

<script>
import ActiveUser from './components/ActiveUser.vue';
import UserData from './components/UserData.vue';
export default {
  components: { ActiveUser, UserData },
  data() {
    return {
      user: {
        name: 'Yeom',
        age: 34
      }
    };
  },
  methods: {
    setUserData(name, age) {
      this.user = {
        name: name,
        age: +age
      };
    }
  }
};
</script>

<style></style>
