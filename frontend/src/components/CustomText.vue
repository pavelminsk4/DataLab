<template>
  <component :is="tag" :class="[`custom-text-${platformLanguage}`]">
    {{ translatedText }}
  </component>
</template>

<script>
import {action, get} from '@store/constants'
import {mapGetters, mapActions} from 'vuex'

const ENGLISH = 'en'

export default {
  name: 'CustomText',
  props: {
    tag: {type: String, default: 'div'},
    text: {type: [String, Number], default: ''},
  },
  computed: {
    ...mapGetters({
      loading: get.LOADING,
      translated: get.TRANSLATION,
    }),
    translatedText() {
      if (this.platformLanguage === ENGLISH) return this.text

      if (this.translated[this.text]) return this.translated[this.text]

      this[action.GET_TRANSLATED_TEXT](this.text)
      return this.translated[this.text]
    },
  },
  methods: {
    ...mapActions([action.GET_TRANSLATED_TEXT]),
  },
}
</script>

<style>
.custom-text-ar {
  text-align: end;
}
</style>
