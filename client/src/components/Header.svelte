<script>
  export let title
  import FirebaseLogo from '../assets/FirebaseLogo.svelte'

  // Firebase
  import { auth, googleProvider, firestore } from '../firebase'
  import { authState } from 'rxfire/auth'
  let user
  const unsubscribe = authState(auth).subscribe(u => (user = u))
</script>

<style>
  header {
    @apply shadow-xl flex justify-between;
  }

  button {
    @apply bg-gray-800 text-white font-bold rounded  shadow-lg py-2 px-6 inline-flex
        items-center;
  }

  button:hover {
    @apply border-yellow-600 bg-yellow-500 text-white;
  }
</style>

<header class="p-4">
  <a href="/">
    <FirebaseLogo />
  </a>
  <div>
    {#if user}
      <button on:click={() => auth.signOut()}>Sign out</button>
    {:else}
      <button on:click={() => auth.signInWithPopup(googleProvider)}>
        <span class="mr-2">Sign in with Google</span>
      </button>
    {/if}
  </div>
</header>
