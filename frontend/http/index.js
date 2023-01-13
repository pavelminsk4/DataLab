import axios from 'axios'
import CSRF_TOKEN from '../csrf_token'

const $api = axios.create({
  withCredentials: true,
})

$api.interceptors.request.use((config) => {
  config.headers = {
    'content-type': 'application/json',
    'X-CSRFToken': CSRF_TOKEN,
  }
  return config
})

export default $api
