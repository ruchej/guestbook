<template>
  <div id="app">
    <GuestBook msg="Welcome to Your GuestBook" />
    <FeedBack />
  </div>
</template>

<script>
import GuestBook from "./components/GuestBook.vue";
import FeedBack from "./components/FeedBack.vue";

export default {
  name: "App",
  components: {
    GuestBook,
    FeedBack
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
