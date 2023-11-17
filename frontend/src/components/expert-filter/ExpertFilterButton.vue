<template>
  <BaseButton class="expert-filter-button">
    <ExpertFilterIcon />
    <span>Expert Filter</span>
  </BaseButton>
</template>

<script>
import BaseButton from '@components/common/BaseButton'
import ExpertFilterIcon from '@components/icons/ExpertFilterIcon'

export default {
  name: 'ExpertFilterButton',
  components: {BaseButton, ExpertFilterIcon},
}
</script>

<style lang="scss" scoped>
.expert-filter-button {
  background-color: #e0f5ff;
  border-color: #e0f5ff;

  color: #006496;

  svg {
    color: #006496;
  }
}
</style>
