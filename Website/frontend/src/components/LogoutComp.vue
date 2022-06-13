<!--
  - Copyright (c)
  - Project : project2-E19
  -
  - -
  -
  - Author : thibault
  - File : LogoutComp.vue
  - Description : *Enter description here*
  -
  - -
  -
  - Last modification : 2022/4/7
  -->

<template>
  <div style="display: none">This is logout comp</div>
</template>

<script>
export default {
  name: "LogoutComp",
  mounted() {
    this.$store.dispatch("userLogout");
    this.$router.push({ name: "LoginPage" });
  },
};
</script>

<style lang="scss"></style>
