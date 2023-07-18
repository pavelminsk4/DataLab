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
        :dir="summaryLanguage"
        label="Header"
        placeholder="Enter the header"
        class="header"
      />
      <BaseTextarea
        v-model="text"
        label="Text"
        placeholder="Enter the text"
        error-message="Clear the field to create AI summary!"
        :dir="summaryLanguage"
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
        AI Summary
      </BaseButton>
      <BaseButton
        :button-loading="buttonSaveLoading"
        @click="$emit('save-summary', header, text)"
      >
        <SaveIcon /> Save
      </BaseButton>
    </div>
  </div>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'

import BaseButton from '@/components/common/BaseButton'
import BaseInput from '@/components/common/BaseInput'
import BaseTextarea from '@/components/common/BaseTextarea'
import SaveIcon from '@/components/icons/SaveIcon'
import BaseSpinner from '@/components/BaseSpinner'
import TFSLanguagesTabs from '@/components/twenty-four-seven/TFSLanguagesTabs'

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
      newText: null,
      isFieldClear: true,
      loadingTranslation: false,
      newSelectedLanguage: this.post.online_post.feed_language__language,
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
        return (
          this.newHeader ||
          this.post.header ||
          this.post.online_post.entry_title
        )
      },
      set(value) {
        this.newHeader = value
      },
    },
    text: {
      get() {
        if (this.newText === '') return this.newText
        return this.newText || this.post.text || this.post.online_post.full_text
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
    ...mapActions([
      action.CLEAR_TFS_AI_SUMMARY,
      action.UPDATE_AI_SUMMARY_LANGUAGE,
    ]),
    async changeLanguage(newLanguage) {
      this.loadingTranslation = true
      this.selectedLanguage = newLanguage

      try {
        await this[action.UPDATE_AI_SUMMARY_LANGUAGE]({
          newLanguage: newLanguage.toLowerCase(),
          header: this.header || '',
          text: this.text || '',
        })

        this.newHeader = this.translatedText.header
        this.newText = this.translatedText.text
      } catch (error) {
        console.error(error)
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
      this.newText = this.aiSummary
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
