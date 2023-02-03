<template>
  <div class="blank-page-wrapper">
    <component class="type-icon" :is="pageName + 'EmptyIcon'" />
    No {{ formatWord(pageName) }} created
  </div>
</template>

<script>
import {splitToSeparateWords} from '@lib/utilities'

import AlertsEmptyIcon from '@/components/icons/AlertsEmptyIcon'
import WorkspaceEmptyIcon from '@/components/icons/WorkspaceEmptyIcon'
import RegularReportsEmptyIcon from '@/components/icons/RegularReportsEmptyIcon'

export default {
  name: 'BlankPage',
  components: {WorkspaceEmptyIcon, RegularReportsEmptyIcon, AlertsEmptyIcon},
  props: {
    pageName: {
      type: String,
      required: true,
    },
  },
  methods: {
    formatWord(word) {
      return splitToSeparateWords(word)
    },
  },
}
</script>

<style scoped>
.blank-page-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  gap: 25px;

  margin-top: 150px;

  color: var(--primary-text-color);
}
</style>
