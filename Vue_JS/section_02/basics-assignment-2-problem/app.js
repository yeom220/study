Vue.createApp({
  data() {
    return {
      inputedText: "",
      confirmedText: "",
    };
  },
  methods: {
    showAlert() {
      alert("alert");
    },
    showInputed(e) {
      this.inputedText = e.target.value;
    },
    confirmInputed(e) {
      this.confirmedText = e.target.value;
    },
  },
}).mount("#assignment");
