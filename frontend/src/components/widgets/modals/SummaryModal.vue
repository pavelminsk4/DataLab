<template>
  <BaseModal>
    <div class="main-title">Summary</div>
    <BaseCheckbox :model-value="true">
      <span class="name">Show all</span>
    </BaseCheckbox>
  </BaseModal>
</template>

<script>
import BaseModal from '@/components/modals/BaseModal'
import BaseCheckbox from '@/components/BaseCheckbox'

export default {
  name: 'SummaryModal',
  components: {BaseCheckbox, BaseModal},
}
</script>

<style scoped>
.main-title {
  margin-bottom: 30px;
}

.name {
  margin-left: 10px;

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
}
</style>
