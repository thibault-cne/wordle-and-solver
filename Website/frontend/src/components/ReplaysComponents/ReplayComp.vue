<!--
          @mouseover="isToggled ^= true"
          @mouseleave="isToggled ^= true"
          -->

<template>
  <div>
    <div class="row">
      <div class="col-6 col-s-6 center">
        <div class="replays-btn center-txt" v-on:click="isToggled ^= true">
          Le mot à deviner était : {{ neededWord }}
        </div>
      </div>
    </div>
    <div class="grid replays-grid" v-bind:class="{ active: isToggled }">
      <table class="center">
        <tbody v-if:="extended">
          <tr v-for="(tries, index) in extendedReplay" v-bind:key="index">
            <ReplayTryComp :tries="tries" />
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import ReplayTryComp from "@/components/ReplaysComponents/ReplayTryComp";

export default {
  name: "ReplayComp",
  components: { ReplayTryComp },
  props: {
    replay: Object,
    maxTries: Number,
    neededWord: String,
  },
  data() {
    return {
      extendedReplay: [],
      extended: false,
      isToggled: false,
    };
  },
  created() {
    const nbLetter = Object.keys(this.replay[1]).length;
    for (let i = 1; i <= this.maxTries; i++) {
      if (this.replay[i] === undefined) {
        let temp = {};
        for (let j = 0; j < nbLetter; j++) {
          temp[j] = {
            letter: "",
            status: 0,
          };
        }
        this.extendedReplay.push(temp);
      } else {
        this.extendedReplay.push(this.replay[i]);
      }
    }
    this.extended = true;
  },
};
</script>

<style scoped></style>
