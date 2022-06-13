/*
 * Copyright (c)
 * Project : project2-E19
 *
 * --
 *
 * Author : thibault
 * File : axios-api.js
 * Description : *Enter description here*
 *
 * --
 *
 * Last modification : 2022/4/5
 */

import axios from "axios";

const getAPI = axios.create({
  baseURL: "http://127.0.0.1:5454",
});

export { getAPI };
