<template>
  <MainLayout :is-two-columns="true" width-second-columns="39%">
    <template #default>
      <router-view></router-view>
    </template>

    <template #second-column>
      <div class="second-column">
        <router-view name="secondColumn"></router-view>
      </div>
    </template>
  </MainLayout>
</template>

<script>
import MainLayout from '@components/layout/MainLayout'

export default {
  name: 'CreateReportView',
  components: {
    MainLayout,
  },
}
</script>

<style lang="scss" scoped>
.second-column {
  height: 100%;
  padding: 32px 32px 0 16px;
}
</style>
