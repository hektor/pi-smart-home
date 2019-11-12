<script>
  export let href
  export let icon
  let currentPath = window.location.pathname
</script>

<style type="text/postcss">
  .nav-item {
    @apply p-2 py-4 flex-1 text-gray-800;
    transition: all 120ms cubic-bezier(0.5, 0.82, 0.165, 1);
  }
  .nav-item:hover {
    @apply text-gray-500;
  }

  .active {
    @apply text-orange-500;
  }
</style>

<div class="nav-item {currentPath === href ? 'active' : ''}">
  <a {href}>
    <svelte:component this={icon} />
  </a>
</div>
