<template>
  <BaseTextarea
    v-model="report"
    label="Report"
    placeholder="Enter the report"
  />

  <div class="buttons">
    <BaseButton :is-disabled="true"> <SaveIcon /> Save </BaseButton>
    <BaseButton :is-not-background="true" :is-disabled="true"
      >Send to Watsapp</BaseButton
    >
  </div>
</template>

<script>
import BaseButton from '@/components/common/BaseButton'
import BaseTextarea from '@/components/common/BaseTextarea'
import SaveIcon from '@/components/icons/SaveIcon'

export default {
  name: 'TFSStoryReportTab',
  components: {BaseTextarea, BaseButton, SaveIcon},
  emits: ['save-summary'],
  props: {
    post: {type: Object, required: true},
  },
  data() {
    return {
      report: '',
    }
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
