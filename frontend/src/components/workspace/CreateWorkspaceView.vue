<template>
  <MainLayout :is-two-columns="true">
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
  name: 'CreateWorkspaceView',
  components: {
    MainLayout,
  },
}
</script>

<style lang="scss" scoped>
.second-column {
  width: 45vw;
  height: 100%;
  padding: 32px 32px 0 16px;
}
</style>
