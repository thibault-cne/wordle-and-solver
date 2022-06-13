/*
 * Copyright (c)
 * Project : project2-E19
 *
 * --
 *
 * Author : thibault
 * File : index.js
 * Description : *Enter description here*
 *
 * --
 *
 * Last modification : 2022/4/11
 */

import { createStore } from "vuex";
import { getAPI } from "@/axios-api";
import createPersistedState from "vuex-persistedstate";

const store = createStore({
  state: {
    accessToken: null,
    refreshToken: null,
    cipherWord: null,
    isPopupActive: false,
    noConfig: false,
  },
  mutations: {
    setWord(state, word) {
      state.cipherWord = word;
    },
    destroyWord(state) {
      state.cipherWord = null;
    },
    updateStorage(state, { access, refresh }) {
      state.accessToken = access;
      state.refreshToken = refresh;
    },
    destroyToken(state) {
      state.accessToken = null;
      state.refreshToken = null;
    },
    togglePopup(state) {
      state.isPopupActive ^= true;
    },
    setNoConfigTrue(state) {
      state.noConfig = true;
    },
    setNoConfigFalse(state) {
      state.noConfig = false;
    },
    setAccessToken(state, token) {
      state.accessToken = token;
    },
  },
  getters: {
    word: (state) => state.cipherWord,
    loggedIn: (state) => state.accessToken != null,
    accessToken: (state) => state.accessToken,
    refreshToken: (state) => state.refreshToken,
    isActivePopup: (state) => state.isPopupActive,
    noConfig: (state) => state.noConfig,
  },
  actions: {
    userLogout(context) {
      if (context.getters.loggedIn) {
        context.commit("destroyToken");
      }
    },
    userLogin(context, userCredentials) {
      return new Promise((resolve, reject) => {
        getAPI
          .post("/auth-api/login", {
            username: userCredentials.username,
            password: userCredentials.password,
          })
          .then((response) => {
            if (response.data.status == "success") {
              context.commit("updateStorage", {
                access: response.data.access,
                refresh: response.data.refresh,
              });
            }
            resolve(response.data.status);
          })
          .catch((err) => {
            reject(err);
          });
      });
    },
    setNoConfig(state, statement) {
      state.noConfig = statement;
    },
  },
  plugins: [createPersistedState()],
});

export { store };
