import moment from "moment";

const pythonDefaultDateFormat = "YYYY-MM-DD hh:mm:ss.SSSSSS+00:00";

export const convertToStandardDate = function (
  value,
  givenFormat = pythonDefaultDateFormat
) {
  return moment(value, givenFormat).format("DD MMM YYYY");
};

export const isTodayBeforeGivenDate = function (
  givenDate,
  givenDateFormat = pythonDefaultDateFormat
) {
  return moment().isBefore(moment(givenDate, givenDateFormat));
};
