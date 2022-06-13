<template>
  <div class="under-popup-content">
    <NavBar />
    <div class="row">
      <div class="col-6 col-s-6 center">
        <h3 class="center-txt">Leader Board</h3>
      </div>
    </div>
    <div class="row">
      <div class="col-6 col-s-6 center">
        <div class="grid-leader">
          <div v-for="(lead, index) in leads" v-bind:key="index">
            <div class="top">
              <span class="float-left"> Rank : {{ index + 1 }} </span>
              <br />
              {{ lead[0] }}
              <br />
              <span class="align-right">Score : {{ lead[1] }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getRequest } from "@/js/requests/getRequest";
import NavBar from "@/components/NavBar";

export default {
  name: "LeaderBoard",
  components: {
    NavBar,
  },
  data() {
    return {
      leads: undefined,
    };
  },
  created() {
    this.getLeaderboard();
  },
  methods: {
    async getLeaderboard() {
      await getRequest("/leaderboard", "json").then((response) => {
        this.leads = response.data;
      });
    },
  },
};
</script>

<style lang="scss"></style>
