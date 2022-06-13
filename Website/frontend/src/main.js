import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { store } from "./store";

// Set fontawesome component
// Create and config the app
createApp(App).use(store).use(router).mount("#app");
