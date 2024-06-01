const app = Vue.createApp({
  data() {
    return {
      counter: 10,
      inputText: "",
      lastText: "",
      confirmedText: "",
      // fullText: "",
    };
  },
  watch: {
    counter(value) {
      if (value > 50) {
        this.counter = 0;
      }
    },
    // inputText(value) {
    //   // console.log("call fullText");
    //   if (value === "") {
    //     if (this.lastText === "") {
    //       this.fullText = "";
    //     } else {
    //       this.fullText = this.lastText;
    //     }
    //   } else {
    //     this.fullText = value + " " + this.lastText;
    //   }
    // },
    // lastText(value) {
    //   if (value === "") {
    //     if (this.inputText === "") {
    //       this.fullText = "";
    //     } else {
    //       this.fullText = this.inputText;
    //     }
    //   } else {
    //     this.fullText = this.inputText + " " + value;
    //   }
    // },
  },
  computed: {
    fullText() {
      // console.log("call outputFullText");
      if (this.inputText === "" && this.lastText === "") {
        return "";
      }
      return this.inputText + " " + this.lastText;
    },
  },
  methods: {
    outputFullText() {
      console.log("call outputFullText");
      if (this.inputText == "") {
        return "";
      }
      return this.inputText + " " + "INIT";
    },
    resetInput() {
      this.inputText = "";
    },
    confirmText() {
      this.confirmedText = this.inputText;
    },
    submitForm(e) {
      // e.preventDefault();
      alert("submitted!");
    },
    setText(e) {
      this.inputText = e.target.value;
    },
    add(n) {
      this.counter += n;
    },
    reduce(n) {
      this.counter -= n;
    },
  },
});

app.mount("#events");
