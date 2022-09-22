<template>
  <div class="report-wrapper">
    <div class="general-wrapper">
      <div class="title">Recipient's email</div>
      <BaseTag />

      <div class="title">Email Title</div>
      <BaseInput />

      <section class="extra-settings"></section>
    </div>
  </div>
</template>

<script>
import BaseTag from '@/components/BaseTag'
import BaseInput from '@/components/BaseInput'
export default {
  name: 'ReportsScreen',
  components: {BaseInput, BaseTag},
}
</script>

<style lang="scss" scoped>
.report-wrapper {
  display: flex;

  .general-wrapper {
    .title {
      margin-bottom: 12px;

      font-style: normal;
      font-weight: 500;
      font-size: 14px;
      line-height: 110%;
      color: var(--primary-text-color);
    }
  }
}
</style>
