<template>
  <MainLayout>
    <SettingsNav />

    <div class="settings-content">
      <slot></slot>
    </div>
  </MainLayout>
</template>

<script>
import MainLayout from '@/components/layout/MainLayout'
import SettingsNav from '@/components/navigation/SettingsNav'

export default {
  name: 'ProjectSettingsLayout',
  components: {
    SettingsNav,
    MainLayout,
  },
}
</script>

<style scoped>
.settings-content {
  margin-top: 80px;
}
</style>
