<script>
  import {
    SunIcon,
    ZapIcon,
    ShieldIcon,
    KeyIcon,
    ActivityIcon,
  } from 'svelte-feather-icons'
</script>

<style>
  .nav-item {
    @apply p-2;
  }
  a {
    transition: all 120ms cubic-bezier(0.5, 0.82, 0.165, 1);
    @apply text-gray-800;
  }

  a:hover {
    @apply text-gray-500;
  }
</style>

<div
  class="w-full h-16 flex flex-row fixed bottom-0 md:flex-col md:w-16 md:left-0
  md:flex-none md:top-0 md:my-32">
  <div class="nav-item flex-1">
    <a href="/lights">
      <SunIcon />
    </a>
  </div>
  <div class="nav-item flex-1">
    <a href="/plugs">
      <ZapIcon />
    </a>
  </div>
  <div class="nav-item flex-1">
    <a href="/doors">
      <KeyIcon />
    </a>
  </div>
  <div class="nav-item flex-1">
    <a href="/security">
      <ShieldIcon />
    </a>
  </div>
</div>
