<!--
  - Copyright (c)
  - Project : project2-E19
  -
  - -
  -
  - Author : thibault
  - File : ConfigComp.vue
  - Description : *Enter description here*
  -
  - -
  -
  - Last modification : 2022/4/12
  -->

<template>
  <div class="config-form popup-form col-4 col-s-9">
    <div class="close-btn" v-on:click="toggleConfig">&times;</div>
    <h2 class="form-title">Configuration</h2>
    <div class="form-element">
      <label for="config-maxletters">Nombre de lettres par mot</label>
      <input
        type="range"
        id="config-maxletters"
        v-model="this.nbLetter"
        min="5"
        max="10"
        step="1"
      />
      <output>{{ this.nbLetter }}</output>
    </div>
    <div class="form-element">
      <label for="config-tries">Nombre de tentatives</label>
      <input
        type="range"
        id="config-tries"
        v-model="this.nbTries"
        min="1"
        max="10"
        step="1"
      />
      <output>{{ this.nbTries }}</output>
    </div>
    <button
      class="submit-button"
      id="validate-config-modification"
      v-on:click="sendConfig"
    >
      Enregister les modifications
    </button>
  </div>
</template>

<script>
import { postRequest } from "@/js/requests/postRequest";
import { store } from "@/store";

export default {
  name: "ConfigComp",
  data: function () {
    return {
      nbLetter: this.initialNbLetter,
      nbTries: this.initialNbTries,
    };
  },
  props: {
    initialNbLetter: Number,
    initialNbTries: Number,
  },
  methods: {
    toggleConfig() {
      store.commit("togglePopup");
    },
    sendConfig() {
      this.toggleConfig();
      const data = {
        wordLength: this.nbLetter,
        maxTries: this.nbTries,
      };
      postRequest(data, "/config-api/set", "json").then(() => {
        location.reload();
      });
    },
  },
};
</script>

<style lang="scss"></style>
