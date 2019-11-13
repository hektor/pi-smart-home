<script>
  export let data = []
  import Sensor from '../components/Sensor.svelte'
</script>

<h1 class="text-gray-400 text-3xl mb-16">Monitor</h1>
<Sensor type="temperature" value={data.temperature * 1} unit="°C" />
<Sensor type="humidity" value={data.humidity * 1} unit="%" />
