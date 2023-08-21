import {mapGetters, mapActions} from 'vuex'
import {get, action} from '@store/constants'
import {LANGUAGES} from '@lib/constants'

const {ENGLISH, ARABIC} = LANGUAGES

export default {
  computed: {
    ...mapGetters({
      platformLanguage: get.PLATFORM_LANGUAGE,
      translated: get.TRANSLATION,
    }),
    currentDir() {
      return this.platformLanguage === ARABIC ? 'rtl' : this.dir
    },
    currentPlaceholder() {
      if (this.platformLanguage === ENGLISH) return this.placeholder
      this[action.GET_TRANSLATED_TEXT](this.placeholder)
      return this.translated[this.placeholder]
    },
  },
  methods: {
    ...mapActions([action.GET_TRANSLATED_TEXT]),
  },
}
