<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <el-row>
      <el-button type="primary" @click="showModal" round
        >Оставить отзыв</el-button
      >
    </el-row>
  </div>
</template>

<script>
import { eventEmitter } from "../main";

export default {
  name: "GuestBook",
  props: {
    msg: String
  },
  methods: {
    showModal() {
      eventEmitter.$emit("dialogVisible");
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
