<script>
  import {
    SunIcon,
    ZapIcon,
    ShieldIcon,
    KeyIcon,
    ActivityIcon
  } from 'svelte-feather-icons';
</script>

<style>
  nav {
    display: flex;
    position: fixed;
    overflow: hidden;
    bottom: 0;
  }

  a {
    flex: 1;
    text-align: center;
    padding: 1rem;
  }
</style>

<nav>
  <a href="/">
    <SunIcon />
    Lights
  </a>
  <a href="/">
    <ZapIcon />
    Sockets
  </a>
  <a href="/">
    <KeyIcon />
    Doors
  </a>
  <a href="/">
    <ActivityIcon />
    Sensors
  </a>
  <a href="/">
    <ShieldIcon />
    Security
  </a>
</nav>
