Vue.createApp({
  data() {
    return {
      name: "yeom",
      age: 34,
      imageUrl:
        "https://img.icons8.com/?size=100&id=1347&format=png&color=000000",
    };
  },
  methods: {
    randomNumber() {
      return Math.random();
    },
  },
}).mount("#assignment");
