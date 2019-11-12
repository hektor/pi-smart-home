<script>
  export let router = {}
  export let settings = []
  import Togglable from '../components/Togglable.svelte'
</script>

<h1>Doors</h1>
{#each Object.values(settings) as setting, i}
  <Togglable status={setting} type="door" id={i} />
{/each}
