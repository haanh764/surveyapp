import { Response } from "miragejs";
import loginInfo from "~/tests/e2e/support/data/login-info";

/*
  Created to mock multiple api conditions. 
*/

const { mockEmails } = loginInfo;

const getRequestBody = function (request) {
  return JSON.parse(request.requestBody);
};

export const mockUserSignup = (request) => {
  let requestBody = getRequestBody(request);
  let message = new Response(200, {}, { message: "Success." });
  if (requestBody.email == mockEmails.error400) {
    message = new Response(400, { errors: ["some errors occured"] });
  } else if (requestBody.email == mockEmails.success201) {
    message = new Response(201, {}, { message: "User already exists." });
  }
  return message;
};

export const mockUserLogin = (request) => {
  let requestBody = getRequestBody(request);
  let message = new Response(200, {}, { message: "User is activated." });
  if (requestBody.email == mockEmails.error400) {
    message = new Response(400, { errors: ["some errors occured"] });
  } else if (requestBody.email == mockEmails.success201) {
    message = new Response(201, {}, { message: "User is not activated." });
  }
  return message;
};
