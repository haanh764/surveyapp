import Vue from "vue";
import Router from "vue-router";
import { trailingSlash } from "@/util/helpers";
import { layout } from "@/util/routes";
import PageNotFoundView from "@views/PageNotFoundView.vue";
import store from "@store/index.js";
import Cookies from "js-cookie";
import { userLogout, adminLogout } from "@api";

Vue.use(Router);

const userRoutes = [
  layout("Default", [
    {
      path: "/user/surveys",
      name: "user-surveys",
      component: () =>
        import(
          /* webpackChunkName: "user-surveys" */ "@views/user/surveys/SurveysView.vue"
        )
    },
    {
      path: "/user/surveys/:id/edit",
      name: "user-survey-edit",
      component: () =>
        import(
          /* webpackChunkName: "user-survey-edit" */ "@views/user/survey-edit/SurveyEditView.vue"
        )
    },
    {
      path: "/user/surveys/:id/",
      name: "user-survey-detail",
      component: () =>
        import(
          /* webpackChunkName: "user-survey-detail" */ "@views/user/survey-detail/SurveyDetailView.vue"
        )
    },
    {
      path: "/user/settings",
      name: "user-settings",
      component: () =>
        import(
          /* webpackChunkName: "user-settings" */ "@views/user/settings/SettingsView.vue"
        )
    },
    {
      path: "/user/confirm",
      name: "user-confirm",
      component: () =>
        import(
          /* webpackChunkName: "user-confirm" */ "@views/user/login-confirm/LoginConfirmView.vue"
        )
    },
    //user-blocked
    {
      path: "/user/blocked",
      name: "user-blocked",
      component: () =>
        import(
          /* webpackChunkName: "user-blocked" */ "@views/user/login-blocked/LoginBlockedView.vue"
        )
    }
  ])
];

const adminRoutes = [
  layout("Default", [
    {
      path: "/admin/surveys",
      name: "admin-surveys",
      component: () =>
        import(
          /* webpackChunkName: "admin-surveys" */ "@views/admin/surveys/SurveysView.vue"
        )
    },
    {
      path: "/admin/users",
      name: "admin-users",
      component: () =>
        import(
          /* webpackChunkName: "admin-users" */ "@views/admin/users/UsersView.vue"
        )
    },
    {
      path: "/admin/settings",
      name: "admin-settings",
      component: () =>
        import(
          /* webpackChunkName: "admin-settings" */ "@views/admin/settings/SettingsView.vue"
        )
    }
  ])
];

const generalRoutes = [
  layout("DefaultWithoutSidebar", [
    {
      path: "/",
      name: "general-landing",
      component: () =>
        import(
          /* webpackChunkName: "general-landing" */ "@views/general/landing/LandingView.vue"
        )
    },
    {
      path: "/privacy-policy",
      name: "general-privacy-policy",
      component: () =>
        import(
          /* webpackChunkName: "general-privacy-policy" */ "@views/general/privacy-policy/PrivacyPolicyView.vue"
        )
    },
    {
      path: "/terms-and-conditions",
      name: "general-terms-and-conditions",
      component: () =>
        import(
          /* webpackChunkName: "general-terms-and-conditions" */ "@views/general/terms-and-conditions/TermsAndConditionsView.vue"
        )
    },
    {
      path: "/user/login",
      meta: { isAccessableAfterLogin: false },
      name: "general-user-login",
      component: () =>
        import(
          /* webpackChunkName: "general-user-login" */ "@views/user/login/LoginView.vue"
        )
    },
    {
      path: "/user/signup",
      name: "general-user-signup",
      component: () =>
        import(
          /* webpackChunkName: "general-user-signup" */ "@views/user/signup/SignupView.vue"
        )
    },
    {
      path: "/admin/login",
      name: "general-admin-login",
      component: () =>
        import(
          /* webpackChunkName: "general-admin-login" */ "@views/admin/login/LoginView.vue"
        )
    },
    {
      path: "/survey/:id",
      name: "general-survey-fill",
      component: () =>
        import(
          /* webpackChunkName: "general-survey-fill" */ "@views/general/survey-fill/SurveyFillView.vue"
        )
    },
    {
      path: "/user/signup/thankyou",
      name: "general-user-signup-thankyou",
      component: () =>
        import(
          /* webpackChunkName: "general-user-signup-thankyou" */ "@views/user/signup-thankyou/SignupThankyouView.vue"
        )
    },
    {
      path: "/user/delete/thankyou",
      name: "general-user-delete-thankyou",
      component: () =>
        import(
          /* webpackChunkName: "general-user-delete-thankyou" */ "@views/user/delete-thankyou/DeleteThankyouView.vue"
        )
    },
    { path: "/logout", name: "general-logout" }
  ])
];

const router = new Router({
  mode: NODE_ENV == "development" ? "history" : "hash",
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
    layout("DefaultWithoutSidebar", [
      { path: "/404", name: "general-404", component: PageNotFoundView },
      { path: "*", redirect: "404" }
    ])
  ]
});

router.beforeEach((to, from, next) => {
  const isBlocked = store.getters["user/isBlocked"];
  const hasLoggedIn = store.getters["user/hasLoggedIn"];
  const accountType = store.getters["user/accountType"];
  const hasBeenActivated = store.getters["user/hasBeenActivated"];
  const hasAcceptedTnC = store.getters["user/hasAcceptedTnC"];
  const hasAcceptedPrivacyPolicy = store.getters["user/hasAcceptedPrivacyPolicy"];
  const hasAcceptedTncAndPp = (hasAcceptedTnC && hasAcceptedPrivacyPolicy);

  const userMainPage = { name: "user-surveys" };
  const adminMainPage = { name: "admin-users" };

  const preventedWords = [ "landing", "login", "signup", "delete" ];
  const shouldBePrevented = (routeName) => {
    return preventedWords.some((preventedWord) =>
      routeName.includes(preventedWord)
    );
  };

  const width = window.innerWidth;
  const isMobile = width <= 768;

  const unsetClientData = () => {
    store.dispatch("user/setUserData", {});
    store.dispatch("user/setToken", "");
    store.dispatch("user/setItems", []);
    Cookies.remove("access_token_cookie");
  };

  if (hasLoggedIn) {
    if (to.name == "general-logout") {
      if (accountType == 0) {
        userLogout()
          .then(() => {
            unsetClientData();
            return next({ name: "general-landing" });
          })
          .catch(() => {
            unsetClientData();
            return next({ name: "general-landing" });
          });
      } else if (accountType == 1) {
        adminLogout()
          .then(() => {
            unsetClientData();
            return next({ name: "general-admin-login" });
          })
          .catch(() => {
            unsetClientData();
            return next({ name: "general-admin-login" });
          });
      }
    } else if (from.name == "user-blocked" && isBlocked) {
      return next({ name: "user-blocked" });
    } else if (from.name == "user-confirm" && !hasBeenActivated) {
      return next({ name: "user-confirm" });
    } else if (from.name == "user-surveys" && !hasAcceptedTncAndPp) {
      return next(userMainPage);
    } else if (shouldBePrevented(to.name)) {
      if (accountType == 0) {
        return next(userMainPage);
      } else if (accountType == 1) {
        return next(adminMainPage);
      }
    } else if (accountType == 0) {
      if (!to.name.startsWith("admin")) {
        if (to.name == "user-survey-edit") {
          !isMobile && store.dispatch("app/setMini", true);
        }
        return next();
      } else {
        return next(userMainPage);
      }
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
