<script>
  import { onMount } from 'svelte'
  import { saveMatrix } from '../helpers/firestore'
  $: character = []
  const matrixSize = 8

  const generateCharacter = () => {
    let newChar = []
    for (let x = 0; x < Math.pow(matrixSize, 2); x++) {
      newChar.push(Math.random() > 0.5 ? 1 : 0)
    }
    character = newChar
  }

  onMount(() => {
    generateCharacter()
  })
</script>

<style>
  .grid-wrapper {
    display: inline-grid;
    grid-template-columns: repeat(8, 1fr);
    grid-template-rows: repeat(8, 1fr);
    grid-gap: 0.1rem;
  }

  .grid-item {
    width: 1rem;
    height: 1rem;
    @apply bg-gray-800 m-2 w-8 h-8 rounded shadow-lg;
  }

  .active {
    @apply bg-white;
  }

  button {
    @apply bg-gray-800 text-white font-bold rounded  shadow-lg py-2 px-6 inline-flex
        items-center m-2;
  }

  button:hover {
    @apply border-yellow-600 bg-yellow-500 text-white;
  }
</style>

<h1 class="text-gray-400 text-3xl mb-16">Character generator</h1>
<div class="grid-wrapper">
  {#each character as pixel}
    <div class="grid-item {pixel ? 'active' : ''}" />
  {/each}
</div>
<div class="flex mt-8">
  <button on:click={generateCharacter}>Generate character</button>
  <button on:click={() => saveMatrix('test', character)}>Save character</button>
</div>
