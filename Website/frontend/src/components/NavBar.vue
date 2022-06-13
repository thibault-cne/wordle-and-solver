<!--
  - Copyright (c)
  - Project : project2-E19
  -
  - -
  -
  - Author : thibaulmt
  - File : NavBar.vue
  - Description : *Enter description here*
  -
  - -
  -
  - Last modification : 2022/4/1
  -->

<template>
  <div>
    <div class="navbar row">
      <div class="desk-navbar col-s-12 col-12">
        <div class="nav-left row">
          <div class="nav-brand nav-link">
            <router-link :to="{ name: 'HomePage' }">TazMou</router-link>
          </div>
          <div class="nav-item" v-on:click="displayConfig" v-if="noConfig">
            Config
          </div>
          <div class="nav-link nav-item">
            <router-link :to="{ name: 'LeaderBoard' }">LeaderBoard</router-link>
          </div>
          <div class="nav-item dropdown">
            Jeux
            <div class="dropdown-menu dropdown-menu-animated hover-nav-link">
              <router-link :to="{ name: 'GrillePage' }">Classique</router-link>
              <router-link :to="{ name: 'DailyWord' }">Mot du jour</router-link>
              <router-link :to="{ name: 'GrilleWordleTI' }"
                >Absurdle</router-link
              >
            </div>
          </div>
        </div>
        <div class="nav-right row">
          <div class="nav-item nav-link" v-if="userLoggedIn">
            <router-link :to="{ name: 'ProfilPage' }">Profil</router-link>
          </div>
          <div class="nav-item nav-link">
            <router-link v-if="!userLoggedIn" :to="{ name: 'LoginPage' }">
              Login
            </router-link>
            <router-link v-else :to="{ name: 'LogoutComp' }">
              Logout
            </router-link>
          </div>
        </div>
      </div>
      <div class="phone-navbar col-12 col-s-12">
        <div class="menu-icon" v-on:click="displayNavbar($event)">
          <div class="bar-1"></div>
          <div class="bar-2"></div>
          <div class="bar-3"></div>
          <div class="bar-4"></div>
          <div class="bar-5"></div>
        </div>
        <div class="nav-content">
          <div class="col-2 col-s-2 nav-brand nav-link">
            <router-link :to="{ name: 'HomePage' }">TazMou</router-link>
          </div>
          <div
            class="col-3 col-s-3 nav-item"
            v-on:click="displayConfig"
            v-if="noConfig"
          >
            Config
          </div>
          <div class="col-2 col-s-2 nav-link nav-item">
            <router-link :to="{ name: 'LeaderBoard' }">LeaderBoard</router-link>
          </div>
          <div class="col-1 col-s-1 nav-item dropdown">
            Jeux
            <div class="dropdown-menu dropdown-menu-animated hover-nav-link">
              <router-link :to="{ name: 'GrillePage' }">Classique</router-link>
              <router-link :to="{ name: 'DailyWord' }">Mot du jour</router-link>
              <router-link :to="{ name: 'GrilleWordleTI' }"
                >Absurdle</router-link
              >
            </div>
          </div>
          <div class="col-3 col-s-3 nav-item nav-link" v-if="userLoggedIn">
            <router-link :to="{ name: 'ProfilPage' }">Profil</router-link>
          </div>
          <div class="col-3 col-s-3 nav-item nav-link">
            <router-link v-if="!userLoggedIn" :to="{ name: 'LoginPage' }">
              Login
            </router-link>
            <router-link v-else :to="{ name: 'LogoutComp' }">
              Logout
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import ConfigComp from "@/components/ConfigComp";

export default {
  name: "NavBar",
  computed: {
    ...mapGetters({
      userLoggedIn: "loggedIn",
      active: "isActivePopup",
      noConfig: "noConfig",
    }),
  },
  data() {
    return {
      config: {
        loaded: false,
      },
    };
  },
  methods: {
    displayNavbar(event) {
      event.currentTarget.parentElement.classList.toggle("active");
    },
    displayConfig() {
      ConfigComp.methods.toggleConfig();
    },
  },
};
</script>

<style lang="scss"></style>
