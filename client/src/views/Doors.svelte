<script>
  export let router = {}
  export let data = []
  import Togglable from '../components/Togglable.svelte'
</script>

<h1>Doors</h1>
{#each Object.values(data) as setting, i}
  <Togglable status={setting} type="door" id={i} />
{/each}
