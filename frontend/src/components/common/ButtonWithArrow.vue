<template>
  <BaseButton v-bind="$attrs">
    <slot></slot>
    <ArrowLeftIcon class="button-arrow-icon" />
  </BaseButton>
</template>

<script>
import ArrowLeftIcon from '@/components/icons/ArrowLeftIcon'
import BaseButton from '@/components/common/BaseButton'

export default {
  name: 'ButtonWithArrow',
  components: {ArrowLeftIcon, BaseButton},
}
</script>

<style scoped>
.button-arrow-icon {
  margin-left: 10px;
  transform: rotate(180deg);
}
</style>
