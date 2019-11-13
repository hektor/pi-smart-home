<script>
  import { toggleAlarm, getAlarmStatus } from '../helpers/firestore'
  import { onMount } from 'svelte'
  let status = false
  onMount(() => {
    getAlarmStatus().then(currentStatus => {
      status = currentStatus
    })
  })
  const handleAlert = () => {
    toggleAlarm()
    status = !status
  }
</script>

<style>
  button {
    width: 10rem;
    height: 10rem;
    @apply bg-gray-600 rounded-full;
  }

  .active {
    background: red;
  }
</style>

<h1>Security</h1>
<button class={status ? 'active' : ''} on:click={handleAlert}>
  {status ? 'Alarming!' : 'Press for alarm'}
</button>
