import Vue from "vue";
import Router from "vue-router";
import { trailingSlash } from "@/util/helpers";
import {
  layout
} from "@/util/routes";
import PageNotFoundView from "@views/PageNotFoundView.vue";
import store from "@store/index.js";

Vue.use(Router);

const userRoutes = [
  layout("Default", [
    { path: "/user/surveys", name: "user-surveys", component: () => import(/* webpackChunkName: "user-surveys" */ "@views/user/surveys/SurveysView.vue") },
    { path: "/user/surveys/:id/edit", name: "user-survey-edit", component: () => import(/* webpackChunkName: "user-survey-edit" */ "@views/user/survey-edit/SurveyEditView.vue") },
    { path: "/user/surveys/:id/", name: "user-survey-detail", component: () => import(/* webpackChunkName: "user-survey-detail" */ "@views/user/survey-detail/SurveyDetailView.vue") },
    { path: "/user/settings", name: "user-settings", component: () => import(/* webpackChunkName: "user-settings" */ "@views/user/settings/SettingsView.vue") }
  ])
];

const adminRoutes = [
  layout("Default", [
    { path: "/admin/surveys", name: "admin-surveys", component: () => import(/* webpackChunkName: "admin-surveys" */ "@views/admin/surveys/SurveysView.vue") },
    { path: "/admin/users", name: "admin-users", component: () => import(/* webpackChunkName: "admin-users" */ "@views/admin/users/UsersView.vue") },
    { path: "/admin/settings", name: "admin-settings", component: () => import(/* webpackChunkName: "admin-settings" */ "@views/admin/settings/SettingsView.vue") }
  ])
];

const generalRoutes = [
  layout("DefaultWithoutSidebar", [
    { path: "/", name: "general-landing", component: () => import(/* webpackChunkName: "general-landing" */ "@views/general/landing/LandingView.vue") },
    { path: "/privacy-policy", name: "general-privacy-policy", component: () => import(/* webpackChunkName: "general-privacy-policy" */ "@views/general/privacy-policy/PrivacyPolicyView.vue") },
    { path: "/terms-and-conditions", name: "general-terms-and-conditions", component: () => import(/* webpackChunkName: "general-terms-and-conditions" */ "@views/general/terms-and-conditions/TermsAndConditionsView.vue") },
    { path: "/user/login", name: "general-user-login", component: () => import(/* webpackChunkName: "general-user-login" */ "@views/user/login/LoginView.vue") },
    { path: "/user/signup", name: "general-user-signup", component: () => import(/* webpackChunkName: "general-user-signup" */ "@views/user/signup/SignupView.vue") },
    { path: "/admin/login", name: "general-admin-login", component: () => import(/* webpackChunkName: "general-admin-login" */ "@views/admin/login/LoginView.vue") },
    { path: "/logout", name: "general-logout" }

  ])
];

const respondentRoutes = [
  layout("DefaultWithoutSidebar", [
    { path: "/respondent/survey/:id", name: "respondent-survey-fill", component: () => import(/* webpackChunkName: "respondent-survey-fill" */ "@views/respondent/survey/SurveyView.vue") }
  ])
];

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
    layout("DefaultWithoutSidebar", [
      { path: "/404", name: "general-404", component: PageNotFoundView },
      { path: "*", redirect: "404" } ])
  ]
});


router.beforeEach((to, from, next) => {

  const hasLoggedIn = store.getters["user/hasLoggedIn"];
  const accountType = store.getters["user/accountType"];

  const userMainPage = { name: "user-surveys" };
  const adminMainPage = { name: "admin-surveys" };


  if (hasLoggedIn) {
    if (to.name == "general-logout") {
      store.dispatch("user/setUserData", {});
      store.dispatch("user/setToken", "");
      return next({ name: "general-landing" });
    } else if (to.name == "general-landing" || to.name.includes("login") || to.name.includes("signup")) {
      if (accountType == 0) {
        return next(userMainPage);
      } else if (accountType == 1) {
        return next(adminMainPage);
      }
    } else if (accountType == 0 && !to.name.startsWith("admin")) {
      return next();
    } else if (accountType == 1 && !to.name.startsWith("user")) {
      return next();
    } else {
      return next({ name: "general-404" });
    }
  } else {
    if (!to.name.startsWith("general")) {
      return next({ name: "general-user-login" });
    }
  }

  return to.path.endsWith("/") ? next() : next(trailingSlash(to.path));

});

export default router;
