<template>
  <BaseInput
    v-model="header"
    label="Header"
    placeholder="Enter the header"
    class="header"
  />
  <BaseTextarea
    v-model="text"
    label="Text"
    placeholder="Enter the text"
    class="text"
  />

  <div class="buttons">
    <BaseButton
      :is-not-background="true"
      :button-loading="buttonAISummaryLoading"
      @click="$emit('create-ai-summary')"
    >
      AI Summary
    </BaseButton>
    <BaseButton @click="$emit('save-summary', header, text)">
      <SaveIcon /> Save
    </BaseButton>
  </div>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'

import BaseButton from '@/components/common/BaseButton'
import BaseInput from '@/components/common/BaseInput'
import BaseTextarea from '@/components/common/BaseTextarea'
import SaveIcon from '@/components/icons/SaveIcon'

const {mapState} = createNamespacedHelpers('twentyFourSeven')

export default {
  name: 'TFSSummaryTab',
  components: {BaseInput, BaseTextarea, BaseButton, SaveIcon},
  emits: ['save-summary', 'create-ai-summary'],
  props: {
    post: {type: Object, required: true},
    buttonAISummaryLoading: {type: Boolean, required: true},
  },
  data() {
    return {
      newHeader: null,
      newText: null,
    }
  },
  computed: {
    ...mapState(['aiSummary']),
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
        return this.newText || this.aiSummary || this.post.text
      },
      set(value) {
        this.newText = value
      },
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
