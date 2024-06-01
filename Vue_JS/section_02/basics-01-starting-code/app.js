const app = Vue.createApp({
  data() {
    return {
      courseGoalA: "Course AAA",
      courseGoalB: "<h2>Course BBB</h2>",
      vueLink: "https://www.naver.com",
    };
  },
  methods: {
    outputGoal() {
      const random = Math.random();
      if (random > 0.5) {
        return this.courseGoalA;
      } else {
        return this.courseGoalB;
      }
    },
  },
});

app.mount("#user-goal");
