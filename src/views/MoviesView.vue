<script setup>
import { ref, onMounted } from "vue";

let movies = ref([]);

function fetchMovies() {
  fetch("/api/v1/movies")
    .then((response) => response.json())
    .then((data) => {
      movies.value = data.movies;
    });
}

onMounted(() => {
  fetchMovies();
});
</script>

<template>
  <div class="container">
    <h2 class="my-4">Movies</h2>
    <div class="row">
      <div class="col-md-6 mb-4" v-for="movie in movies" :key="movie.id">
        <div class="card h-100 d-flex flex-row">
          <img :src="movie.poster" class="movie-img" :alt="movie.title" />
          <div class="card-body">
            <h5 class="card-title">{{ movie.title }}</h5>
            <p class="card-text">{{ movie.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.movie-img {
  width: 100px;
  height: 150px;
  object-fit: cover;
  border-top-left-radius: 0.25rem;
  border-bottom-left-radius: 0.25rem;
}
.card-body {
  padding: 0.75rem;
}
.card-title {
  margin-bottom: 0.5rem;
  font-weight: 600;
}
.card-text {
  font-size: 0.9rem;
  color: #555;
}
</style>
