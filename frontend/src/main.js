import {createApp} from 'vue'
import {mapGetters} from 'vuex'
import {get} from '@store/constants'
import router from '@router'
import store from '@store'
import App from './App.vue'

const app = createApp(App)
app.use(router)
app.use(store)

app.mixin({
  computed: {
    ...mapGetters({platformLanguage: get.PLATFORM_LANGUAGE}),
  },
  methods: {
    goToNotFoundPage() {
      this.$router.push({
        name: 'NotFound',
      })
    },
    togglePageScroll(isOpen) {
      if (isOpen) {
        document.body.classList.add('overflow-hidden')
      } else {
        document.body.classList.remove('overflow-hidden')
      }
    },
  },
})

app.mount('#app')
