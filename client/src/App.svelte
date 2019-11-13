<script>
  // Routing
  import { Router, Route } from 'svero'
  import Signin from './views/Signin.svelte'
  import Lights from './views/Lights.svelte'
  import Plugs from './views/Plugs.svelte'
  import Doors from './views/Doors.svelte'
  import Monitor from './views/Monitor.svelte'
  import Security from './views/Security.svelte'
  import CharacterGenerator from './views/CharacterGenerator.svelte'

  // Svelte
  import { onMount } from 'svelte'

  // Components
  import Header from './components/Header.svelte'
  import Tabbar from './components/Tabbar.svelte'
  import Togglable from './components/Togglable.svelte'
  import MainLayout from './layouts/MainLayout.svelte'

  // Helpers
  import { getAllFromDocument } from './helpers/firestore'

  // Variables
  let lightSettings = []
  let plugSettings = []
  let doorSettings = []
  let sensorData = []
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
<MainLayout>
  <Router>
    <Route path="*" component={Signin} />
    <Route path="/lights" component={Lights} data={lightSettings} />
    <Route path="/plugs" component={Plugs} data={plugSettings} />
    <Route path="/doors" component={Doors} data={doorSettings} />
    <Route path="/security" component={Security} />
    <Route path="/monitor" component={Monitor} data={sensorData} />
    <Route path="/character-generator" component={CharacterGenerator} />
    <Tabbar />
  </Router>
</MainLayout>
