Vue.createApp({
  data() {
    return {
      tasks: [],
      inputTaskValue: "",
      visibleTasks: true,
    };
  },
  computed: {
    toggleBtnText() {
      return this.visibleTasks ? "Hide" : "Show";
    },
  },
  methods: {
    addTask() {
      this.tasks.push(this.inputTaskValue);
    },
    toggleTasks() {
      this.visibleTasks = !this.visibleTasks;
    },
  },
}).mount("#assignment");
