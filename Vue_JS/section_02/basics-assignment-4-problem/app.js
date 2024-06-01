Vue.createApp({
  data() {
    return {
      inputValue: "",
      visibleToggle: true,
      inputBgc: "",
    };
  },
  computed: {
    pCss() {
      if (this.inputValue === "user1") {
        return { user1: true };
      } else if (this.inputValue === "user2") {
        return { user2: true };
      }
    },
    toggle() {
      if (this.visibleToggle) {
        return { visible: true };
      } else {
        return { hidden: true };
      }
    },
  },
  methods: {
    clickToggle() {
      this.visibleToggle = !this.visibleToggle;
    },
    setInputBgc(e) {
      this.inputBgc = e.target.value;
    },
  },
}).mount("#assignment");
