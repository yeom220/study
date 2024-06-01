Vue.createApp({
  data() {
    return {
      result: 0,
      timer: "",
    };
  },
  watch: {
    result() {
      if (this.timer) {
        clearTimeout(this.timer);
      }
      const fuc = this.resetValue;
      this.timer = setTimeout(function () {
        // console.log("called timer");
        fuc();
      }, 5000);
    },
  },
  computed: {
    showText() {
      if (this.result > 37) {
        return "Too much!";
      }
      if (this.result === 37) {
        return "Perfect";
      }
      return "Not there yet";
    },
  },
  methods: {
    add(num) {
      this.result += num;
    },
    resetValue() {
      this.result = 0;
    },
  },
}).mount("#assignment");
