import { getAPI } from "@/axios-api";
import { refreshToken } from "@/js/requests/refreshRequests";
import { createHeader } from "@/js/requests/createHeader";

function getRequest(url, requestType) {
  let header = createHeader(requestType);
  return new Promise((resolve, reject) => {
    getAPI
      .get(url, { headers: header })
      .then((response) => {
        resolve(response);
      })
      .catch((error) => {
        if (error.response) {
          if (error.response.status === 401) {
            refreshToken();
          }
        }
        reject(error);
      });
  });
}

export { getRequest };
