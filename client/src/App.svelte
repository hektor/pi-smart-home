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
</style>

<Header {title} />
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
    <button on:click={() => auth.signOut()}>Sign out</button>
  {:else}
    <button on:click={() => auth.signInWithPopup(googleProvider)}>
      Sign in with Google
    </button>
  {/if}
</div>
<Nav />
