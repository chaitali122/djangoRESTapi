<template>
  <div id = "display">
    <button v-on:click="loadMovies">Show Movie</button>
    <table>
      <tr>
        <th>Id</th>
        <th>Name</th>
        <th>Director</th>
        <th>Genre</th>
        <th>Rating</th>
        <th>Release Date</th>
      </tr>
      <tr v-for="item in items" :key="item.id">
        <td >{{item.id}}</td>
        <td >{{item.name}}</td>
        <td >{{item.director}}</td>
        <td >{{item.genre}}</td>
        <td >{{item.rating}}</td>
        <td >{{item.release_date}}</td>
      </tr>
    </table>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  name: 'App',
  data() {
    return {
      items: []
    };
  },
  methods: {
    loadMovies: function() {
      axios.get('/api/movies/').then(
        response => {
          this.items = response.data;
        }
      );
    },
  created() {
    this.loadMovies();
  }
}
}
</script>

<style>
table, th, td,button {
  border: 1px solid black;
  margin: 20px;
  padding: 10px;
}
</style>