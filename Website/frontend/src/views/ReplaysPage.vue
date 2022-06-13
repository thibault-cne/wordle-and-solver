<template>
  <div class="under-popup-content">
    <NavBar />
    <div class="row">
      <div class="col-6 col-s-6 center">
        <h3 class="center-txt">Historique de vos parties</h3>
      </div>
    </div>
    <div class="grid-wrapper">
      <div v-for="(replay, index) in replays" v-bind:key="index">
        <ReplayComp
          v-if="Object.keys(replay[0]).length > 0"
          :replay="replay[0]"
          :maxTries="replay[2]"
          :needed-word="replay[1]"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { getRequest } from "@/js/requests/getRequest";
import ReplayComp from "@/components/ReplaysComponents/ReplayComp";
import NavBar from "@/components/NavBar";

export default {
  name: "ReplaysPage",
  components: {
    ReplayComp,
    NavBar,
  },

  data() {
    return {
      replays: [],
    };
  },
  created() {
    this.getUsersReplays();
  },
  methods: {
    async getUsersReplays() {
      await getRequest("/profil-api/getReplays", "json").then((response) => {
        this.replays = response.data.replays;
      });
    },
  },
};
</script>

<style scoped></style>
