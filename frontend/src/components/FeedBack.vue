<template>
  <el-dialog title="Оставить комментарий" :visible.sync="dialogVisible">
    <el-form :model="form">
      <el-form-item label="Ваше имя" :label-width="formLabelWidth">
        <el-input
          v-model="form.name"
          maxlength="32"
          minlength="3"
          show-word-limit
          validate-event
        ></el-input>
      </el-form-item>
      <el-form-item label="Сообщение" :label-width="formLabelWidth">
        <el-input
          type="textarea"
          :rows="2"
          v-model="form.textarea"
          maxlength="512"
          minlength="16"
          show-word-limit
          validate-event
        ></el-input>
      </el-form-item>
      <el-form-item>
        <input
          type="file"
          id="file"
          ref="file"
          v-on:change="handleFileUpload()"
        />
      </el-form-item>
    </el-form>
    <span slot="footer" class="dialog-footer">
      <el-button @click="formClear">Отмена</el-button>
      <el-button type="primary" @click="sendResponse">Отправить</el-button>
    </span>
  </el-dialog>
</template>

<script>
import { eventEmitter } from "../main";

const axios = require("axios").default;
const APIPostGR = "//localhost:8000/api/v1/create";

export default {
  data() {
    return {
      file: "",
      dialogVisible: false,
      formLabelWidth: "120px",
      form: {
        name: "",
        textarea: ""
      }
    };
  },
  methods: {
    formClear() {
      this.form.name = "";
      this.form.textarea = "";
      this.dialogVisible = false;
    },
    sendResponse() {
      let data = new FormData();
      data.append("name", this.form.name);
      data.append("body", this.form.textarea);
      data.append("img", this.file);
      axios
        .post(APIPostGR, data)
        .then(function(response) {
          console.log(response);
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    handleFileUpload() {
      this.file = this.$refs.file.files[0];
    }
  },
  mounted() {
    eventEmitter.$on("dialogVisible", () => {
      this.dialogVisible = true;
    });
  }
};
</script>
