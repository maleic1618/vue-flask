<template>
  <div id="app">
    <h1>test app</h1>
    <button v-on:click="load">API Load!</button>
    {{message}}
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data () {
    return {
      message: ''
    }
  },
  methods: {
    load: function (event) {
      setTimeout(
        function () {
          axios.get('http://localhost:5000/api/users')
            .then(response => (this.message = response.data))
        }.bind(this), 1000)
    }
  }
}
</script>
