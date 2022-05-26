// Imports
import Vue from "vue";
import Router from "vue-router";
import { trailingSlash } from "@/util/helpers";
import {
  layout
} from "@/util/routes";
import PageNotFoundView from "@views/PageNotFoundView.vue";

Vue.use(Router);

const userRoutes = [
  layout("Default", [
    { path: "/user/surveys", name: "user-surveys", component: () => import(/* webpackChunkName: "user-surveys" */ "@views/user/surveys/SurveysView.vue") },
    { path: "/user/settings", name: "user-settings", component: () => import(/* webpackChunkName: "user-surveys" */ "@views/user/settings/SettingsView.vue") },
    { path: "/user/logout", name: "user-logout", redirect: '/' },
  ])
];

const adminRoutes = [];

const generalRoutes = [];

const respondentRoutes = [];

const router = new Router({
  mode: "history",
  base: process.env.BASE_URL,
  scrollBehavior: (to, from, savedPosition) => {
    if (to.hash) return { selector: to.hash };
    if (savedPosition) return savedPosition;

    return { x: 0, y: 0 };
  },
  routes: [
    ...generalRoutes,
    ...userRoutes,
    ...adminRoutes,
    ...respondentRoutes,
    { path: "/404", name: "general-page-not-found", component: PageNotFoundView },
    { path: "*", redirect: "404" }
  ]
});

router.beforeEach((to, from, next) => {
  return to.path.endsWith("/") ? next() : next(trailingSlash(to.path));
});

export default router;
