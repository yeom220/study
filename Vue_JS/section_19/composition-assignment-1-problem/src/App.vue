<template>
  <h2>My Course Goal</h2>
  <!-- Task 1: Output your main course goal with help of the composition API -->
  <p :style="{ display: button.visible ? 'block' : 'none' }">{{ myGoal }}</p>
  <!-- <p :style="{ display: btnVisible ? 'block' : 'none' }">{{ myGoal }}</p> -->
  <!-- Don't hardcode it into the template, instead hardcode it into the JS code -->
  <h3>OUTPUT COURSE GOAL</h3>
  <!-- Task 2: Toggle (show/ hide) the goal with help of the button  -->
  <button @click="toggleButton">{{ button.label }} Goal</button>
  <!-- <button @click="toggleButton">{{ btnLabel }} Goal</button> -->
  <!-- Task 3: Manage data in three ways -->
  <!-- => Separate refs -->
  <!-- => Ref Object -->
  <!-- => Reactive Object -->
  <!-- Task 4: Also solve the assignment with the Options API -->
</template>

<script>
import { ref, reactive } from 'vue';
// import { ref } from 'vue';

export default {
  setup() {
    const myGoal = ref('Professional Developer');

    const button = reactive({
      label: 'Hide',
      visible: true,
    });
    function toggleButton() {
      button.visible = !button.visible;
      if (button.visible) {
        button.label = 'Hide';
      } else {
        button.label = 'Show';
      }
    }

    // Task 3
    // const btnLabel = ref('Hide');
    // const btnVisible = ref(true);
    // function toggleButton() {
    //   btnVisible.value = !btnVisible.value;
    //   if (btnVisible.value) {
    //     btnLabel.value = 'Hide';
    //   } else {
    //     btnLabel.value = 'Show';
    //   }
    // }

    return {
      myGoal,
      button,
      toggleButton,
    };
    // return {
    //   myGoal,
    //   btnLabel,
    //   btnVisible,
    //   toggleButton,
    // };
  },
};
</script>

<!-- Task4 -->
<!-- <script>
export default {
  data() {
    return {
      myGoal: 'Professional Developer',
      btnLabel: 'Hide',
      btnVisible: true,
    };
  },
  methods: {
    toggleButton() {
      this.btnVisible = !this.btnVisible;
      if(this.btnVisible){
        this.btnLabel = 'Hide'
      }else{
        this.btnLabel = 'Show';
      }
    },
  },
};
</script> -->

<style>
html {
  font-family: sans-serif;
}
body {
  margin: 3rem;
  text-align: center;
}
</style>
