<template>
  <TFSLanguagesTabs
    :languages-tabs="languagesTabs"
    :selected-language="selectedLanguage"
    @change-language="changeLanguage"
  />

  <BaseSpinner v-if="translationLoading" class="spinner" />
  <div v-else :class="[isArabicLanguage && 'arabic-language']">
    <div class="post-title">
      {{ title }}
    </div>
    <div class="post-description">
      {{ description }}
    </div>
  </div>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'

import BaseSpinner from '@components/BaseSpinner'
import TFSLanguagesTabs from '@components/twenty-four-seven/TFSLanguagesTabs'

const {mapState, mapActions} = createNamespacedHelpers('twentyFourSeven')

const LANGUAGES_NAMES = {
  ORIGINAL: 'Original',
  ENGLISH: 'English',
  ARABIC: 'Arabic',
}

export default {
  name: 'TFSOriginalContentTab',
  components: {BaseSpinner, TFSLanguagesTabs},
  emits: [
    'save-summary',
    'send-to-whatsapp',
    'change-original-content-language',
  ],
  props: {
    post: {type: Object, required: true},
    buttonWhatsappLoading: {type: Boolean, required: true},
    translationLoading: {type: Boolean, required: true},
    phoneNumbers: {type: Array, default: () => []},
  },
  data() {
    return {
      selectedLanguage: LANGUAGES_NAMES.ORIGINAL,
    }
  },
  computed: {
    ...mapState(['textTranslation']),
    title() {
      return this.textTranslation?.title || this.post.post.entry_title
    },
    description() {
      return (
        this.textTranslation?.text ||
        this.post.post.full_text ||
        'Original content is available via link in post!'
      )
    },
    isArabicLanguage() {
      if (
        this.post.post.feed_language__language === LANGUAGES_NAMES.ARABIC &&
        this.selectedLanguage !== LANGUAGES_NAMES.ENGLISH
      )
        return true
      return this.selectedLanguage === LANGUAGES_NAMES.ARABIC
    },
  },
  created() {
    this.languagesTabs = Object.values(LANGUAGES_NAMES)
  },
  methods: {
    ...mapActions([action.CLEAR_TFS_TRANSLATED_TEXT]),
    changeLanguage(newLanguage) {
      this.selectedLanguage = newLanguage
      if (newLanguage === LANGUAGES_NAMES.ORIGINAL)
        return this[action.CLEAR_TFS_TRANSLATED_TEXT]()
      this.$emit(
        'change-original-content-language',
        newLanguage,
        this.title,
        this.description
      )
    },
  },
}
</script>

<style lang="scss" scoped>
.languages-tabs {
  display: flex;
  justify-content: flex-end;

  margin-bottom: 20px;

  font-weight: 500;
  font-size: 14px;

  .language {
    margin: 0 10px;

    cursor: pointer;

    &:nth-child(2) {
      position: relative;

      &::before {
        position: absolute;
        right: -10px;

        content: '';

        height: 100%;
        width: 1px;

        background-color: var(--border-color);
      }

      &::after {
        position: absolute;
        left: -10px;

        content: '';

        height: 100%;
        width: 1px;

        background-color: var(--border-color);
      }
    }
  }

  .active-language {
    border-bottom: 1px solid var(--border-active-color);

    color: var(--primary-color);
  }
}

.post-title {
  margin: 0 0 16px;

  font-weight: 600;
  font-size: 20px;
  line-height: 28px;
  color: var(--typography-title-color);
}

.post-description {
  font-weight: 400;
  font-size: 14px;
  color: var(--typography-primary-color);
}

.spinner {
  margin: 20px auto;
}

.arabic-language {
  display: flex;
  flex-direction: column;
  align-items: flex-end;

  text-align: end;
}
</style>
