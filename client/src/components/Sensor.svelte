<script>
  // Firebase
  import { firestore } from '../firebase'
  export let value
  export let type
  export let unit
</script>

<div class="flex flex-col justify-center items-center mb-16">

  <h1 class="text-gray-400 text-xl capitalize">{type}</h1>
  {#if value}
    <p class="text-gray-600 text-5xl">{value.toFixed(2)} {unit}</p>
  {/if}

</div>
