<script>
  export let data = []
  import Togglable from '../components/Togglable.svelte'
</script>

<h1>Lights</h1>
{#each Object.values(data) as setting, i}
  <Togglable status={setting} type="light" id={i} />
{/each}
