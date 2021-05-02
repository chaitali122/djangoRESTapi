<template>
<div id="app">
    <h2>Add a New Movie</h2>
    <form @submit.prevent="addMovie">
      <input v-model="newName" placeholder="Name">
      <input v-model="newDirector" placeholder="Director">
      <input v-model="newGenre" placeholder="Genre">
      <input v-model="newRating" placeholder="Rating">
      <input v-model="newReleaseDate" placeholder="Release Date">
      <button v-on:click="addMovie">Add Movie</button>
    </form>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  name: 'App',
  data() {
    return {
      newName: "",newDirector: "",newGenre:"",newRating:"",newReleaseDat:"",
    };
  },
  methods: {
    addMovie: function() {
      axios.post('/api/movies/', {name: this.newName, director: this.newDirector,genre: this.newGenre,rating: this.newRating,release_date: this.newReleaseDate }).then(
        response => {
          this.newName = "";
          this.newDirector = "";
          this.newGenre = "";
          this.newRating = "";
          this.newReleaseDate = "";
        }
      )
    }
  },
}
</script>
<style>
html, body {
  margin: 0;
  padding: 0;
  font-family: Avenir, Helvetica, Arial, sans-serif;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #2c3e50;
  width: 100vw;
  min-width: 300px;
  max-width: 1000px;
  margin: 0 auto;
}
h2 {
  margin: 10px;
}
input{
  margin: 5px;
  padding: 5px;
}
form {
  margin: 20px;
  display: flex;
  flex-direction: column;
}
form textarea {
  resize: none;
  height: 50px;
  margin: 10px;
  background: beige;
  outline: none !important;
  border: none;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.4);
  border-radius: 5px;
  padding: 10px;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-size: 1em;
}
form button {
  background: lightgreen;
  color: darkgreen;
  padding: 10px;
  border: none;
  border-radius: 5px;
  margin: 10px;
  cursor: pointer;
  outline: none !important;
}
form button:hover {
  background-color: #a0fea0;
}
</style>