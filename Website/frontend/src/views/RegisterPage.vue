<!--
  - Copyright (c)
  - Project : project2-E19
  -
  - -
  -
  - Author : thibault
  - File : RegisterPage.vue
  - Description : *Enter description here*
  -
  - -
  -
  - Last modification : 2022/4/5
  -->

<template>
  <div class="row form">
    <div class="">
      <router-link :to="{ name: 'HomePage' }">
        <img
          class="houseImg"
          src="../../public/Icons/house-solid.svg"
          alt="Retour au menu"
        />
      </router-link>
    </div>
    <div class="col-s-10 col-8 center">
      <div class="form-title">
        <h1 class="form-title">Register</h1>
      </div>
      <div class="form-content row">
        <div class="col-8 col-s-10 center">
          <div class="form-element">
            <label>Nom d'utilisateur</label>
            <input
              id="username"
              name="username"
              placeholder="Entrez votre nom d'utilisateur"
              type="text"
              v-model="username"
            />
          </div>
          <div class="form-element">
            <label>Mot de passe</label>
            <input
              id="password"
              name="password"
              placeholder="Entrez votre mot de passe"
              type="password"
              v-model="password"
            />
          </div>
          <transition name="bounce">
            <div v-if="incorrectAuth" class="warning">
              <p class="error-msg">Une erreur est survenue.</p>
            </div>
          </transition>
          <div class="form-element">
            <button class="submit-btn" v-on:click="sendLogin">Valider</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { postRequest } from "@/js/requests/postRequest";
import { store } from "@/store";
import router from "@/router";

export default {
  name: "RegisterPage",
  data() {
    return {
      username: "",
      password: "",
      incorrectAuth: false,
    };
  },
  methods: {
    sendLogin() {
      let data = {
        username: this.username,
        password: this.password,
      };
      postRequest(data, "/auth-api/register", "json")
        .then(function (response) {
          if (response.data.status) {
            store.commit("updateStorage", {
              access: response.data.access,
              refresh: response.data.refresh,
            });
            router.push({ name: "GrillePage" });
          } else {
            this.incorrectAuth ^= true;
          }
        })
        .catch(function (err) {
          console.log(err);
        });
    },
  },
};
</script>

<style lang="scss"></style>
