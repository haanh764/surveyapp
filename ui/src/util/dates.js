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

export const getDurationFromTodayToGivenDate = function (
  givenDate,
  givenDateFormat = pythonDefaultDateFormat
) {
  let now = moment(new Date()); //todays date
  let duration = moment.duration(moment(givenDate, givenDateFormat).diff(now));
  return {
    duration,
    minutes: duration.asMinutes(),
    hours: duration.asHours(),
    days: duration.asDays(),
    months: duration.asMonths()
  };
};
