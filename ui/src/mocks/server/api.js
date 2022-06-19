import { Response } from "miragejs";
import loginInfo from "~/tests/e2e/support/data/login-info";

/*
  Created to mock multiple api conditions. 
*/

const { mockEmails } = loginInfo;

const getRequestProperty = function (request, property) {
  return JSON.parse(request[property]);
};

export const mockUserSignup = (request) => {
  let requestBody = getRequestProperty(request, "requestBody");
  let message = new Response(200, {}, { message: "Success." });
  if (requestBody.email == mockEmails.error400) {
    message = new Response(400, { errors: [ "some errors occured" ] });
  } else if (requestBody.email == mockEmails.success201) {
    message = new Response(201, {}, { message: "User already exists." });
  }
  return message;
};

export const mockUserLogin = (request) => {
  let requestBody = getRequestProperty(request, "requestBody");
  let message = new Response(
    200,
    {},
    { message: "Access token is 1234567890" }
  );
  if (requestBody.email == mockEmails.error400) {
    message = new Response(400, { errors: [ "some errors occured" ] });
  }
  return message;
};

export const mockUserNotActivated = () => {
  let message = new Response(200, {}, { message: "User is activated" });
  return message;
};
