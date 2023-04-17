<template>
  <MainLayout>
    <div class="header">
      <MainLayoutTitleBlock
        title="Alerts"
        description="Set up alerts for your project with highly customized filters"
        :back-page="{name: 'main page', routName: 'MainView'}"
      />

      <BaseButton @click="$emit('create-alert')">
        Create new report
      </BaseButton>
    </div>
    <template v-if="alerts.length"> </template>
    <div v-else class="no-alerts">
      <img src="@/assets/alerts/no-alerts.svg" alt="No alerts image" />
      <div class="no-alerts__text">
        No alerts created
        <img
          src="@/assets/alerts/mailbox.svg"
          alt="open mailbox with raised flag image"
        />
      </div>
    </div>
  </MainLayout>
</template>

<script>
import MainLayout from '@/components/layout/MainLayout'
import MainLayoutTitleBlock from '@components/layout/MainLayoutTitleBlock'

import BaseButton from '@/components/common/BaseButton'

export default {
  name: 'AlertsScreen',
  components: {MainLayout, MainLayoutTitleBlock, BaseButton},
  props: {
    alerts: {type: Array, default: () => []},
  },
}
</script>

<style lang="scss" scoped>
.header {
  display: flex;
  justify-content: space-between;
}

.no-alerts {
  display: flex;
  align-items: center;
  flex-direction: column;

  gap: 30px;

  &__text {
    display: flex;

    gap: 10px;
  }
}
</style>
