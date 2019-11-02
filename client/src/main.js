import App from "./App.svelte";
import './utils.css'

const app = new App({
  target: document.body,
  props: {
    title: "Pi Hub"
  }
});

export default app;
