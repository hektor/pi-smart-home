<script>
  // Router
  import { Link } from 'svero'
  export let router = {}
  let currentPath = window.location.pathname

  import Tab from './Tab.svelte'

  // Icons
  import {
    SunIcon,
    ZapIcon,
    ShieldIcon,
    KeyIcon,
    ActivityIcon,
    MehIcon,
  } from 'svelte-feather-icons'
</script>

<div
  class="w-full h-16 flex flex-row fixed bottom-0 md:flex-col md:w-16 md:left-0
  md:flex-none md:top-0 md:my-32">
  <Tab href="/lights" icon={SunIcon} />
  <Tab href="/plugs" icon={ZapIcon} />
  <Tab href="/doors" icon={KeyIcon} />
  <Tab href="/security" icon={ShieldIcon} />
  <Tab href="/monitor" icon={ActivityIcon} />
  <Tab href="/character-generator" icon={MehIcon} />
</div>
