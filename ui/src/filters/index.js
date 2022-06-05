import Vue from "vue";
import { convertToStandardDate } from "@util/dates.js";

Vue.filter("capitalize", function (value) {
  if (!value) return "";
  value = value.toString();
  return value.charAt(0).toUpperCase() + value.slice(1);
});

Vue.filter("standardDate", convertToStandardDate);
