<template>
  <component :is="tag">
    <slot name="before"></slot>
    {{ translatedText }}
    <slot></slot>
  </component>
</template>

<script>
import {action, get} from '@store/constants'
import {mapGetters, mapActions} from 'vuex'

export default {
  name: 'CustomText',
  props: {
    tag: {type: String, default: 'div'},
    text: {type: String, default: ''},
  },
  computed: {
    ...mapGetters({
      translated: get.TRANSLATION,
      platformLanguage: get.PLATFORM_LANGUAGE,
    }),
    translatedText() {
      if (this.platformLanguage === 'en') return this.text

      this[action.GET_TRANSLATED_TEXT](this.text)
      return this.translated[this.text]
    },
  },
  methods: {
    ...mapActions([action.GET_TRANSLATED_TEXT]),
  },
}
</script>
