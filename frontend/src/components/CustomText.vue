<template>
  <component :is="tag" :class="[`custom-text-${this.platformLanguage}`]">
    <slot name="before"></slot>
    {{ translatedText }}
    <slot></slot>
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
      platformLanguage: get.PLATFORM_LANGUAGE,
    }),
    translatedText() {
      if (this.platformLanguage === ENGLISH) return this.text

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
