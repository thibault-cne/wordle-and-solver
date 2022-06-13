<!--
  - Copyright (c)
  - Project : project2-E19
  -
  - -
  -
  - Author : thibault
  - File : HomePage.vue
  - Description : *Enter description here*
  -
  - -
  -
  - Last modification : 2022/4/5
  -->

<template>
  <div>
    <div class="content">
      <div class="col-12 col-s-12">
        <div class="row">
          <div class="col-6 col-s-6 center">
            <h2 class="title">TazMou</h2>
          </div>
        </div>
        <div>
          <div class="row">
            <div class="col-8 col-s-8 center">
              <div class="btn center">
                <router-link
                  :to="{ name: 'GrillePage' }"
                  class="nav-btn-link link"
                >
                  Nouvelle partie
                </router-link>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-8 col-s-8 center">
              <div class="btn center">
                <router-link
                  :to="{ name: 'LoginPage' }"
                  class="nav-btn-link link"
                >
                  Login
                </router-link>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-8 col-s-8 center">
              <div class="btn center">
                <router-link
                  :to="{ name: 'RegisterPage' }"
                  class="nav-btn-link link"
                >
                  Register
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomePage",
};
// Set the page name
document.title = "Acceuil";
</script>

<style lang="scss"></style>
