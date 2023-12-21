<template>
  <div class="summary-wrapper">
    <TFSLanguagesTabs
      :languages-tabs="languagesTabs"
      :selected-language="selectedLanguage"
      @change-language="changeLanguage"
    />
    <BaseSpinner v-if="loadingTranslation" class="spinner" />

    <div v-else>
      <BaseInput
        v-model="header"
        :custom-dir="summaryLanguage"
        label="Header"
        placeholder="Enter the header"
        class="header"
      />
      <BaseTextarea
        v-model="text"
        label="Text"
        placeholder="Enter the text"
        error-message="Clear the field to create AI summary!"
        :custom-dir="summaryLanguage"
        :has-error="!isFieldClear"
        :class="[!isFieldClear && 'summary-error']"
      />
    </div>

    <div class="buttons">
      <BaseButton
        v-if="isSummaryTab"
        :is-not-background="true"
        :button-loading="buttonAISummaryLoading"
        @click="createAISummary"
      >
        <CustomText text="AI Summary" />
      </BaseButton>
      <BaseButton
        :button-loading="buttonSaveLoading"
        @click="
          $emit('save-summary', newHeader, newHeaderAr, newText, newTextAr)
        "
      >
        <SaveIcon color="#ffffff" />
        <CustomText text="Save" />
      </BaseButton>
    </div>
  </div>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'

import CustomText from '@components/CustomText'
import BaseButton from '@components/common/BaseButton'
import BaseInput from '@components/common/BaseInput'
import BaseTextarea from '@components/common/BaseTextarea'
import SaveIcon from '@components/icons/SaveIcon'
import BaseSpinner from '@components/BaseSpinner'
import TFSLanguagesTabs from '@components/twenty-four-seven/TFSLanguagesTabs'

const {mapState, mapActions} = createNamespacedHelpers('twentyFourSeven')

const TABS = {
  ORIGINAL_CONTENT: 'Original content',
  SUMMARY: 'Summary',
}

const LANGUAGES_NAMES = {
  ENGLISH: 'English',
  ARABIC: 'Arabic',
}

export default {
  name: 'TFSSummaryTab',
  components: {
    BaseInput,
    BaseTextarea,
    BaseButton,
    SaveIcon,
    TFSLanguagesTabs,
    BaseSpinner,
    CustomText,
  },
  emits: ['save-summary', 'create-ai-summary'],
  props: {
    post: {type: Object, required: true},
    currentTab: {type: String, required: true},
    buttonAISummaryLoading: {type: Boolean, required: true},
    buttonSaveLoading: {type: Boolean, required: true},
  },
  data() {
    return {
      newHeader: null,
      newHeaderAr: null,
      newText: null,
      newTextAr: null,
      isFieldClear: true,
      loadingTranslation: false,
      newSelectedLanguage: this.post.post.feed_language__language,
    }
  },
  computed: {
    ...mapState(['aiSummary', 'translatedText']),
    selectedLanguage: {
      get() {
        if (this.newSelectedLanguage !== LANGUAGES_NAMES.ARABIC)
          return LANGUAGES_NAMES.ENGLISH
        return this.newSelectedLanguage
      },
      set(newLang) {
        this.newSelectedLanguage = newLang
      },
    },
    header: {
      get() {
        if (this.newHeader === '') return this.newHeader
        const header =
          this.selectedLanguage === LANGUAGES_NAMES.ARABIC
            ? this.post.header_ar
            : this.post.header

        const currentHeader =
          this.selectedLanguage === LANGUAGES_NAMES.ARABIC
            ? this.newHeaderAr
            : this.newHeader
        return currentHeader || header || this.post.post.entry_title
      },
      set(value) {
        this.newHeader = value
      },
    },
    text: {
      get() {
        if (this.newText === '') return this.newText
        const text =
          this.selectedLanguage === LANGUAGES_NAMES.ARABIC
            ? this.post.text_ar
            : this.post.text

        const currentText =
          this.selectedLanguage === LANGUAGES_NAMES.ARABIC
            ? this.newTextAr
            : this.newText
        return currentText || text || this.post.post.full_text
      },
      set(value) {
        this.newText = value
      },
    },
    isSummaryTab() {
      return this.currentTab === TABS.SUMMARY
    },
    summaryLanguage() {
      return this.selectedLanguage === LANGUAGES_NAMES.ARABIC ? 'rtl' : 'ltr'
    },
  },
  created() {
    this.languagesTabs = Object.values(LANGUAGES_NAMES)
  },
  methods: {
    ...mapActions([action.CLEAR_TFS_AI_SUMMARY, action.CHANGE_HEADER_LANGUAGE]),
    async changeLanguage(newLanguage) {
      this.loadingTranslation = true
      this.selectedLanguage = newLanguage

      try {
        if (
          this.selectedLanguage === LANGUAGES_NAMES.ARABIC &&
          !this.newHeaderAr
        ) {
          await this[action.CHANGE_HEADER_LANGUAGE]({
            newLanguage: newLanguage.toLowerCase(),
            header: this.header || '',
          })

          this.newHeaderAr = this.translatedText.header
        }
      } finally {
        this.loadingTranslation = false
      }
    },
    createAISummary() {
      if (this.text) return (this.isFieldClear = false)

      this.isFieldClear = true
      this[action.CLEAR_TFS_AI_SUMMARY]()
      this.$emit('create-ai-summary')
    },
  },
  watch: {
    aiSummary() {
      this.newText = this.aiSummary.summary
      this.newTextAr = this.aiSummary.summary_ar
    },
  },
}
</script>

<style lang="scss" scoped>
.summary-wrapper {
  display: flex;
  flex-direction: column;

  .spinner {
    display: flex;
    align-self: center;
  }
  .header {
    margin-bottom: 32px;
  }

  .buttons {
    display: flex;
    justify-content: flex-end;
    gap: 16px;

    margin: 36px -24px 0;
    padding: 18px 24px 0 0;

    border-top: 1px solid var(--border-color);
  }
}
</style>

<style lang="scss">
.summary-wrapper {
  .textarea-wrapper {
    height: 280px;
    textarea {
      height: 100%;
    }
  }
}

.summary-error {
  textarea {
    border: 1px solid var(--error-primary-color);
  }
}
</style>
