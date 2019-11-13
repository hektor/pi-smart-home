<script>
  // Firebase
  import { firestore } from '../firebase'
  export let value
  export let type
  export let unit
</script>

<style>

</style>

<h1>{type}</h1>
{#if value}
  <h1>Value {value.toFixed(2)} {unit}</h1>
{/if}
