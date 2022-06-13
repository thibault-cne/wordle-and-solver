<!--
  - Copyright (c)
  - Project : project2-E19
  -
  - -
  -
  - Author : louiscleriot
  - File : grillewordl.vue
  - Description : *Enter description here*
  -
  - -
  -
  - Last modification : 2022/4/4
  -->

<template>
  <div v-bind:class="{ active: isActive }">
    <div class="under-popup-content">
      <NavBar />
      <div class="row">
        <div class="col-6 col-s-6 center">
          <h3 class="center-txt">Absurdl</h3>
        </div>
      </div>
      <div class="row">
        <div class="col-4 col-s-8 center">
          <div
            class="game-message-inexistant"
            v-if="this.retourapi === 'inconnu'"
          >
            Le mot n'existe pas dans le dictionnaire
          </div>
          <div class="game-message-win" v-if="this.retourapi === 'win'">
            Bravo ! <br />
            Vous avez gagné, relancer une partie pour voir si vous y arriverrais
            encore
          </div>
          <div
            class="game-message-perdu"
            v-else-if="this.retourapi === 'perdu'"
          >
            Dommage ! <br />
            Vous avez perdu, vous pouvez réessayer en commençant avec un nouveau
            mot
            <br />
            {{ this.solution }}
          </div>
          <div class="grid">
            <table class="center">
              <tbody>
                <tr v-for="(essais, index) in nb_essais" :key="index">
                  <td
                    class="center letters"
                    v-for="lettre in essais"
                    :key="lettre"
                    v-bind:class="lettre.class"
                  >
                    <span v-if="lettre.status === 1">
                      <audio autoplay>
                        <source src="../../public/Audio/Burp.mp3" />
                      </audio>
                      {{ lettre.lettre }}
                    </span>
                    <span v-else-if="lettre.status === 2">
                      <audio autoplay>
                        <source src="../../public/Audio/Pet.mp3" />
                      </audio>
                      {{ lettre.lettre }}
                    </span>
                    <span v-else-if="lettre.status === 0">
                      <audio autoplay>
                        <source src="../../public/Audio/Blah.mp3" />
                      </audio>
                      {{ lettre.lettre }}
                    </span>
                    <span v-else>
                      {{ lettre.lettre }}
                    </span>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      <audio autoplay v-if="this.retourapi === 'win'">
        <source src="../../public/Audio/zizou_masterclass.mp3" />
      </audio>
    </div>
    <ConfigComp
      v-if="this.config.loaded"
      :initial-nb-letter="config.nbLetter"
      :initial-nb-tries="config.nbTries"
      :initial-volume="config.volume"
    />
  </div>
</template>

<script>
import NavBar from "@/components/NavBar";
import ConfigComp from "@/components/ConfigComp";
import { mapGetters } from "vuex";
import { postRequest } from "@/js/requests/postRequest";
import { getRequest } from "@/js/requests/getRequest";

export default {
  components: {
    NavBar,
    ConfigComp,
  },
  computed: {
    ...mapGetters({
      isActive: "isActivePopup",
    }),
  },
  async created() {
    await this.getNewWord();
    await this.getGameConfig();
  },
  mounted() {
    window.addEventListener("keyup", this.onkeyup);
  },
  data() {
    return {
      verification: {
        pasla: false,
        mauvaiseplace: false,
        juste: false,
      },
      config: {
        loaded: false,
      },
      settedUp: false,
      nb_essais: [],
      index: 0,
      ligne: 0,
      alphabet: "abcdefghijklmnopqrstuvwxyz".split(""),
      reponse: [],
      retourapi: null,
      solution: "",
    };
  },
  name: "GrilleWordleTI",
  methods: {
    async getNewWord() {
      await getRequest("/create", "json").then((response) => {
        if (response.data.hasPendingGame) {
          this.setUpOldGame(response.data.pendingGame);
        }
      });
    },
    async getGameConfig() {
      await getRequest("/config", "json").then((response) => {
        this.config.nbLetter = response.data.config.nbLetter;
        this.config.nbTries = response.data.config.nbTries;
        this.config.volume = response.data.config.volume * 100;
        this.config.loaded = true;
        for (let i = this.ligne; i < response.data.config.nbTries; i++) {
          const arr = [];
          for (let j = 0; j < response.data.config.nbLetter; j++) {
            arr.push({ lettre: "", status: "", class: "" });
          }
          this.nb_essais.push(arr);
        }
      });
    },
    async setUpOldGame(gameData) {
      const keys = Object.keys(gameData);
      for (const key of keys) {
        const tempKeys = Object.keys(gameData[key]);
        const tempArr = [];
        for (const tempKey of tempKeys) {
          let className = this.getClassName(gameData[key][tempKey].status);
          tempArr.push({
            lettre: gameData[key][tempKey].letter.toUpperCase(),
            status: gameData[key][tempKey].status,
            class: className,
          });
        }
        this.nb_essais.push(tempArr);
        this.ligne++;
      }
    },
    onkeyup: async function (event) {
      const nbLetter = this.nb_essais[0].length;
      if (this.alphabet.includes(event.key)) {
        if (this.retourapi !== "win" && this.retourapi !== "perdu") {
          if (this.index < nbLetter) {
            this.nb_essais[this.ligne][this.index].lettre = String.fromCharCode(
              event.keyCode
            );
            this.index++;
          }
        }
      } else if (event.key === "Backspace") {
        if (this.index > 0) {
          this.index--;
          this.nb_essais[this.ligne][this.index].lettre = "";
        } else {
          this.nb_essais[this.ligne][this.index].lettre = "";
        }
      } else if (event.key === "Enter") {
        if (this.index === nbLetter) {
          await this.testMethod();
          if (this.retourapi === "existe") {
            await this.setstatuslettre();
            this.ligne++;
            this.index = 0;
          }
        }
      }
    },
    async testMethod() {
      let data = {};
      if (this.$store.getters.loggedIn) {
        data = {
          mot: this.nb_essais[this.ligne],
          essai: this.ligne,
        };
      }
      await postRequest(data, "/testTI", "json").then((response) => {
        console.log(response);
        this.retourapi = response.data[1].status;
        this.reponse = response.data[0];
        this.solution = response.data[2].message;
      });
    },
    async setstatuslettre() {
      let nbLetter = this.nb_essais[this.ligne].length;
      for (let i = 0; i < nbLetter; i++) {
        let className = this.getClassName(parseInt(this.reponse[i]));
        this.nb_essais[this.ligne][i].status = parseInt(this.reponse[i]);
        this.nb_essais[this.ligne][i].class = className;
        console.log(this.reponse[i]);
        await this.sleep(400);
      }
    },
    sleep(ms) {
      return new Promise((resolve) => {
        setTimeout(resolve, ms);
      });
    },
    getClassName(status) {
      let className = "";
      switch (status) {
        case 0:
          className = "pasla";
          break;
        case 1:
          className = "malplace";
          break;
        case 2:
          className = "juste";
          break;
        default:
          break;
      }
      return className;
    },
  },
};
</script>

<style lang="scss"></style>
