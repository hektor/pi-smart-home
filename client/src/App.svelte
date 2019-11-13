<script>
  // Routing
  import { Router, Route } from 'svero'
  import Signin from './views/Signin.svelte'
  import Lights from './views/Lights.svelte'
  import Plugs from './views/Plugs.svelte'
  import Doors from './views/Doors.svelte'
  import Monitor from './views/Monitor.svelte'
  import Security from './views/Security.svelte'
  import About from './views/About.svelte'

  // Svelte
  import { onMount } from 'svelte'

  // Firebase
  import { auth, googleProvider, firestore } from './firebase'
  import { authState } from 'rxfire/auth'

  // Components
  import Header from './components/Header.svelte'
  import Tabbar from './components/Tabbar.svelte'
  import Togglable from './components/Togglable.svelte'

  import { getAllFromDocument } from './helpers/firestore'

  // Variables
  let user
  let lightSettings = []
  let plugSettings = []
  let doorSettings = []
  let sensorData = []
  const unsubscribe = authState(auth).subscribe(u => (user = u))
  const title = 'Pi Hub'

  onMount(() => {
    getAllFromDocument('devices', 'lights').then(data => {
      lightSettings = data
    })

    getAllFromDocument('devices', 'plugs').then(data => {
      plugSettings = data
    })

    getAllFromDocument('devices', 'doors').then(data => {
      doorSettings = data
    })

    getAllFromDocument('devices', 'sensors').then(data => {
      sensorData = data
    })
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
<div class="ml-32">
  <Router>
    <Route path="*" component={Signin} />
    <Route path="/about" component={About} />
    <Route path="/lights" component={Lights} data={lightSettings} />
    <Route path="/plugs" component={Plugs} data={plugSettings} />
    <Route path="/doors" component={Doors} data={doorSettings} />
    <Route path="/security" component={Security} />
    <Route path="/monitor" component={Monitor} data={sensorData} />
    <Tabbar />
  </Router>
</div>

<div class="flex md:flex-row-reverse flex-wrap">
  <div class="w-full md:w-4/5">
    <div class="container pt-16 px-6" />
    <!-- <div class="toggle-group lights">
      {#each Object.values(lightSettings) as lightSetting, i}
        <Togglable status={lightSetting} type="light" id={i} />
      {/each}
    </div> -->
    <!-- <div class="toggle-group plugs">
      {#each Object.values(plugSettings) as plugSetting, i}
        <Togglable status={plugSetting} type="plug" id={i} />
      {/each}
    </div> -->
    <!-- <div class="toggle-group doors">
      {#each Object.values(doorSettings) as doorSetting, i}
        <Togglable status={doorSetting} type="door" id={i} />
      {/each}
    </div> -->
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
</div>
