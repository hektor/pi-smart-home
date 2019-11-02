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
  const unsubscribe = authState(auth).subscribe(u => (user = u))
  const title = 'Pi Hub'

  onMount(async () => {
    const lightsRef = await firestore
      .collection('devices')
      .doc('lights')
      .get()
    lightSettings = await lightsRef.data()
  })
</script>

<Header {title} />
{#each Object.values(lightSettings) as lightSetting, i}
  <Togglable turnedOn={lightSetting} id={i} />
{/each}
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
