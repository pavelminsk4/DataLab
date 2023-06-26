<template>
  <TFSLanguagesTabs
    v-if="isSummaryTab"
    :languages-tabs="languagesTabs"
    :selected-language="selectedLanguage"
    @change-language="changeAISummaryLanguage"
  />

  <BaseInput
    v-model="header"
    label="Header"
    placeholder="Enter the header"
    class="header"
  />
  <BaseTextarea v-model="text" label="Text" placeholder="Enter the text" />

  <div class="buttons">
    <BaseButton
      v-if="isSummaryTab"
      :is-not-background="true"
      :button-loading="buttonAISummaryLoading"
      @click="$emit('create-ai-summary')"
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
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'

import BaseButton from '@/components/common/BaseButton'
import BaseInput from '@/components/common/BaseInput'
import BaseTextarea from '@/components/common/BaseTextarea'
import SaveIcon from '@/components/icons/SaveIcon'
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
  components: {BaseInput, BaseTextarea, BaseButton, SaveIcon, TFSLanguagesTabs},
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
      selectedLanguage: LANGUAGES_NAMES.ENGLISH,
    }
  },
  computed: {
    ...mapState(['aiSummary', 'translatedAISummary']),
    header: {
      get() {
        if (this.newHeader === '') return this.newHeader
        return this.newHeader || this.post.header
      },
      set(value) {
        this.newHeader = value
      },
    },
    text: {
      get() {
        if (this.newText === '') return this.newText
        return (
          this.translatedAISummary ||
          this.aiSummary ||
          this.newText ||
          this.post.text
        )
      },
      set(value) {
        this.newText = value
        this[action.CLEAR_TFS_AI_SUMMARY]()
      },
    },
    isSummaryTab() {
      return this.currentTab === TABS.SUMMARY
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
    changeAISummaryLanguage(newLanguage) {
      this.selectedLanguage = newLanguage

      this[action.UPDATE_AI_SUMMARY_LANGUAGE]({
        newLanguage: newLanguage.toLowerCase(),
        text: this.text,
      })
    },
  },
}
</script>

<style lang="scss" scoped>
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
</style>
