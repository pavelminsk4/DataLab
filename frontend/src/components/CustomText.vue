<template>
  <BaseButtonSpinner v-if="!translatedText" />
  <component v-else :is="tag">
    <slot name="before"></slot>
    {{ translatedText }}
    <slot></slot>
  </component>
</template>

<script>
import {action, get} from '@store/constants'
import {mapGetters, mapActions} from 'vuex'

import BaseButtonSpinner from '@/components/BaseButtonSpinner'

const ENGLISH = 'en'

export default {
  name: 'CustomText',
  components: {BaseButtonSpinner},
  props: {
    tag: {type: String, default: 'div'},
    text: {type: [String, Number], default: ''},
  },
  computed: {
    ...mapGetters({
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
