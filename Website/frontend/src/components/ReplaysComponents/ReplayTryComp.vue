<template>
  <td
    v-for="(letter, index) in tries"
    v-bind:key="index"
    v-bind:class="getClassName(letter.status)"
  >
    {{ letter.letter.toUpperCase() }}
  </td>
</template>

<script>
export default {
  name: "ReplayTryComp",
  props: {
    tries: Object,
  },
  created() {},
  methods: {
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

<style scoped></style>
