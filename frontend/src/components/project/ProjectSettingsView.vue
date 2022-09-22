<template>
  <MainLayout>
    <SettingsNav />

    <ReportsScreen />
  </MainLayout>
</template>

<script>
import MainLayout from '@/components/layout/MainLayout'
import SettingsNav from '@/components/navigation/SettingsNav'
import ReportsScreen from '@/components/project/screens/ReportsScreen'

export default {
  name: 'ProjectReports',
  components: {ReportsScreen, SettingsNav, MainLayout},
}
</script>

<style scoped>
.project-nav {
  margin-top: 30px;
}
</style>
