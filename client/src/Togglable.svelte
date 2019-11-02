<script>
  // Firebase
  import { firestore } from './firebase'
  export let turnedOn
  export let id
  function toggleStatus() {
    turnedOn = !turnedOn
    const lightSetting = firestore
      .collection('devices')
      .doc('lights')
      .update({
        [id]: turnedOn,
      })
  }
</script>

{#if turnedOn}
  <button on:click={toggleStatus}>⚪</button>
{:else}
  <button on:click={toggleStatus}>⚫</button>
{/if}
