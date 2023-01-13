<template>
  <div class="blank-page-wrapper">
    <component class="type-icon" :is="pageName + 'Icon'" />
    No {{ formatWord(pageName) }} created
  </div>
</template>

<script>
import {splitToSeparateWords} from '@lib/utilities'

import AlertsIcon from '@/components/icons/AlertsIcon'
import WorkspaceIcon from '@/components/icons/WorkspaceIcon'
import RegularReportsIcon from '@/components/icons/RegularReportsIcon'

export default {
  name: 'BlankPage',
  components: {WorkspaceIcon, RegularReportsIcon, AlertsIcon},
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
