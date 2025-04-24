<template>
  <form @submit.prevent="saveMovie" id="movieForm">
    <div class="form-group mb-3">
      <label for="title" class="form-label">Movie Title</label>
      <input type="text" name="title" class="form-control" required />
    </div>

    <div class="form-group mb-3">
      <label for="description" class="form-label">Description</label>
      <textarea name="description" class="form-control" required></textarea>
    </div>

    <div class="form-group mb-3">
      <label for="poster" class="form-label">Movie Poster</label>
      <input type="file" name="poster" class="form-control" required />
    </div>

    <button type="submit" class="btn btn-primary">Submit</button>

    <div v-if="message" class="alert alert-success mt-3">
      {{ message }}
    </div>

    <ul v-if="errors.length" class="alert alert-danger mt-3">
      <li v-for="(error, index) in errors" :key="index">{{ error }}</li>
    </ul>
  </form>
</template>

<script setup>
import { ref, onMounted } from "vue";

const csrf_token = ref("");
const message = ref("");
const errors = ref([]);

function getCsrfToken() {
  fetch("/api/v1/csrf-token")
    .then((response) => response.json())
    .then((data) => {
      csrf_token.value = data.csrf_token;
    })
    .catch((error) => {
      console.error("CSRF fetch error:", error);
    });
}

function saveMovie() {
  message.value = "";
  errors.value = [];

  let movieForm = document.getElementById("movieForm");
  let form_data = new FormData(movieForm);

  fetch("/api/v1/movies", {
    method: "POST",
    body: form_data,
    headers: {
      "X-CSRFToken": csrf_token.value,
    },
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.message) {
        message.value = data.message;
        movieForm.reset();
      } else if (data.errors) {
        errors.value = data.errors;
      }
    })
    .catch((error) => {
      console.error("Submission error:", error);
    });
}

onMounted(() => {
  getCsrfToken();
});
</script>

<style scoped>
.form-group {
  margin-bottom: 1rem;
}
</style>
