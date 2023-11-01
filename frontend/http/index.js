import axios from 'axios'
import router from '@router'
import CSRF_TOKEN from '../csrf_token'
import store from '@store'
import {action} from '@store/constants'

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

$api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response.status === 500) {
      router.push('/not-found')
    }

    store.dispatch(action.OPEN_FLASH_MESSAGE, {
      message: error.message,
      title: 'Server Error',
      type: 'Error',
    })
    return Promise.reject(error)
  }
)

export default $api
