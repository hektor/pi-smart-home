import App from "./App.svelte";
import '.styles/utils.css'

const app = new App({
  target: document.body,
  props: {
    title: "Pi Hub"
  }
});

export default app;
