<!--
  - Copyright (c)
  - Project : project2-E19
  -
  - -
  -
  - Author : thibault
  - File : LoginPage.vue
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
        <h1 class="form-title">Login</h1>
      </div>
      <div class="form-content row">
        <div class="col-9 col-s-10 center">
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
              <p class="error-msg">
                Nom d'utilisateur ou mot de passe incorrect.
              </p>
              <p class="register-link">
                <router-link :to="{ name: 'RegisterPage' }" class="link">
                  Pour vous créer un compte cliquer ici
                </router-link>
              </p>
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
export default {
  name: "LoginPage",
  data() {
    return {
      username: "",
      password: "",
      incorrectAuth: false,
    };
  },
  methods: {
    sendLogin() {
      this.$store
        .dispatch("userLogin", {
          username: this.username,
          password: this.password,
        })
        .then((response) => {
          if (response === "success") {
            this.$router.push({ name: "GrillePage" });
          } else {
            this.incorrectAuth = true;
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};

// Page name
document.title = "Login";
</script>

<style lang="scss"></style>
