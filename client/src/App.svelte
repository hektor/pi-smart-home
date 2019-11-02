<script>
  // Svelte
  import { onMount } from 'svelte'

  // Firebase
  import { auth, googleProvider, firestore } from './firebase'
  import { authState } from 'rxfire/auth'

  // Components
  import Header from './Header.svelte'
  import Nav from './Nav.svelte'
  import Togglable from './Togglable.svelte'

  // Variables
  let user
  let lightSettings = []
  let plugSettings = []
  let doorSettings = []
  const unsubscribe = authState(auth).subscribe(u => (user = u))
  const title = 'Pi Hub'

  onMount(async () => {
    const lightsRef = await firestore
      .collection('devices')
      .doc('lights')
      .get()
    lightSettings = await lightsRef.data()
  })

  onMount(async () => {
    const plugsRef = await firestore
      .collection('devices')
      .doc('plugs')
      .get()
    plugSettings = await plugsRef.data()
  })

  onMount(async () => {
    const doorsRef = await firestore
      .collection('devices')
      .doc('doors')
      .get()
    doorSettings = await doorsRef.data()
  })
</script>

<style>
  .toggle-group {
    flex: 1;
  }

  button {
    transition: all 120ms cubic-bezier(0.5, 0.82, 0.165, 1);
  }

  button:hover {
    @apply bg-gray-700;
  }
</style>

<Header {title} />
<div class="flex md:flex-row-reverse flex-wrap">
  <div class="w-full md:w-4/5">
    <div class="container pt-16 px-6" />
    <div class="toggle-group lights">
      {#each Object.values(lightSettings) as lightSetting, i}
        <Togglable status={lightSetting} type="light" id={i} />
      {/each}
    </div>
    <div class="toggle-group plugs">
      {#each Object.values(plugSettings) as plugSetting, i}
        <Togglable status={plugSetting} type="plug" id={i} />
      {/each}
    </div>
    <div class="toggle-group doors">
      {#each Object.values(doorSettings) as doorSetting, i}
        <Togglable status={doorSetting} type="door" id={i} />
      {/each}
    </div>
    <div>
      {#if user}
        <button
          on:click={() => auth.signOut()}
          class="bg-gray-800 text-white font-bold rounded
          hover:border-yellow-600 hover:bg-yellow-500 hover:text-white shadow-lg
          py-2 px-6 inline-flex items-center m-2">
          Sign out
        </button>
      {:else}
        <button
          on:click={() => auth.signInWithPopup(googleProvider)}
          class="bg-gray-800 text-white font-bold rounded shadow-lg py-2 px-6
          inline-flex items-center m-2">
          <span class="mr-2">Sign in with Google</span>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            viewBox="0 0 24 24">
            <path
              fill="currentcolor"
              d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z" />
          </svg>
        </button>
      {/if}
    </div>
  </div>
  <Nav />
</div>
