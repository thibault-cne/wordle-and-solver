import { createRouter, createWebHistory } from "vue-router";

// Import views
import RegisterPage from "@/views/RegisterPage";
import LoginPage from "@/views/LoginPage";
import HomePage from "@/views/HomePage";
import GrilleWordle from "@/views/GrilleWordle";
import LogoutComp from "@/components/LogoutComp";
import GrilleWordleTI from "@/views/GrilleWordleTI";
import DailyWordle from "@/views/DailyWordle";
import ProfilPage from "@/views/ProfilPage";
import ReplaysPage from "@/views/ReplaysPage";
import LeaderBoard from "@/views/LeaderBoard";

const routes = [
  {
    path: "/",
    name: "HomePage",
    component: HomePage,
    meta: {
      title: "TazMou - Page d'acceuil",
    },
  },
  {
    path: "/login",
    name: "LoginPage",
    component: LoginPage,
    meta: {
      title: "TazMou - Login",
    },
  },
  {
    path: "/register",
    name: "RegisterPage",
    component: RegisterPage,
    meta: {
      title: "TazMou - Register",
    },
  },
  {
    path: "/logout",
    name: "LogoutComp",
    component: LogoutComp,
  },
  {
    path: "/grille",
    name: "GrillePage",
    component: GrilleWordle,
    meta: {
      title: "TazMou - le jeu original",
    },
  },
  {
    path: "/grilleTI",
    name: "GrilleWordleTI",
    component: GrilleWordleTI,
  },
  {
    path: "/dailyWord",
    name: "DailyWord",
    component: DailyWordle,
  },
  {
    path: "/profil",
    name: "ProfilPage",
    component: ProfilPage,
    meta: {
      title: "TazMou - Profil",
    },
  },
  {
    path: "/replays",
    name: "ReplaysPage",
    component: ReplaysPage,
    meta: {
      title: "TazMou - Page des replays",
    },
  },
  {
    path: "/leaderboard",
    name: "LeaderBoard",
    component: LeaderBoard,
    meta: {
      title: "TazMou - Page du LeaderBoard",
    },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// This callback runs before every route change, including on page load.
router.beforeEach((to, from, next) => {
  // This goes through the matched routes from last to first, finding the closest route with a title.
  // e.g., if we have `/some/deep/nested/route` and `/some`, `/deep`, and `/nested` have titles,
  // `/nested`'s will be chosen.
  const nearestWithTitle = to.matched
    .slice()
    .reverse()
    .find((r) => r.meta && r.meta.title);

  // If a route with a title was found, set the document (page) title to that value.
  if (nearestWithTitle) {
    document.title = nearestWithTitle.meta.title;
  }
  next();
});

// ...

export default router;
