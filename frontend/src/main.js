import {createApp} from 'vue'
import router from '@router'
import store from '@store'
import App from './App.vue'

const app = createApp(App)
app.use(router)
app.use(store)

app.mixin({
  methods: {
    togglePageScroll(isOpen) {
      if (isOpen) {
        document.body.classList.add('overflow-hidden')
      } else {
        document.body.classList.remove('overflow-hidden')
      }
    },

    t(text) {
      store.dispatch('t', text)
    },
  },
})

app.mount('#app')
