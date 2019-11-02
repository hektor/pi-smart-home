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

<style>
  button {
    transition: all 120ms cubic-bezier(0.5, 0.82, 0.165, 1);
    @apply bg-gray-800 m-2 w-8 h-8 rounded shadow-lg;
  }

  button:hover {
    @apply bg-gray-700;
  }

  .active {
    background: #fff;
  }
</style>

<button on:click={toggleStatus} class={status ? 'active' : ''} />
