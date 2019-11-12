<script>
  export let title
  import FirebaseLogo from '../assets/FirebaseLogo.svelte'
</script>

<style>
  header {
    @apply shadow-xl flex-1;
  }
</style>

<header class="p-4">
  <a href="/">
    <FirebaseLogo />
  </a>
</header>
