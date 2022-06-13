<!--
  - Copyright (c)
  - Project : project2-E19
  -
  - -
  -
  - Author : louis chatard and kelian moy
  - File : ProfilPage.vue
  - Description : *Enter description here*
  -
  - -
  -
  - Last modification : 2022/4/26
  -->

<template>
  <NavBar />
  <div class="profil">
    <div class="changePicture">
      <div class="picture">
        <img v-if="url" :src="url" />
        <img v-else src="../../public/ProfilPictures/taz.png" />
      </div>
      <div class="form-picture">
        <form method="POST" enctype="multipart/form-data">
          <label class="picture-change" for="picture">
            Changer de photo de profil
          </label>
          <input
            id="picture"
            name="picture"
            type="file"
            accept="image/*"
            @change="onFileChange"
            style="display: none"
            method="POST"
            enctype="multipart/form-data"
          />
          <button class="submit-btn" type="button" @click="uploadPicture">
            Enregister
          </button>
        </form>
      </div>
    </div>
    <div class="formulaire">
      <div class="profilUser">
        <h1>{{ this.username }}</h1>
        <label>Changer de nom d'utilisateur</label>
        <div class="form-element">
          <input
            id="new_username"
            name="new_username"
            placeholder="Nouveau nom d'utilisateur"
            type="text"
            v-model="new_username"
          />
        </div>
        <div v-if="this.status === 'alreadyUsedUsername'" class="">
          Nom d'utilisateur déjà pris, veuillez essayer autre chose.
        </div>
        <div class="changeUser">
          <button class="submit-btn" @click="changeUsername">
            Changer de nom d'utilisateur
          </button>
        </div>
        <br />
      </div>
      <div class="profilPassword form-element">
        <label>Changer de mot de passe</label>
        <input
          id="password"
          name="password"
          placeholder="Entrez votre nouveau mot de passe"
          type="password"
          v-model="password"
        />
        <div class="changePassword">
          <button class="submit-btn" @click="changePassword">
            Changer de mot de passe
          </button>
        </div>
      </div>
      <div class="btn" type="button">
        <router-link class="nav-btn-link link" :to="{ name: 'ReplaysPage' }">
          Voir mes replays
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar";
import { mapGetters } from "vuex";
import { getRequest } from "@/js/requests/getRequest";
import { postRequest } from "@/js/requests/postRequest";
import { store } from "@/store";

export default {
  name: "ProfilePage",
  components: {
    NavBar,
  },
  computed: {
    ...mapGetters({
      userLoggedIn: "loggedIn",
    }),
  },
  data() {
    return {
      username: "",
      new_username: "",
      password: "",
      picturePath: "../../../Data/ProfilPictures/taz.png ",
      showPassword: false,
      image: document.getElementById("picture"),
      url: null,
      picture: [],
      status: "",
    };
  },
  created() {
    this.getInfo();
    this.getPicture();
  },
  methods: {
    async getInfo() {
      await getRequest("/profil-api/getinfo", "json").then((response) => {
        console.log(response);
        this.username = response.data.username;
      });
    },
    async getPicture() {
      await getRequest("/profil-api/getPicture", "file").then((response) => {
        console.log(response);
        this.picture = response.data.picture;
      });
    },
    onFileChange(e) {
      this.picture = e.target.files[0];
      const file = e.target.files[0];
      this.url = URL.createObjectURL(file);
    },
    uploadPicture() {
      let formData = new FormData();
      formData.append("image", this.picture);
      postRequest(formData, "/profil-api/changePicture", "file").then(
        (response) => {
          console.log(response);
        }
      );
    },
    changeUsername() {
      postRequest(
        { new_username: this.new_username },
        "/profil-api/changeUsername",
        "json"
      )
        .then((response) => {
          if (response.data.status === "success") {
            store.commit("updateStorage", {
              access: response.data.access,
              refresh: response.data.refresh,
            });
            this.username = this.new_username;
            this.status = "new_username_succesfull";
          } else if (response.data.status === "alreadyUsedUsername") {
            this.status = "alreadyUsedUsername";
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    changePassword() {
      postRequest(
        { password: this.password },
        "/profil-api/changePassword",
        "json"
      )
        .then((response) => {
          if (response === "success") {
            this.statut = "new_password_succesfull";
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};

// Page name
document.title = "Profil";
</script>

<style lang="scss"></style>
