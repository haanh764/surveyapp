import {
  USER_SIGNUP_URL,
  USER_LOGIN_URL,
  USER_LOGOUT_URL,
  USER_NOT_ACTIVATED_URL,
  USER_CHANGE_PASSWORD_URL,
  USER_DELETE_ACCOUNT_URL
} from "@/api/urls";
import {
  mockUserSignup,
  mockUserLogin,
  mockUserNotActivated
} from "@/mocks/server/api";
import { createServer, Model } from "miragejs";

const customizeUrl = (url) => {
  return `${VUE_APP_API_BASE_URL}${url}`;
};

export function makeServer({ environment = "development" } = {}) {
  let server = createServer({
    environment,

    models: {
      user: Model,
      survey: Model
    },

    seeds(server) {
      server.create("user", {
        id: 0,
        email: "test@test.com",
        isActivated: false,
        isBlocked: false
      });
    },
    namespace: "api",
    routes() {
      this.post(customizeUrl(USER_SIGNUP_URL), (schema, request) => {
        return mockUserSignup(request);
      });

      this.post(customizeUrl(USER_LOGIN_URL), (schema, request) => {
        return mockUserLogin(request);
      });

      this.post(customizeUrl(USER_LOGOUT_URL), () => {
        return {
          message: "User is logged out"
        };
      });

      this.delete(customizeUrl(USER_DELETE_ACCOUNT_URL), () => {
        return {
          message: "User is deleted"
        };
      });

      this.get(customizeUrl(USER_NOT_ACTIVATED_URL), (schema, request) => {
        return mockUserNotActivated(request);
      });

      this.post(customizeUrl(USER_CHANGE_PASSWORD_URL), () => {
        return {
          message: "Password is changed"
        };
      });
    }
  });

  return server;
}
