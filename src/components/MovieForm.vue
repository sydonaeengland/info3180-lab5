<template>
  <div class="container">
    <h2>Upload Form</h2>

    <!-- Success Message -->
    <div v-if="successMessage" class="alert alert-success">
      {{ successMessage }}
    </div>

    <!-- Error Messages -->
    <div v-if="errors.length" class="alert alert-danger">
      <ul>
        <li v-for="(error, index) in errors" :key="index">{{ error }}</li>
      </ul>
    </div>

    <!-- Upload Form -->
    <form
      @submit.prevent="saveMovie"
      id="movieForm"
      enctype="multipart/form-data"
    >
      <div class="form-group mb-3">
        <label for="title">Movie Title</label>
        <input type="text" name="title" class="form-control" />
      </div>

      <div class="form-group mb-3">
        <label for="description">Description</label>
        <textarea name="description" class="form-control"></textarea>
      </div>

      <div class="form-group mb-3">
        <label for="poster">Photo Upload</label>
        <input type="file" name="poster" class="form-control" />
      </div>

      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const successMessage = ref("");
const errors = ref([]);
const csrf_token = ref("");

onMounted(() => {
  getCsrfToken();
});

function getCsrfToken() {
  fetch("/api/v1/csrf-token")
    .then((response) => response.json())
    .then((data) => {
      csrf_token.value = data.csrf_token;
    });
}

function saveMovie() {
  successMessage.value = "";
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
        successMessage.value = data.message;
      } else if (data.errors) {
        errors.value = data.errors;
      }
    })
    .catch((error) => {
      console.log("Submission error:", error);
    });
}
</script>

<style scoped>
.form-group {
  margin-bottom: 1rem;
}
</style>
