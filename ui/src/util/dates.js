import moment from "moment";

export const convertToStandardDate = function (value) {
  return moment(value, "DD/MM/YYYY hh:mm:ss").format("DD MMM YYYY");
};
