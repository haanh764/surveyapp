import {
  USER_SIGNUP_URL,
  USER_LOGIN_URL,
  USER_LOGOUT_URL,
  USER_NOT_ACTIVATED_URL,
  USER_CHANGE_PASSWORD_URL,
  USER_DELETE_ACCOUNT_URL,
} from "@/api/urls";
import { mockUserSignup, mockUserLogin } from "@/mocks/server/api";
import { createServer, Model } from "miragejs";

const customizeUrl = (url) => {
  return `${VUE_APP_API_BASE_URL}${url}`;
};

let otherDomains = [];
let methods = ["get", "put", "patch", "post", "delete"];

export function makeServer({ environment = "development" } = {}) {
  let server = createServer({
    environment,

    models: {
      user: Model,
      survey: Model,
    },

    seeds(server) {
      server.create("user", {
        id: 0,
        email: "test@test.com",
        isActivated: false,
        isBlocked: false,
      });
    },

    routes() {
      for (const domain of ["/", ...otherDomains]) {
        for (const method of methods) {
          this[method](`${domain}*`, async (schema, request) => {
            let [status, headers, body] = await window.handleFromCypress(
              request
            );
            return new Response(status, headers, body);
          });
        }
      }

      this.post(customizeUrl(USER_SIGNUP_URL), (schema, request) => {
        return mockUserSignup(request);
      });

      this.post(customizeUrl(USER_LOGIN_URL), (schema, request) => {
        return mockUserLogin(request);
      });

      this.post(customizeUrl(USER_LOGOUT_URL), () => {
        return {
          message: "User is logged out",
        };
      });

      this.delete(customizeUrl(USER_DELETE_ACCOUNT_URL), () => {
        return {
          message: "User is deleted",
        };
      });

      this.get(customizeUrl(USER_NOT_ACTIVATED_URL), () => {
        return {
          message: "User is activated",
        };
      });

      this.post(customizeUrl(USER_CHANGE_PASSWORD_URL), () => {
        return {
          message: "Password is changed",
        };
      });
    },
  });

  return server;
}
