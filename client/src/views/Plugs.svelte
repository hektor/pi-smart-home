<script>
  export let data = []
  import Togglable from '../components/Togglable.svelte'
</script>

<h1 class="text-gray-400 text-3xl mb-16">Plugs</h1>
{#each Object.values(data) as setting, i}
  <Togglable status={setting} type="plug" id={i} />
{/each}
