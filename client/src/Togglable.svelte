<script>
  // Firebase
  import { firestore } from './firebase'
  export let status
  export let id
  export let type
  const collectionTypes = {
    light: {
      collectionName: 'lights',
    },
    plug: {
      collectionName: 'plugs',
    },
    door: {
      collectionName: 'doors',
    },
  }
  function toggleStatus() {
    status = !status
    firestore
      .collection('devices')
      .doc(collectionTypes[type].collectionName)
      .update({
        [id]: status,
      })
  }
</script>

{#if status}
  <button on:click={toggleStatus}>⚪</button>
{:else}
  <button on:click={toggleStatus}>⚫</button>
{/if}
