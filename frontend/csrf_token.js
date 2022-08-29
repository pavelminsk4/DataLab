import Cookies from "js-cookie"
let CSRF_TOKEN = Cookies.get("csrftoken");
export default CSRF_TOKEN;
