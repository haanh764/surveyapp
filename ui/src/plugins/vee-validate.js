import Vue from "vue";
import { ValidationProvider, ValidationObserver, extend } from "vee-validate";
import { email, alpha, min, max } from "vee-validate/dist/rules";

extend("email", email);
extend("alpha", alpha);
extend("min", min);
extend("max", {
  ...max,
  message: "Maximum number of characters has been reached."
});

extend("required", {
  validate(value) {
    return {
      required: true,
      valid: [ "", null, undefined ].indexOf(value) === -1
    };
  },
  computesRequired: true,
  message: "This field is required"
});

Vue.component("ValidationProvider", ValidationProvider);
Vue.component("ValidationObserver", ValidationObserver);
